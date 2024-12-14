from django.contrib import admin
from django.urls import path
from capstone.views import LoginView,SignupView,LandingView,HomeView,QuriesView,SubmitProjectView,otprequest
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

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
    path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('tokenrefresh', TokenRefreshView.as_view(), name='token_refresh'),
]


