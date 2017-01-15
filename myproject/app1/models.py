from django.db import models
import datetime
from django.core.validators import MaxValueValidator,MinValueValidator


class Users(models.Model):
    name = models.CharField(max_length=200, blank = False)
    DOB = models.DateField(blank = False)
    age = models.IntegerField(blank = False)
    address = models.CharField(max_length = 200, blank = False)
    mob_no = models.IntegerField(validators=[MaxValueValidator(9999999999),MinValueValidator(7000000000)],unique = True)
    email = models.CharField(max_length = 20 ,unique= True)
    passwrd = models.CharField(max_length = 20)

    def __str__(self):
        return '%d' % (self.age)

    

class Example(models.Model):
    DOB = models.DateField(max_length=200,blank = False)

    # def __str__(self):
    # 	return self.question_text