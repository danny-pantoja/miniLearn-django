from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Video(models.Model):
  # define fields
  # https://docs.djangoproject.com/en/3.0/ref/models/fields/
  title = models.CharField(max_length=100)
  description = models.CharField(max_length=100)
  owner = models.ForeignKey(
      get_user_model(),
      on_delete=models.CASCADE
  )

  def __str__(self):
    # This must return a string
    return f"Title '{self.title}' Description {self.description}."

  def as_dict(self):
    """Returns dictionary version of Video models"""
    return {
        'id': self.id,
        'title': self.title,
        'description': self.description
    }
