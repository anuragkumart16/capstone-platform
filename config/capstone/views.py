from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
from .models import CapstoneModel,QueryModel,SubmissionModel
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.db.utils import IntegrityError
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from .serializers import OtprequestSerializer

# Create your views here.
def HomeView(request):
    # return render(request,'index.html')
    return redirect('login')

def LoginView(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Signin Successful!")
            return redirect('home') 
        else:
            messages.error(request, "Invalid username or password")
    return render(request, 'signin.html')  


def SignupView(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        mentor = request.POST.get('mentor')
        figma = request.POST.get('figma')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
            return redirect('signup')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return redirect('signup')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        login(request, user)
        # saving additional information to capstone model
        instance = CapstoneModel(student = username,mentor=mentor,figma_link=figma)
        instance.save()
        messages.success(request,'Created Account Successfully!')
        return redirect('landingpage')  
    else:
        return render(request,'signup.html')
    

# @login_required
def LandingView(request):
    # referer = request.META.get('HTTP_REFERER')  
    # if not referer:
    #     return HttpResponseForbidden("Access denied: direct access not allowed")
    return render(request,'landingpage.html')

# @login_required
def QuriesView(request):
    if request.method == 'POST':
        # getting all values
        student = request.user.username
        query = request.POST.get('query')
        file = request.FILES['file']
        # checking if the user is signed in
        if student == "":
            messages.warning(request,'You need to SignIn First!')
            return redirect('signin')
        # automatically filling mentor
        instance = CapstoneModel.objects.get(student = student)
        mentor = instance.mentor
        instance = QueryModel(query=query,file=file,student=student,mentor=mentor)
        instance.save()
        messages.success(request,'query saved successfully!')
        return redirect('query')
    else:
        return render(request,'queries.html')

# @login_required
def SubmitProjectView(request):
    if request.method == 'POST':
        name = request.user.username
        hosted_link = request.POST.get('hosted_link')
        github_link = request.POST.get('github_link')
        video_link = request.POST.get('video_link')
        if name == "":
            messages.warning(request,'You need to SignIn First!')
            return redirect('submitproject')
        try:
            instance = SubmissionModel(hosted_link=hosted_link,github_link=github_link,explanation_link=video_link,student=name)
            instance.save()
            messages.success(request,'Project Submitted Successfully! We will be sending you the results soon.')
            return redirect('submitproject')
        except IntegrityError:
            messages.warning(request,'You Have Already Submitted Project Once!')    
            return redirect('submitproject')
    else:
        return render(request,'submitproject.html')
    

class otprequest(APIView):
    def post(self,request):
        # getting the data needed
        data = request.data
        serializer = OtprequestSerializer(data=data)
        if not serializer.is_valid():
            return Response({
                'status': False,
                'message' : 'Something went wrong'
            },status.HTTP_400_BAD_REQUEST)
        
        email = data['email']
        global otp
        otp= random.randint(1000,9999)

        # Email account credentials
        from_address = "acrossdevice01@gmail.com"
        password = "bapw oify vutv fuau"

        # send email to 
        to_address = email

        # Email content
        subject = "Verify Otp for Creating Account"
        body = f"your otp for email verification is {otp} ."

        msg = MIMEMultipart()
        msg['From'] = from_address
        msg['To'] = to_address
        msg['Subject'] = subject

        # Attach the body with the msg instance
        msg.attach(MIMEText(body, 'plain'))

        # Create server object with SSL option
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        
        server.login(from_address, password)
        server.sendmail(from_address, to_address, msg.as_string())
        server.quit()
        return Response({
            'status':True,
            'message':'Otp succesfully sent',
            'otp': f'{otp}'
        },status.HTTP_200_OK)




        