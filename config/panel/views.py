from .models import MentorModel, MarksModel
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from capstone.models import CapstoneModel, SubmissionModel, QueryModel
import json
from django.core.serializers import serialize
from .serializers import MarksModelSerializers
import random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


# Create your views here.
class MentorLoginAPIView(APIView):
    def post(self, request):
        data = request.data
        username = data["username"]
        password = data["password"]
        try:
            instance = MentorModel.objects.get(name=username)
            if instance.password == password:
                return Response(
                    {"LoggedIn": True, "message": "Login Successful!"},
                    status.HTTP_200_OK,
                )
            else:
                return Response(
                    {"LoggedIn": False, "message": "Login Failed!, Check Password!"},
                    status.HTTP_401_UNAUTHORIZED,
                )
        except MentorModel.DoesNotExist:
            return Response(
                {"LoggedIn": False, "message": "User Not Found, Contact Admin"}
            )


class GetStudentDetails(APIView):
    def post(self, request):
        data = request.data
        MentorName = data["MentorName"]
        instance = CapstoneModel.objects.filter(mentor=MentorName)
        data = {}
        for element in instance:
            name = element.student
            user = User.objects.get(username=name)
            email = user.email
            if SubmissionModel.objects.filter(student=name).exists():
                isSubmitted = True
            else:
                isSubmitted = False
            subdata = {"email": email, "isSubmitted": isSubmitted, "username": name}
            data[name] = subdata

        return Response(
            {"data": data, "message": "Fetch Successful"}, status.HTTP_200_OK
        )


class GetUserData(APIView):
    def post(self, request):
        data = request.data
        student = data["student"]
        UserInstance = User.objects.get(username=student)
        email = UserInstance.email
        CapstoneInstance = CapstoneModel.objects.get(student=student)
        figma = CapstoneInstance.figma_link
        mentor = CapstoneInstance.mentor
        try:
            QueryInstance = QueryModel.objects.filter(student=student)
            query_json = serialize("json", QueryInstance)
            query_data = json.loads(query_json)  # Convert JSON string to Python objects
        except QueryModel.DoesNotExist:
            query_data = {}
        SubmissionInstance = SubmissionModel.objects.get(student=student)
        hosted_link = SubmissionInstance.hosted_link
        github_link = SubmissionInstance.github_link
        explanation_link = SubmissionInstance.explanation_link
        try:
            MarksInstance = MarksModel.objects.filter(name=student)
            marks_json = serialize("json", MarksInstance)
            marks_data = json.loads(marks_json)
        except MarksModel.DoesNotExist:
            marks_data = {}
        return Response(
            {
                "username": student,
                "email": email,
                "figma": figma,
                "mentor": mentor,
                "query": query_data,
                "hosted-link": hosted_link,
                "github-link": github_link,
                "explanation-link": explanation_link,
                "marks": marks_data,
            },
            status.HTTP_200_OK,
        )

def send_result_email(
    student,
    email,
    html_structure,
    css_design,
    responsiveness,
    functional_design,
    debugging,
):
    global otp
    otp = random.randint(1000, 9999)

    # Email account credentials
    from_address = "acrossdevice01@gmail.com"
    password = "bapw oify vutv fuau"

    # send email to
    to_address = email

    # Email content
    subject = "Marks For Capstone"
    body = f"""Dear {student},
Following are your marks for capstone project
HTML structure = {html_structure},
CSS Design = {css_design},
Responsiveness = {responsiveness},
Funtional Design = {functional_design}
Debugging = {debugging}

regards 
NST Team
        """

    msg = MIMEMultipart()
    msg["From"] = from_address
    msg["To"] = to_address
    msg["Subject"] = subject

    # Attach the body with the msg instance
    msg.attach(MIMEText(body, "plain"))

    # Create server object with SSL option
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    server.login(from_address, password)
    server.sendmail(from_address, to_address, msg.as_string())
    server.quit()


class SetMarksView(APIView):
    def post(self, request):
        data = request.data
        serializer = MarksModelSerializers(data=data)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            student = validated_data["name"]
            email = validated_data["email"]
            html_structure = validated_data["html_structure"]
            css_design = validated_data["css_design"]
            responsiveness = validated_data["responsiveness"]
            functional_design = validated_data["functional_design"]
            debugging = validated_data["debugging"]
            serializer.save()
            send_result_email(
                student,
                email,
                html_structure,
                css_design,
                responsiveness,
                functional_design,
                debugging,
            )
            return Response(
                {
                    "status": 200,
                    "message": "Marks Updated And Email Sent Successfully!",
                },
                status.HTTP_200_OK,
            )
        else:
            return Response(
                {
                    "status": 400,
                    "message": "Invalid Value Entered",
                    "error": serializer.errors,
                },
                status.HTTP_400_BAD_REQUEST,
            )
        

def send_query_response(email,answer):
    # Email account credentials
    from_address = "acrossdevice01@gmail.com"
    password = "bapw oify vutv fuau"

    # send email to
    to_address = email

    # Email content
    subject = "Marks For Capstone"
    body = answer

    msg = MIMEMultipart()
    msg["From"] = from_address
    msg["To"] = to_address
    msg["Subject"] = subject

    # Attach the body with the msg instance
    msg.attach(MIMEText(body, "plain"))

    # Create server object with SSL option
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    server.login(from_address, password)
    server.sendmail(from_address, to_address, msg.as_string())
    server.quit()



class QueryHandlingView(APIView):
    def post(self,request):
        data = request.data
        id = data['id']
        answer = data['answer']
        instance = QueryModel.objects.get(id=id)
        instance.answer = answer
        instance.is_answered = True
        userName = instance.student
        user = User.objects.get(username=userName)
        email = user.email
        send_query_response(email,answer)
        return Response({
            'message':'Query status updated and email is sent'
        },status.HTTP_200_OK)

        
    def get(self,request):
        data = request.data
        mentor = data['mentor']
        try:
            QueryInstance = QueryModel.objects.filter(mentor = mentor)
            query_json = serialize("json", QueryInstance)
            query_data = json.loads(query_json)  # Convert JSON string to Python objects
        except QueryModel.DoesNotExist:
            query_data = {}
        return Response({
            'status': 200,
            'data':query_data
        },status.HTTP_200_OK)

        
