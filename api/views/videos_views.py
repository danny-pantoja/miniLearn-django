from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user, authenticate, login, logout
from django.middleware.csrf import get_token

from ..models.videos import Videos
from ..serializers import VideosSerializer, UserSerializer

# Create your views here.
class Videos(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    serializer_class = VideosSerializer
    def get(self, request):
        """Index request"""
        # Get all the Content:
        # Filter the content by owner, so you can only see your owned content
        videos = Videos.objects.filter(owner=request.user.id)
        # Run the data through the serializer
        data = VideosSerializer(videos, many=True).data
        return Response({ 'videos': data })

    def post(self, request):
        """Create request"""
        # Add user to request data object
        request.data['videos']['owner'] = request.user.id
        # Serialize/create videos
        videos = VideosSerializer(data=request.data['videos'])
        # If the videos data is valid according to our serializer...
        if videos.is_valid():
            # Save the created videos & send a response
            videos.save()
            return Response({ 'videos': videos.data }, status=status.HTTP_201_CREATED)
        # If the data is not valid, return a response with the errors
        return Response(videos.errors, status=status.HTTP_400_BAD_REQUEST)

class VideosDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)
    def get(self, request, pk):
        """Show request"""
        # Locate the videos to show
        videos = get_object_or_404(Videos, pk=pk)
        # Only want to show owned videos?
        if not request.user.id == videos.owner.id:
            raise PermissionDenied('Unauthorized, you do not own this content')

        # Run the data through the serializer so it's formatted
        data = VideosSerializer(videos).data
        return Response({ 'videos': data })

    def delete(self, request, pk):
        """Delete request"""
        # Locate videos to delete
        videos = get_object_or_404(Videos, pk=pk)
        # Check the videos's owner against the user making this request
        if not request.user.id == videos.owner.id:
            raise PermissionDenied('Unauthorized, you do not own this content')
        # Only delete if the user owns the  videos
        videos.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk):
        """Update Request"""
        # Remove owner from request object
        # This "gets" the owner key on the data['videos'] dictionary
        # and returns False if it doesn't find it. So, if it's found we
        # remove it.
        if request.data['videos'].get('owner', False):
            del request.data['videos']['owner']

        # Locate videos
        # get_object_or_404 returns a object representation of our Content
        videos = get_object_or_404(Videos, pk=pk)
        # Check if user is the same as the request.user.id
        if not request.user.id == videos.owner.id:
            raise PermissionDenied('Unauthorized, you do not own this content')

        # Add owner to data object now that we know this user owns the resource
        request.data['videos']['owner'] = request.user.id
        # Validate updates with serializer
        data = VideosSerializer(videos, data=request.data['videos'])
        if data.is_valid():
            # Save & send a 204 no content
            data.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        # If the data is not valid, return a response with the errors
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
