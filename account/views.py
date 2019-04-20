from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as login_
from django.http import HttpResponseRedirect


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText




#def register(request):
#	return render(request,'accounts/register.html')
 #Create your views here.

def sucess(request):
	return render(request,'successfull.html')

def register(request):
	if request.method == 'POST':
		u = request.POST['user']
		e = request.POST['email']
		p = request.POST['password']
		f = request.POST['first']
		l = request.POST['last']

		User.objects.create_user(username=u,email=e,password=p,first_name=f,last_name=l)

		s = smtplib.SMTP('smtp.gmail.com', 587)
		s.starttls()
		s.login("gamingzonedhruv@gmail.com", "yash12345@")
		message = "congratulation"
		msg = MIMEMultipart('alternative')

		text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.python.org"
		html = """\
		<html>
			<head></head>
			<body>
				<p>Hi!<br>
				How are you?<br>
				Here is the <a href="http://www.python.org">link</a> you wanted.
				</p>
			</body>
		</html>
		"""

		part1 = MIMEText(text, 'plain')
		part2 = MIMEText(html, 'html')

		msg.attach(part1)
		msg.attach(part2)
		s.sendmail("gamingzonedhruv@gmail.com", (e), msg.as_string())
		s.quit()
		
		return HttpResponseRedirect('/register/sucess')
	return render(request, 'accounts/register.html',{})
	

def login(request):
	if request.method =='POST':

		us=request.POST['user_']
		pas=request.POST['password']
		user = authenticate(request, username=us,password=pas)
		if user is not None:
			login_(request, user)
			return HttpResponse("successfull")			
			#return render(request, 'accounts/login.html',{})
		else:
			return HttpResponse("sorry")
	return render(request, 'accounts/login.html',{})
	return HttpResponse('login successful')




		
	
