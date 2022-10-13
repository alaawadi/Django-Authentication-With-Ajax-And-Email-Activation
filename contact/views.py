from django.shortcuts import render
# from .models import Info
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.





def contact(email,message,subject):
    mail = 'alaawadi98@gmail.com'
    send_mail(
        subject,
        message,
        email,
        
        [mail],
        
    )



def send_message(request):
    # myinfo = Info.objects.first()

    if request.method == 'POST':
        subject = request.POST['subject']
        email = request.POST['email']
        message = request.POST['message']

        contact(
            subject,
            message,
            email,
            
            
        )

    return render(request,'contact/contact.html')



