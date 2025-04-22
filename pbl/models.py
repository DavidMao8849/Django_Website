from django.db import models

class Member(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos/')
    student_id = models.CharField(max_length=20)
    hobby = models.TextField()

    def __str__(self):
        return self.name

class Friend(models.Model):
    name = models.CharField(max_length=100)
    relation = models.CharField(max_length=50)
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='friends')

    def __str__(self):
        return f"{self.name} ({self.relation})"
