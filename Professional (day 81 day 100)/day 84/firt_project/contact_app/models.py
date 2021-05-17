from django.db import models

# Create your models here.
class ContactForm(models.Model):
    user = models.CharField(max_length=25)
    email = models.EmailField()
    comment = models.TextField()

    def __str__(self):
        return self.user