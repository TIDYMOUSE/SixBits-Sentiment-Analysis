from django.db import models

# Create your models here.


class Post(models.Model):
    username = models.CharField(
        max_length=50, blank=False, help_text="Enter the username from twitter/fb")
    post_code = models.TextField(
        max_length=1000, blank=False, help_text="Enter the embed url")
    post_text = models.TextField(
        max_length=200, blank=False, help_text="Enter the text portion of the post")
    like_count = models.IntegerField(blank=False)
    post_trend = models.CharField(max_length=50)

    class Meta:
        ordering = ['-like_count']

    def __str__(self) -> str:
        return self.username + " : " + self.post_trend + " : " + self.post_text[:70]
