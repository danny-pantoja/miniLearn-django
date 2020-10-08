from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user, authenticate, login, logout
from django.middleware.csrf import get_token

from ..models.video import Video
from ..serializers import VideoSerializer, UserSerializer

# Create your views here.
class Videos(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    serializer_class = VideoSerializer
    def get(self, request):
        """Index request"""
        # Get all the Content:
        # Filter the content by owner, so you can only see your owned content
        videos = Video.objects.filter(owner=request.user.id)
        # Run the data through the serializer
        data = VideoSerializer(videos, many=True).data
        return Response({ 'videos': data })

    def post(self, request):
        """Create request"""
        # Add user to request data object
        request.data['video']['owner'] = request.user.id
        # Serialize/create videos
        video = VideoSerializer(data=request.data['video'])
        # If the videos data is valid according to our serializer...
        if video.is_valid():
            # Save the created videos & send a response
            video.save()
            return Response({ 'video': video.data }, status=status.HTTP_201_CREATED)
        # If the data is not valid, return a response with the errors
        return Response(video.errors, status=status.HTTP_400_BAD_REQUEST)

class VideoDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)
    def get(self, request, pk):
        """Show request"""
        # Locate the videos to show
        video = get_object_or_404(Video, pk=pk)
        # Only want to show owned video?
        if not request.user.id == video.owner.id:
            raise PermissionDenied('Unauthorized, you do not own this content')

        # Run the data through the serializer so it's formatted
        data = VideosSerializer(video).data
        return Response({ 'video': data })

    def delete(self, request, pk):
        """Delete request"""
        # Locate video to delete
        videos = get_object_or_404(Video, pk=pk)
        # Check the video's owner against the user making this request
        if not request.user.id == video.owner.id:
            raise PermissionDenied('Unauthorized, you do not own this content')
        # Only delete if the user owns the  video
        video.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk):
        """Update Request"""
        # Remove owner from request object
        # This "gets" the owner key on the data['video'] dictionary
        # and returns False if it doesn't find it. So, if it's found we
        # remove it.
        if request.data['video'].get('owner', False):
            del request.data['video']['owner']

        # Locate video
        # get_object_or_404 returns a object representation of our Content
        video = get_object_or_404(Video, pk=pk)
        # Check if user is the same as the request.user.id
        if not request.user.id == video.owner.id:
            raise PermissionDenied('Unauthorized, you do not own this content')

        # Add owner to data object now that we know this user owns the resource
        request.data['video']['owner'] = request.user.id
        # Validate updates with serializer
        data = VideosSerializer(video, data=request.data['video'])
        if data.is_valid():
            # Save & send a 204 no content
            data.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        # If the data is not valid, return a response with the errors
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
