from django.shortcuts import render, get_object_or_404,HttpResponse,HttpResponseRedirect
from blog.models import Post,comment
import datetime
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.db.models import Avg, Max, Min, Sum, Count



def home(request):
	
	blog=Post.objects.all()
	#com = comment.objects.get()
	#lis.append(com)
	latest_blog=Post.objects.all().order_by('-created_date')

	return render(request, 'home.html',{'blog':blog,'latest_blog':latest_blog})
	


def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	#post.view_count += 1
	#post.save()
	lis=[]
	commet=comment.objects.filter(com_name=pk)
	count= comment.objects.filter(com_name=pk).count()
	lis.append(count)
	if request.method == 'POST':
		com = request.POST['coment']
		p = Post.objects.get(pk=pk)

		if len(com)==0:

			return HttpResponseRedirect('/blog/{}'.format(pk))

		else:

			comment.objects.create(comments=com, com_name=p)

			return HttpResponseRedirect('/blog/{}'.format(pk))

	

	return render(request, 'post_detail.html', {'post': post,'commet':commet,'lis':lis})

def yash(request):
	posts =Post.objects.all()
	
	return render(request, 'post.html',{'posts':posts})

#def post_edit(request,pk):
#	post = get_object_or_404(Post, pk=pk)
#	if request.method == 'POST':
#		a=request.POST['head']
#		b=request.POST['content']
#
#		Post.save(name=a,content=b)
#
#	return render(request,'post_edit.html',{'post':post})



def new_form(request):

	if request.method == 'POST':
		h = request.POST['head']
		c = request.POST['content']
		i = request.FILES['pho']

		Post.objects.create(name=h, content=c, img=i)
	return render(request, 'new_form.html',{})
	

		


# Create your views here.
