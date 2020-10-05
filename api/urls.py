from django.urls import path
from .views.mango_views import Mangos, MangoDetail
from .views.user_views import SignUp, SignIn, SignOut, ChangePassword
from .views.instructor_content_views import InstructorContent, InstructorContentDetails
from .views.videos_views import Videos, VideosDetails

urlpatterns = [
  	# Restful routing
    path('mangos/', Mangos.as_view(), name='mangos'),
    path('mangos/<int:pk>/', MangoDetail.as_view(), name='mango_detail'),
    path('sign-up/', SignUp.as_view(), name='sign-up'),
    path('sign-in/', SignIn.as_view(), name='sign-in'),
    path('sign-out/', SignOut.as_view(), name='sign-out'),
    path('change-pw/', ChangePassword.as_view(), name='change-pw'),
    path('instructor-content/', InstructorContent.as_view(), name='instructor_content'),
    path('instructor-content/<int:pk>/', InstructorContentDetails.as_view(), name='instructor_content'),
    path('videos/', Videos.as_view(), name='videos'),
    path('videos/<int:pk>/', VideosDetails.as_view(), name='videos'),

]
