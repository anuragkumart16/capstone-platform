from django.contrib import admin
from django.urls import path
from capstone.views import LoginView,SignupView,LandingView,HomeView,QuriesView,SubmitProjectView,otprequest
from panel.views import MentorLoginAPIView
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
]

if settings.DEBUG:  # Only serve media files during development
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
