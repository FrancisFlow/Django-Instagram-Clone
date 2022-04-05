from django.shortcuts import render, redirect, get_object_or_404
from . models import Image
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import CommentForm, UpdateUserForm, UpdateUserProfileForm, NewProfileForm

# Create your views here.
@login_required(login_url='/accounts/login')
def home(request):
    images= Image.get_images().order_by('-date_posted')
    current_user= request.user
    return render(request, 'index.html', {'images': images, 'current_user': current_user})

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

def new_profile(request):
    current_user=request.user
    if request.method=='POST':
        form=NewProfileForm(request.POST, request.FILES)
        if form.is_valid():
            post=form.save(commit=False)
            post.user=current_user
            # post.save()
            return redirect('profile')
    else:
        form=NewProfileForm()
    return render(request, 'new_profile.html', {'form': form})



def profile(request, profile_id):
    images=request.user.profile.posts.all()
    if request.method=='POST':
        user_form=UpdateUserForm(request.POST, instance=request.user)
        prof_form=UpdateUserProfileForm(request.POST, request.FILES, instance=request.user)
        if user_form.is_valid() and prof_form.is_valid():
            user_form.save()
            prof_form.save()
            return HttpResponseRedirect(request.path_info)
    else:
        user_form=UpdateUserForm(instance=request.user)
        prof_form=UpdateUserProfileForm(instance=request.user.profile)
    params={
        'images': images,
        'user_form': user_form,
        'prof_form': prof_form,
    }
    return render(request, 'profile.html', params)


