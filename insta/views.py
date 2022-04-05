from django.shortcuts import render, redirect, get_object_or_404
from . models import Image
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import CommentForm

# Create your views here.
# /@login_required(login_url='/accounts/login')
def home(request):
    images= Image.get_images().order_by('-date_posted')
    return render(request, 'index.html', {'images': images})

def welcome(request):
    return HttpResponse("Welcome to instagram")

def post_comment(request, id):
    image=get_object_or_404(Image, pk=id)

    if request.method=='POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            savecomment=form.save(commit=False)
            savecomment.post=image
            savecomment.user=request.user.profile
            savecomment.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form=CommentForm()
    params={
        'image': image,
        'form': form,
    }
    return render(request, 'comment.html', params)
