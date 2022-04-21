from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE)


    def __str__(self):
        return self.user.username


class DbaRoaster(models.Model):
    date = models.DateField(primary_key=True)
    day = models.CharField(max_length=25, blank=True, null=True)
    deepak = models.CharField(max_length=25, blank=True, null=True)
    nainesh = models.CharField(max_length=25, blank=True, null=True)
    akhilesh = models.CharField(max_length=25, blank=True, null=True)
    gaurav = models.CharField(max_length=25, blank=True, null=True)
    pranav = models.CharField(max_length=25, blank=True, null=True)
    prashant = models.CharField(max_length=25, blank=True, null=True)
    rohan = models.CharField(max_length=25, blank=True, null=True)
    shreeyash = models.CharField(max_length=25, blank=True, null=True)
    ankit = models.CharField(max_length=25, blank=True, null=True)
    ashvini = models.CharField(max_length=25, blank=True, null=True)
    kripa = models.CharField(max_length=25, blank=True, null=True)
    siddesh = models.CharField(max_length=25, blank=True, null=True)
    biki = models.CharField(max_length=25, blank=True, null=True)
    sumit = models.CharField(max_length=25, blank=True, null=True)
    mrunal = models.CharField(max_length=25, blank=True, null=True)
    pritam = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dba_roaster'
