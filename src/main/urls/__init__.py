from django.contrib import admin
from django.urls import include, path

api = [
    path('', include('main.urls.v1', namespace='v1')),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api)),
]
