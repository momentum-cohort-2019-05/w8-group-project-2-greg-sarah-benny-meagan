from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# Create your models here.

class Question(models.Model):
    """Model representing a posted questions."""
    title = models.CharField(max_length=100, help_text='Enter a title for your question')
    body = models.TextField(max_length=1000, help_text='Enter details about your question')
    categories = models.ManyToManyField('Category')
    timestamp = models.DateField(auto_now_add=True)

    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='question_asker')

    def get_absolute_url(self):
        return reverse('questions', args=[str(self.pk)])

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        """String for representing the Model object."""
        return self.title

class Answer(models.Model):
    """Model representing an answer to a posted question."""
    body = models.TextField(max_length=1000, help_text='Enter your answer')
    question = models.ForeignKey(to=Question, on_delete=models.CASCADE)
    timestamp = models.DateField(auto_now_add=True)
    correct = models.BooleanField(default=False)

    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='answerer')

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        """String for representing the Model object."""
        return self.body

class Category(models.Model):
    category_name = models.CharField(max_length=200)

    def __str__(self):
        return self.category_name

    def get_absolute_url(self):
        return reverse('category', args=[str(self.pk)])