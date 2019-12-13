from django.urls import path, include
from .views import PostRudView, PostListCreateView
# app_name="API"
urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('<int:pk>/', PostRudView.as_view(), name="post-rud"),
    path('',PostListCreateView.as_view(), name="post-ListCreate")
]
