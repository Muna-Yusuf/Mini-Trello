from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Board, Task


class RegisterSerializer(serializers.ModelSerializer):
    """Serializer for user registration."""
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class BoardSerializer(serializers.ModelSerializer):
    """Serializer for boards."""
    
    owner = serializers.CharField(source='owner.username', read_only=True)
    class Meta:
        model = Board
        fields = ['id', 'name', 'owner']
        read_only_fields = ['id', 'owner']


class TaskSerializer(serializers.ModelSerializer):
    """Serializer for tasks."""
    board = serializers.PrimaryKeyRelatedField(queryset=Board.objects.all())

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'status', 'board']
        read_only_fields = ['id']
        extra_kwargs = {'status': {'default': 'todo'}}

    def validate_board(self, board):
        """Ensure the task can only be assigned to a board owned by the current user."""
        request = self.context['request']
        if board.owner != request.user:
            raise serializers.ValidationError("You can only assign tasks to your own boards.")
        return board
