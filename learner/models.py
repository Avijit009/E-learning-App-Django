from django.db import models
from account.models import LearnerProfile, InstructorProfile
# Create your models here.


class AskedQuestion(models.Model):
    learner = models.ForeignKey(LearnerProfile, on_delete=models.CASCADE)
    subject = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.subject
    
class AnswerQuestion(models.Model):
    instructor=models.ForeignKey(InstructorProfile,on_delete=models.CASCADE)
    question=models.ForeignKey(AskedQuestion,on_delete=models.CASCADE)
    answer=models.TextField()