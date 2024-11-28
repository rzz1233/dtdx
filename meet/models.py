from django.db import models
from django.contrib.auth.hashers import make_password
import uuid
# Create your models here.


class Login(models.Model):
    user = models.CharField(max_length=100,unique=True)
    pwd = models.CharField(max_length=256)
    role = models.CharField(max_length=32)

    # def save(self, *args, **kwargs):
    #     # 如果密码是明文的，进行加密
    #     if not self.pwd.startswith('pbkdf2_sha256'):
    #         self.password = make_password(self.pwd)
    #     super(Login, self).save(*args, **kwargs)


class Dept(models.Model):
    name = models.CharField(max_length=32,unique=True)


class Users(models.Model):
    name = models.CharField(max_length=32)
    user = models.CharField(max_length=100,unique=True)
    pwd = models.CharField(max_length=256)
    dept = models.ForeignKey(Dept, on_delete=models.CASCADE)

class Meetinglist(models.Model):
    date = models.DateField()
    starttime = models.TimeField()
    endtime = models.TimeField()
    title = models.CharField(max_length=64)
    dept = models.ForeignKey(Dept, on_delete=models.CASCADE)
    outpeople = models.CharField(max_length=64)
    status = models.CharField(max_length=64)


class Attendee(models.Model):
    meetname = models.CharField(max_length=64)
    user = models.CharField(max_length=32)
    meetdate = models.DateField()
    check_time = models.TimeField(max_length=32)
    status = models.CharField(max_length=32)


# class qiandao(models.Model):
#     meeting = models.ForeignKey(Meetinglist, on_delete=models.CASCADE)
#     status = models.CharField(max_length=32)