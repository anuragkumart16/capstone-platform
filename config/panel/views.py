from django.shortcuts import render,redirect
from django.contrib import messages
from .models import MentorModel
from django.db import IntegrityError
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import MentorSerializer


# Create your views here.
class MentorLoginAPIView(APIView):
    def post(self,request):
        data = request.data
        username = data['username']
        password = data['password']
        try:
            instance = MentorModel.objects.get(name=username)
            if instance.password == password:
                return Response({
                    'LoggedIn': True,
                    'message': 'Login Successful!'
                },status.HTTP_200_OK)
            else:
                return Response({
                    'LoggedIn':False,
                    'message': 'Login Failed!, Check Password!'
                },status.HTTP_401_UNAUTHORIZED)
        except MentorModel.DoesNotExist:
                return Response({
                    'LoggedIn': False,
                    'message':'User Not Found, Contact Admin'
                })
        


def SignupView(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        try:
            instance = MentorModel(name = name,email=email,password=password)
            instance.save()
        except IntegrityError:
            messages.warning(request,'Email is already taken!')
            return redirect('signup')
        return redirect(f'landingpage/?userdata={name}')
    else:
        return render(request,'signup.html')


def LandingView(request):
    Username = request.GET.get('username')
    return render(request,'landingpage.html',{'username':Username})



# student apis

# class StudentView(APIView):
#     def post (self,request):
#         data = request.data
#         serializer = UserSerializer(data = data)
#         if not serializer.is_valid():
#             instance = StudentModel(student=data['studentEmail'],Mentor_name = data['mentorName'],figma_link=data['figmaLink'],hosted_link=data['hostedLink'],github_link=data['githubLink'],explanation_link=data['explanationLink'])
#             instance.save()
#             return Response({
#                 'status': 400,
#                 'message':serializer.errors
#             },status.HTTP_400_BAD_REQUEST)
#         else:
#             instance = User.objects.create(username = data['username'])
#             instance.set_password(data['password'])
#             instance.save()
#             return Response({
#                 'status' : 201,
#                 'message':'User Creation Successful'
#             },status.HTTP_201_CREATED)
    
#     def get (self,request):
#         # self.permission_classes = [IsAuthenticated]
#         # self.check_permissions(request)
#         obj = User.objects.all()
#         serializer = UserSerializer(obj,many=True)
#         return Response({
#             'status':200,
#             'message':'Fetch Successful',
#             'data' : serializer.data
#         },status.HTTP_200_OK)