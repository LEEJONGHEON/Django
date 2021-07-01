from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .models import Post
from django.core.paginator import Paginator


def index(request):
    post_list = Post.objects
    list = Post.objects.all().order_by('-pub_date')
    paginator = Paginator(list, 2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'Blog/index.html', {'post_list': post_list, 'posts': posts})


# Create
def new(request):
    return render(request, 'Blog/new.html')


def create(request):
    post = Post()
    post.title = request.POST['title']
    post.content = request.POST['content']
    post.author = request.POST['author']
    post.image = request.FILES['image']

    post.file_title = request.POST['file_title']
    post.file = request.FILES['file']
    post.save()

    return redirect('/post/' + str(post.id))

# Read
def detail(request, post_id):
    post_detail = get_object_or_404(Post, pk=post_id)
    return render(request, 'Blog/detail.html', {'post': post_detail})

# Update
def updateForm(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    return render(request, 'Blog/updateForm.html', {'post': post})


def update(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.title = request.POST['title']
    post.content = request.POST['content']

    post.image = request.FILES['image']
    post.file_title = request.POST['file_title']
    post.file = request.FILES['file']

    post.save()
    return redirect('/post/')


# Delete
def delete(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    return redirect('/post/')

def result(request):
    query = request.GET['query']
    if query:
            posts = Post.objects.filter(title__contains=query)
    return render(request, 'Blog/result.html', {'posts': posts})