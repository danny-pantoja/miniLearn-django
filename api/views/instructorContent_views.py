from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user, authenticate, login, logout
from django.middleware.csrf import get_token

from ..models.instructorContent import InstructorContent
from ..serializers import InstructorContentSerializer, UserSerializer

# Create your views here.
class InstructorContent(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    serializer_class = InstructorContentSerializer
    def get(self, request):
        """Index request"""
        # Get all the Content:
        # Filter the content by owner, so you can only see your owned content
        instructorContent = InstructorContent.objects.filter(owner=request.user.id)
        # Run the data through the serializer
        data = InstructorContentSerializer(instructorContent, many=True).data
        return Response({ 'instructorContent': data })

    def post(self, request):
        """Create request"""
        # Add user to request data object
        request.data['instructorContent']['owner'] = request.user.id
        # Serialize/create instructorContent
        instructorContent = InstructorContentSerializer(data=request.data['instructorContent'])
        # If the instructorContent data is valid according to our serializer...
        if instructorContent.is_valid():
            # Save the created instructorContent & send a response
            instructorContent.save()
            return Response({ 'instructorContent': instructorContent.data }, status=status.HTTP_201_CREATED)
        # If the data is not valid, return a response with the errors
        return Response(instructorContent.errors, status=status.HTTP_400_BAD_REQUEST)

class InstructorContentDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)
    def get(self, request, pk):
        """Show request"""
        # Locate the instructorContent to show
        instructorContent = get_object_or_404(InstructorContent, pk=pk)
        # Only want to show owned instructorContent?
        if not request.user.id == instructorContent.owner.id:
            raise PermissionDenied('Unauthorized, you do not own this content')

        # Run the data through the serializer so it's formatted
        data = InstructorContentSerializer(instructorContent).data
        return Response({ 'instructorContent': data })

    def delete(self, request, pk):
        """Delete request"""
        # Locate instructorContent to delete
        instructorContent = get_object_or_404(InstructorContent, pk=pk)
        # Check the instructorContent's owner against the user making this request
        if not request.user.id == instructorContent.owner.id:
            raise PermissionDenied('Unauthorized, you do not own this content')
        # Only delete if the user owns the  instructorContent
        instructorContent.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk):
        """Update Request"""
        # Remove owner from request object
        # This "gets" the owner key on the data['instructorContent'] dictionary
        # and returns False if it doesn't find it. So, if it's found we
        # remove it.
        if request.data['instructorContent'].get('owner', False):
            del request.data['instructorContent']['owner']

        # Locate instructorContent
        # get_object_or_404 returns a object representation of our Content
        instructorContent = get_object_or_404(InstructorContent, pk=pk)
        # Check if user is the same as the request.user.id
        if not request.user.id == instructorContent.owner.id:
            raise PermissionDenied('Unauthorized, you do not own this content')

        # Add owner to data object now that we know this user owns the resource
        request.data['instructorContent']['owner'] = request.user.id
        # Validate updates with serializer
        data = InstructorContentSerializer(instructorContent, data=request.data['instructorContent'])
        if data.is_valid():
            # Save & send a 204 no content
            data.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        # If the data is not valid, return a response with the errors
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
