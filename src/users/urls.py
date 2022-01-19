from django.urls import path
from rest_framework.routers import DefaultRouter

from users.api import views

app_name = 'users'

router = DefaultRouter()
router.register('users', views.UserViewSet)

urlpatterns = [
    path('user/', views.CurrentUserView.as_view()),
]
urlpatterns += router.urls
