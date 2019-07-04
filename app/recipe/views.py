from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Tag

from recipe import serializers
# Only going to include the list functionality


class TagViewSet(viewsets.GenericViewSet,
                 mixins.ListModelMixin,
                 mixins.CreateModelMixin):
    """
    Manage tags in the database
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    # what query is called when this view set is called
    queryset = Tag.objects.all()
    serializer_class = serializers.TagSerializer

    def get_queryset(self):
        """
        Return objects for the current authenticated user only
        """
        # -name returns order in reverse order
        return self.queryset.filter(user=self.request.user).order_by('-name')

    def perform_create(self, serializer):
        """
        Create a new tag
        :param serializer:
        """
        serializer.save(user=self.request.user)
