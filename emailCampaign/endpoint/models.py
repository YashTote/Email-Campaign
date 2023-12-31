from django.db import models
from django.utils import timezone
# Create your models here.


class Campaign(models.Model):
    title = models.CharField(max_length=50)
    subject = models.CharField(max_length=255)
    preview_text = models.TextField()
    article_url = models.URLField()
    html_content = models.TextField()
    plain_text_content = models.TextField()
    published_date = models.DateTimeField()
    def __str__(self):
        return self.title
class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.first_name
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.name
    
class CategoryRelationship(models.Model):
    subscriber = models.ForeignKey(Subscriber, on_delete=models.CASCADE)
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.subscriber.first_name} - {self.category.name} - {self.campaign.title}"
    
class DeliveryRecord(models.Model):
    email = models.EmailField()
    time_sent = models.DateTimeField()
    
    def save(self, *args, **kwargs):
        # Set the time_sent field to the current date and time if the record is being created
        if not self.pk:
            self.time_sent = timezone.now()
        super(DeliveryRecord, self).save(*args, **kwargs)
    def __str__(self):
        return self.email