from django.db import models
from django.utils import timezone
from django.urls import reverse


class Post(models.Model):
    ''' Model definition for Post '''
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title

    def publish(self):
        ''' Publishes the post if it's not published yet '''
        self.published_date = timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approved_comment=True)

    def get_absolute_url(self):
        ''' Redirections to the new post page/list of comments '''
        return reverse("post_detail", kwargs={'pk': self.pk})


class Comment(models.Model):
    ''' Model definition for Comment '''
    post = models.ForeignKey(
        Post, related_name="comments", on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def __str__(self):
        return self.text

    def approve(self):
        ''' Approves a comment to appear on a post'''
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        ''' Redirections to the list of posts '''
        # return reverse("post_list", kwargs={"pk": self.pk})
        return reverse("post_list", kwargs={"pk": self.pk})
