from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm, UpdateForm

def index(request):
    # If the method is POST
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        # If the form is valid
        if form.is_valid():
            # Yes, Save
            form.save()

            # Redirect to Home
            return HttpResponseRedirect('/')

        else:
            # No, Show Error
                return HttpResponseRedirect(form.error.as_json())



    # Get all posts, limit = 20
    posts = Post.objects.all().order_by('-created_at')[:100]

    # Show
    return render(request, 'posts.html',
                    {'posts': posts})

def delete(request, post_id):
    # Find post
    post = Post.objects.get(id = post_id)
    post.delete()
    return HttpResponseRedirect('/')

def edit(request, post_id):
    post = Post.objects.get(id = post_id)
    form = UpdateForm(instance=post)

    if request.method == 'POST':
        form = UpdateForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            print(form.error)

    
    return render(request,'edit.html',{'form': form})

   
def like(request, post_id):
    post = Post.objects.get(id = post_id)
    new_like = post.like_count + 1
    post.like_count = new_like
    post.save()
    return HttpResponseRedirect('/')
    




