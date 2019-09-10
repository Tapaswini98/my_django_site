from django.shortcuts import render
from django.utils import  timezone
from  .models import Post
from  django.shortcuts import get_object_or_404



# Create your views here.
def post_list(request):
    posts= Post.objects.all().order_by('-published_date')
    stuff_for_frontend={'posts':posts}
    return render(request,'blog/post_list.html',stuff_for_frontend)

def post_detail(request,pk):
    post=get_object_or_404(Post,pk=pk)
    stuff_for_frontend= {'post':post}

    return render(request,'blog/post_detail.html',stuff_for_frontend)

