
from django.urls import path
from . import views

urlpatterns = [
    path('threads/', views.ThreadListCreateView.as_view(), name='thread-list-create'),
    path('threads/<int:pk>/', views.ThreadRetrieveUpdateDestroyView.as_view(), name='thread-detail'),

    path('comments/', views.CommentListCreateView.as_view(), name='comment-list-create'),
    path('comments/<int:pk>/', views.CommentRetrieveUpdateDestroyView.as_view(), name='comment-detail'),

    path('stories/', views.StoryListCreateView.as_view(), name='story-list-create'),
    path('stories/<int:pk>/', views.StoryRetrieveUpdateDestroyView.as_view(), name='story-detail'),

    path('photos/', views.PhotoListCreateView.as_view(), name='photo-list-create'),
    path('photos/<int:pk>/', views.PhotoRetrieveUpdateDestroyView.as_view(), name='photo-detail'),
]
