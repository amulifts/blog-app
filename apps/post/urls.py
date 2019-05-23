from django.urls import path
from apps.post import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path("", views.index),
    path("create/", views.PostCreateView.as_view(), name="create-post"),
    path("detail/<slug>", views.PostDetailView.as_view(), name="detail"),
    path("<id>/comment/", views.create_comment, name="create-comment"),
    path("list/", views.PostListView.as_view(), name="list"),
]
