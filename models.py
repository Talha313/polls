from django.db import models


# Create your models here.
class Question(models.Model):
    Question_text = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')

    def _str_(self):
        return "%s" (self.Question_text)


class Choices(models.Model):
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0, null=True, blank=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def _str_(self):
        return self.choice_text
