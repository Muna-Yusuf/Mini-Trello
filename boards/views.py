from django.contrib.auth.models import User
from rest_framework import generics, serializers, viewsets, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from .models import Board, Task
from .serializers import BoardSerializer, TaskSerializer, RegisterSerializer


class RegisterUserView(generics.CreateAPIView):
    """View for registering a new user."""
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)

        user_data = response.data
        return Response({
            'user': user_data,
        })


class BoardViewSet(viewsets.ModelViewSet):
    """ViewSet for managing boards."""
    serializer_class = BoardSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Only return boards owned by the current authenticated user."""
        if not self.request.user.is_authenticated:
            return Board.objects.none()
        return Board.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        """Associate the new board with the current authenticated user."""
        serializer.save(owner=self.request.user)

    def perform_update(self, serializer):
        serializer.save(owner=self.request.user)

    def destroy(self, request, *args, **kwargs):
        board = self.get_object()
        if board.owner != request.user:
            return Response({'error': 'Unauthorized'}, status=status.HTTP_403_FORBIDDEN)
        return super().destroy(request, *args, **kwargs)


class TaskViewSet(viewsets.ModelViewSet):
    """ViewSet for managing tasks."""
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Only return tasks that belong to boards owned by the current authenticated user."""
        if not self.request.user.is_authenticated:
            return Task.objects.none()
        return Task.objects.filter(board__owner=self.request.user)

    def perform_create(self, serializer):
        """Ensure the user can only create tasks on boards they own."""
        board = serializer.validated_data.get('board')
        if board.owner != self.request.user:
            raise serializers.ValidationError("You can't add a task to someone else's board.")
        serializer.save()

    def perform_update(self, serializer):
        board = serializer.validated_data.get('board', None)
        if board and board.owner != self.request.user:
            raise serializers.ValidationError("You can't assign a task to someone else's board.")
        serializer.save()

    def update(self, request, *args, **kwargs):
        """Ensure the user can only update tasks on boards they own."""
        task = self.get_object()
        if task.board.owner != request.user:
            return Response({'error': 'Unauthorized'}, status=status.HTTP_403_FORBIDDEN)
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """Ensure the user can only delete tasks from boards they own."""
        task = self.get_object()
        if task.board.owner != request.user:
            return Response({'error': 'Unauthorized'}, status=status.HTTP_403_FORBIDDEN)
        return super().destroy(request, *args, **kwargs)