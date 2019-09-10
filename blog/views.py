from django.shortcuts import render
from django.utils import  timezone
from  .models import Post



# Create your views here.
def post_list(request):
    posts= Post.objects.all().order_by('-published_date')
    stuff_for_frontend={'posts':posts}
    return render(request,'blog/post_list.html',stuff_for_frontend)
