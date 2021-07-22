from django.urls import path

from petstagram.accounts.views import login_user, register_user, logout_user, profile_details

urlpatterns = [
    path('login/', login_user, name='log in user'),
    path('register/', register_user, name='register user'),
    path('logout/', logout_user, name='log out user'),
    path('profile/', profile_details, name='profile details'),
]
