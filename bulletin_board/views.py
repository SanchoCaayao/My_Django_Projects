# views.py
# For creating and displaying posts.

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm

# View to display all posts
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'bulletin_board/post_list.html', {'posts': posts})

# View to display a single post
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'bulletin_board/post_detail.html', {'post': post})

# View to create a new post
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'bulletin_board/post_edit.html', {'form': form})
