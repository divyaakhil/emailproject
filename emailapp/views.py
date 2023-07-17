from email import message
from django.shortcuts import render,redirect
from emailapp.models import email
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def add(request):
    return render(request,"add.html")

def mail(request): 
    if request.method=="POST":
        uname=request.POST['Username']
        paswrd=request.POST['Password']
        mail=request.POST['Email']
        stu=email(Username=uname,Password=paswrd,Email=mail)
        stu.save()
        subject="Application Received"
        message=f"Your Username is {uname} and Password is {paswrd}"
        recipient=request.POST['Email']
        send_mail(subject,message,settings.EMAIL_HOST_USER,[recipient])
        return redirect('/')
    return render(request,"add.html")
    
