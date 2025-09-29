from django.db import models
from h11 import Response

# Create your models here.

class Survey(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
class Question(models.Model):
    QUESTTION_TYPES = [
        ('text', 'Текстовый ответ'),
        ('single', 'Один вариант'),
        ('multiple', 'Несколько вариантов'),
    ]

    survey = models.ForeignKey(Survey, on_delete=models.CASCADE,
                               related_name='questions')
    text = models.TextField()
    question_type = models.CharField(max_length=10, choices=QUESTTION_TYPES)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.text
    

class Choise(models.Model):
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    user_ip = models.GenericIPAddressField(null=True, blank=True)

class Answer(models.Model):
    response = models.ForeignKey(Response, on_delete=models.CASCADE)
    text_answer = models.TextField(blank=True)
    choices = models.ManyToManyField(Choise, blank=True)

    def __str__(self):
        return f'Ответ на вопрос: {self.question.text}'