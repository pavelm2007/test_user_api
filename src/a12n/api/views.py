import requests
from django.conf import settings
from requests.exceptions import HTTPError
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from social_django.utils import psa

from a12n.api.serializers import SocialSerializer


@api_view(http_method_names=['POST'])
@permission_classes([AllowAny])
def vk_oauth2_access_token(request):
    # Get access token from VK account
    response = requests.get(
        'https://oauth.vk.com/access_token',
        params={
            'client_id': settings.SOCIAL_AUTH_VK_OAUTH2_KEY,
            'client_secret': settings.SOCIAL_AUTH_VK_OAUTH2_SECRET,
            'redirect_uri': 'http://FRONTENT_URL/auth/vk/',
            'code': request.query_params.get('code'),
        },
    )
    data = response.json()

    return Response({'access_token': data['access_token']})


@api_view(http_method_names=['POST'])
@permission_classes([AllowAny])
@psa()
def user_token(request, backend):
    # Registering or logging in a user with a social account and
    # sending a site authorization token

    serializer = SocialSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        try:
            nfe = settings.NON_FIELD_ERRORS_KEY
        except AttributeError:
            nfe = 'non_field_errors'

        try:
            user = request.backend.do_auth(serializer.validated_data['access_token'])
        except HTTPError as e:
            return Response(
                {
                    'errors': {
                        'token': 'Invalid token',
                        'detail': str(e),
                    },
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        if user:
            if user.is_active:
                token, _ = Token.objects.get_or_create(user=user)
                return Response({'token': token.key})
            else:
                return Response(
                    {'errors': {nfe: 'This user account is inactive'}},
                    status=status.HTTP_400_BAD_REQUEST,
                )
        else:
            return Response(
                {'errors': {nfe: 'Authentication Failed'}},
                status=status.HTTP_400_BAD_REQUEST,
            )
