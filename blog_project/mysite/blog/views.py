# Django Built-in
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


# User created
from blog.models import Post, Comment
from blog.forms import PostForm, CommentForm


class AboutView(TemplateView):
    template_name = "about.html"


class PostListView(ListView):
    model = Post

    def get_queryset(self):
        ''' Creates a SQL Query: SELECT * FROM post WHERE published_date <= timezone.now; '''
        return Post.objects.filter(published_date__lte=timezone.now()).order_by("-published_date")


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'  # Must be superuser to login
    redirect_field_name = 'blog/post_detail.html'  # Redirect to the post created
    form_class = PostForm  # Shows the Post form
    model = Post


class PostUpdateView(LoginRequiredMixin, UpdateView):
    login_url = "/login/"  # Must be superuser to login
    redirect_field_name = "blog/post_detail.html"  # Redirects to the post updated
    form_class = PostForm  # Shows the Post form
    model = Post


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy("post_list")


class DraftListView(LoginRequiredMixin, ListView):
    login_url = "/accounts/login/"  # Must be superuser to login
    # Redirects to the list of draft posts
    redirect_field_name = "blog/post_list.html"
    model = Post

    def get_queryset(self):
        ''' Creates a SQL Query: SELECT * FROM post WHERE published_date IS NULL;'''
        return Post.objects.filter(published_date__isnull=True).order_by("created_date")


''' Comment Views '''


@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect("post_detail", pk=pk)


@login_required
def add_comment_to_post(request, pk):
    ''' Comment Form Function View '''

    # Gets a post or throws error 404 if not found
    post = get_object_or_404(Post, pk=pk)

    # Comment form was filled properly
    if request.method == "POST":
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect("post_detail", pk=post.pk)

    # Comment form was not filled
    else:
        form = CommentForm()

    # Renders the actual page
    return render(request, "blog/comment_form.html", {"form": form})


@login_required
def comment_approve(request, pk):

    # Gets a comment or throws error 404 if not found
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()

    # Redirects to the post page of the comment
    return redirect("post_detail", pk=comment.post.pk)


@login_required
def comment_remove(request, pk):
    # Gets a comment or throws error 404 if not found
    comment = get_object_or_404(Comment, pk=pk)

    # Stores the comments post pk
    post_pk = comment.post.pk

    # Deletes comment from the database
    comment.delete()

    return redirect("post_detail", pk=post_pk)
