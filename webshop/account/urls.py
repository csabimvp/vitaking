from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

app_name = "account"

urlpatterns = [
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path(
        "password_change/",
        auth_views.PasswordChangeView.as_view(),
        name="password_change",
    ),
    path(
        "password_change/done/",
        auth_views.PasswordChangeDoneView.as_view(),
        name="password_change_done",
    ),
    path("register/", views.register, name="register"),
    path("profile/", views.user_profile, name="user_profile"),
    path("profile/edit", views.user_profile_edit, name="user_profile_edit"),
]

