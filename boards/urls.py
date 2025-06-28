from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BoardViewSet, TaskViewSet, RegisterUserView

# DefaultRouter will automatically generate URL patterns for the Board and Task views.
router = DefaultRouter()
router.register(r'boards', BoardViewSet, basename='board')
router.register(r'tasks', TaskViewSet, basename='task')

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('', include(router.urls)),
]