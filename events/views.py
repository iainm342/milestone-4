from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Post
from django.contrib import messages

from .forms import PostForm


def post(request):
    """A view to show all event posts"""
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
    """A view to allow the site owner to add an event post"""
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


def edit_post(request, slug):
    """A view to delete an event post"""
    post = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully updated event")
            return redirect(reverse("post_detail", args=[post.slug]))
        else:
            messages.error(request, "Failed to update the event.")
    else:
        form = PostForm(instance=post)
        messages.info(request, f"You are editing {post.title}")

    template = "events/edit_event.html"
    context = {
        "form": form,
        "post": post,
    }

    return render(request, template, context)


def delete_post(request, slug):
    """Delete an event"""

    post = get_object_or_404(Post, slug=slug)
    post.delete()
    messages.success(request, "Event deleted!")
    return redirect(reverse("events"))
