from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Post
from django.contrib import messages


def post(request):

    posts = Post.objects.all()

    template = "events/events.html"
    context = {
        "posts": posts,
    }

    return render(request, template, context)


def post_detail(request, slug):

    post = get_object_or_404(Post, slug=slug)

    template = "events/post_detail.html"
    context = {
        "post": post,
    }

    return render(request, template, context)
