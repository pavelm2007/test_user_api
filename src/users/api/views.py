from rest_framework import mixins, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from users.api.filters import UserFilter
from users.api.serializers import UserSerializer
from users.models import User


class CurrentUserView(APIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        """Current user"""
        serializer = self.serializer_class(request.user)

        return Response(serializer.data)

    def patch(self, request, *args, **kwargs):
        """Editing current user"""
        serializer = self.serializer_class(request.user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)


class UserViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    filterset_class = UserFilter
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        """List users id"""
        queryset = self.filter_queryset(self.get_queryset())
        ids = [q.id for q in queryset]

        return Response(ids)
