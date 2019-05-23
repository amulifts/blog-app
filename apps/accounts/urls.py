from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from apps.accounts.views import SignupFormView
from apps.post import views

urlpatterns = [
    path("login/", LoginView.as_view(template_name="accounts/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="accounts/logout.html"), name="logout"),
    path("signup/", SignupFormView.as_view(), name="signup"),
    path("signup-success/", views.index, name="success"),
]