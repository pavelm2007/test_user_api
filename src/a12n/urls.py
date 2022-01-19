from django.urls import path

from a12n.api.views import user_token

urlpatterns = [
    path('auth/<str:backend>/', user_token),
]
