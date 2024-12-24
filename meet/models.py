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


class qiandao(models.Model):
    meeting = models.ForeignKey(Meetinglist, on_delete=models.CASCADE)
    status = models.CharField(max_length=32)

class MechanicsOnlineDayTest(models.Model):
    id = models.BigAutoField(primary_key=True)
    county = models.TextField(null=True, blank=True)
    online_num = models.BigIntegerField(null=True, blank=True)
    zongliangtongbi = models.FloatField(null=True, blank=True)
    zonglianghuanbi = models.FloatField(null=True, blank=True)
    pingjungongshi = models.FloatField(null=True, blank=True)
    gongshitongbi = models.FloatField(null=True, blank=True)
    gongshihuanbi = models.FloatField(null=True, blank=True)
    kaigonglv = models.FloatField(null=True, blank=True)
    kaigonglvtongbi = models.FloatField(null=True, blank=True)
    kaigonglvhuanbi = models.FloatField(null=True, blank=True)
    gongzuoyebili = models.FloatField(null=True, blank=True)
    kaigongshu = models.BigIntegerField(null=True, blank=True)
    zonggongshi = models.FloatField(null=True, blank=True)
    gaogongzuoyeshu = models.BigIntegerField(null=True, blank=True)  # gaogongzuoyeshu 字段
    datetime = models.DateTimeField(null=True, blank=True)
    update_time = models.TextField(null=True, blank=True)  # update_time 字段
    county_id = models.BigIntegerField(null=True, blank=True)  # county_id 字段

    class Meta:
        managed = False
        db_table = 't_mechanics_online_day_test'  # 表名
        unique_together = ('datetime', 'county_id')  # 设置唯一约束