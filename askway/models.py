from django.db import models
from django.contrib.auth.models import User

class Query(models.Model):
    question = models.CharField(max_length = 500)
    post_by = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.question


class Solution(models.Model):
    answer = models.CharField(max_length = 500)
    answer_of = models.ForeignKey(Query, on_delete=models.CASCADE)
    answer_by = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.answer