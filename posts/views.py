from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from .models import ItemPost, Comment
from .forms import ItemPostForm, CommentForm


def home(request):
    posts = ItemPost.objects.filter(is_resolved=False)
    search_text = request.GET.get("search", "")
    post_type = request.GET.get("type", "")
    category = request.GET.get("category", "")
    if search_text:
        posts = posts.filter(Q(item_name__icontains=search_text) | Q(location__icontains=search_text) | Q(description__icontains=search_text))
    if post_type in ["Lost", "Found"]:
        posts = posts.filter(post_type=post_type)
    if category in dict(ItemPost.CATEGORY_CHOICES):
        posts = posts.filter(category=category)
    return render(request, "posts/home.html", {
        "posts": posts, "search_text": search_text, "post_type": post_type,
        "category": category, "categories": ItemPost.CATEGORY_CHOICES,
    })


@login_required
def dashboard(request):
    posts = ItemPost.objects.filter(posted_by=request.user)
    return render(request, "posts/dashboard.html", {"posts": posts})


@login_required
def add_post(request):
    if request.method == "POST":
        form = ItemPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.posted_by = request.user
            post.save()
            messages.success(request, "Your post was added.")
            return redirect("dashboard")
    else:
        form = ItemPostForm()
    return render(request, "posts/add_post.html", {"form": form})


@login_required
def edit_post(request, post_id):
    post = get_object_or_404(ItemPost, id=post_id, posted_by=request.user)
    if request.method == "POST":
        form = ItemPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "Your post was updated.")
            return redirect("dashboard")
    else:
        form = ItemPostForm(instance=post)
    return render(request, "posts/edit_post.html", {"form": form, "post": post})


@login_required
def delete_post(request, post_id):
    post = get_object_or_404(ItemPost, id=post_id, posted_by=request.user)
    if request.method == "POST":
        post.delete()
        messages.success(request, "Your post was deleted.")
        return redirect("dashboard")
    return render(request, "posts/delete_post.html", {"post": post})


@login_required
def resolve_post(request, post_id):
    post = get_object_or_404(ItemPost, id=post_id, posted_by=request.user)
    if request.method == "POST":
        post.is_resolved = not post.is_resolved
        post.save()
        messages.success(request, "Post status updated.")
    return redirect("dashboard")


def post_detail(request, post_id):
    post = get_object_or_404(ItemPost, id=post_id)
    comments = post.comments.select_related("user").all()
    if request.method == "POST":
        if not request.user.is_authenticated:
            return redirect("login")
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            messages.success(request, "Your message was posted.")
            return redirect("post_detail", post_id=post.id)
    else:
        form = CommentForm()
    return render(request, "posts/post_detail.html", {"post": post, "comments": comments, "form": form})


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})
