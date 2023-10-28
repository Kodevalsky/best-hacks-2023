from django.contrib import admin
from Offer.models import Announcement, AnnouncementImages, Review, Comment
# Register your models here.

admin.site.register(Announcement)
admin.site.register(AnnouncementImages)
admin.site.register(Review)
admin.site.register(Comment)