from django.db import models

# Create your models here.
class StudentInfo(models.Model):
    roll_no = models.IntegerField(primary_key= True)
    name = models.CharField(max_length= 255)
    classdetail = models.CharField(max_length= 10)
    school = models.CharField(max_length=150)
    mobile = models.CharField(max_length= 15)
    address = models.CharField(max_length= 255)

    def __str__(self):
        return str(self.roll_no)

class StudentAcademic(models.Model):
    student = models.ForeignKey(StudentInfo,related_name='studentAcademic',on_delete= models.CASCADE)
    maths = models.IntegerField()
    physics = models.IntegerField()
    chemistry = models.IntegerField()
    biology = models.IntegerField()
    english = models.IntegerField()