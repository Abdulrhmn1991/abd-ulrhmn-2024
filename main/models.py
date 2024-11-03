# main/models.py
from django.db import models

class DailyFlyer(models.Model):
    image = models.ImageField(upload_to='flyers/')
    description = models.TextField()

    def __str__(self):
        return f"Flyer {self.id}"

class Page(models.Model):
    AREA_CHOICES = (
        ('الباب', 'الباب'),
        ('جنديرس', 'جنديرس'),
    )
    area = models.CharField(max_length=50, choices=AREA_CHOICES)  # إزالة unique=True
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pages/')
    working_hours = models.CharField(max_length=100)
    description = models.TextField()
    whatsapp_number = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.title} ({self.area})"
