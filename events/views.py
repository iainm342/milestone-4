from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Post
from django.contrib import messages

from .forms import PostForm


def post(request):

    posts = Post.objects.all()

    template = "events/events.html"
    context = {
        "posts": posts,
    }

    return render(request, template, context)


def post_detail(request, slug):

    post = get_object_or_404(Post, slug=slug)

    template = "events/event_detail.html"
    context = {
        "post": post,
    }

    return render(request, template, context)


def add_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            messages.success(request, "SUCCESS")
            return redirect(reverse("post_detail", args=[post.slug]))
        else:
            messages.error(request, "FAILED")
    else:
        form = PostForm()

    template = "events/add_event.html"
    context = {
        "form": form,
    }

    return render(request, template, context)
