from django.contrib import admin
from django.urls import path
from capstone.views import LoginView,SignupView,LandingView,HomeView,QuriesView,SubmitProjectView,otprequest
from panel.views import MentorLoginAPIView,GetStudentDetails,GetUserData,SetMarksView,QueryHandlingView,GetQueryView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',HomeView,name='home'), #first page on visiting the website
    path('signin',LoginView,name='login'), #login-page
    path('signup',SignupView,name='signup'), #signup page 
    path('landingpage/',LandingView, name='landingpage'), #protected url 
    path('query',QuriesView,name='query'),
    path('submitproject',SubmitProjectView,name='submitproject'),
    path('optrequest',otprequest.as_view(),name='otpcheck'),

    # api-end-points
    path('mentor-login',MentorLoginAPIView.as_view(),name='mentor-login'),
    path('mentor-student-data',GetStudentDetails.as_view(),name='mentor-student-data'),
    path('get-student-data',GetUserData.as_view(),name='get-user-data'),
    path('set-marks',SetMarksView.as_view(),name='set-marks'),
    path('query-handler',QueryHandlingView.as_view(),name='query-handler'),
    path('get-query',GetQueryView.as_view(),name='get-query')
]

if settings.DEBUG:  # Only serve media files during development
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
