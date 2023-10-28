from django.db import models
from User.models import User

class Announcement(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=255)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    promoted = models.BooleanField(default=False)

class AnnouncementImages(models.Model):
    image_id = models.AutoField(primary_key=True)
    announcement_id = models.ForeignKey(Announcement, on_delete=models.CASCADE)
    image_data = models.ImageField(upload_to='images/')
    image_description = models.TextField()

class Review(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    announcement_id = models.ForeignKey(Announcement, on_delete=models.CASCADE)
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    review_id = models.ForeignKey(Review, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


