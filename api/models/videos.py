from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Videos(models.Model):
  # define fields
  # https://docs.djangoproject.com/en/3.0/ref/models/fields/
  name = models.CharField(max_length=100)
  field_name = models.URLField(max_length=200)
  description = models.CharField(max_length=100)
  owner = models.ForeignKey(
      get_user_model(),
      on_delete=models.CASCADE
  )

  def __str__(self):
    # This must return a string
    return f"The video named '{self.name}' is from {self.field_name}. It is {self.description}."

  def as_dict(self):
    """Returns dictionary version of Videos models"""
    return {
        'id': self.id,
        'name': self.name,
        'field_name': self.field_name,
        'description': self.description
    }
