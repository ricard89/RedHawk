#serializers
from rest_framework import generics, permissions
from api.permissions import IsOwner
from api.serializers import TagSerializer, UserSerializer
from main_app.models import Tag
#from django.contrib.auth.models import User
from accounts.models import User


# Create your views here.
class TagCreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
       user = self.request.user
       return Tag.objects.filter(owner=user)

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save(owner=self.request.user)


class TagDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)


class UserView(generics.ListAPIView):
    """View to list the user queryset."""
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailsView(generics.RetrieveAPIView):
    """View to retrieve a user instance."""
    queryset = User.objects.all()
    serializer_class = UserSerializer
