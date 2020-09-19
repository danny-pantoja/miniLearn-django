from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class InstructorContent(models.Model):
  # define fields
  # https://docs.djangoproject.com/en/3.0/ref/models/fields/
  instructor_content = models.CharField(max_length=100)
  content_availability = models.BooleanField()
  description = models.CharField(max_length=100)
  owner = models.ForeignKey(
      get_user_model(),
      on_delete=models.CASCADE
  )

  def __str__(self):
    # This must return a string
    return f"This content '{self.instructor_content}' is {self.description}. This content is {self.content_availability} available."

  def as_dict(self):
    """Returns dictionary version of InstructorContent models"""
    return {
        'id': self.id,
        'instructor_content': self.instructor_content,
        'content': self.content,
        'description': self.description
    }
