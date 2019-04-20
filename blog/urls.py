from django.urls import path
from blog.views import post_detail, yash,home,new_form
from blog import views



urlpatterns = [
    #path('',post_list, name='post_list'),
    path('',views.home, name='home'),
    #path('blog/',yash, name='yash'),
    path('<int:pk>/', views.post_detail, name='post_detail'),
    path('blog/new_blog/',new_form, name='new_form'),
    #path('blog/edit/<int:pk>/',post_edit,name='post_edit')

]
