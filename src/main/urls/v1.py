
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

app_name = 'api_v1'

schema_view = get_schema_view(
   openapi.Info(
      title='Test task',
      default_version='v1',
      description='Test description',
      terms_of_service='https://www.google.com/policies/terms/',
      contact=openapi.Contact(email='name@namovich.name'),
      license=openapi.License(name='BSD License'),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('a12n/', include('a12n.urls')),
    path('', include('users.urls')),
    path('docs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
