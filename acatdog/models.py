from django.contrib.auth.models import User
from django.db import models


class AdoptInfo(models.Model):
    用户id = models.IntegerField(db_column='用户ID')
    领养日期 = models.DateTimeField()
    动物id = models.IntegerField(db_column='动物ID') 
    领养单编号 = models.AutoField(primary_key=True)
    领养状态 = models.CharField(max_length=50)
    合照 = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'adopt_info'


class AnimalInfo(models.Model):
    动物id = models.AutoField(db_column='动物ID', primary_key=True)
    动物名 = models.CharField(max_length=10 ,default="旺仔")
    动物类别 = models.CharField(max_length=10)
    年龄 = models.IntegerField()
    照片 = models.TextField(blank=True, null=True)
    品种 = models.CharField(max_length=11)
    毛色 = models.CharField(max_length=11)
    性别 = models.CharField(max_length=11)
    性格 = models.CharField(max_length=11, blank=True, null=True)
    地址 = models.CharField(max_length=11)
    是否被领养 = models.CharField(max_length=11)
    绝育情况 = models.CharField(max_length=11, blank=True, null=True)
    疫苗情况 = models.CharField(max_length=11, blank=True, null=True)
    疾病情况 = models.CharField(max_length=11, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'animal_info'


class AssistInfo(models.Model):
    动物id = models.IntegerField(db_column='动物ID')
    救助日期 = models.DateTimeField()
    救助单编号 = models.AutoField(primary_key=True)
    用户id = models.IntegerField(db_column='用户ID')  # Field name made lowercase.
    是否可被领养 = models.CharField(max_length=2)

    class Meta:
        managed = True
        db_table = 'assist_info'


class ManagerInfo(models.Model):
    工号 = models.IntegerField(primary_key=True)
    性别 = models.CharField(max_length=2)
    电话 = models.IntegerField()
    密码 = models.CharField(max_length=10)
    在线时间 = models.IntegerField()
    年龄 = models.IntegerField()
    工龄 = models.IntegerField()
    投诉邮箱 = models.CharField(max_length=10)

    class Meta:
        managed = True
        db_table = 'manager_info'


class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    addr = models.CharField(max_length=50, blank=True, null=True)
    phonum = models.CharField(max_length=13, null=True)
    sex = models.CharField(max_length=2, default='男', null=True)
    job = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=50, null=True)
    photo = models.URLField(max_length=256, blank=True)
    age = models.DateTimeField(blank=True, null=True)
    crepoint = models.IntegerField(default='0')

    class Meta:
        managed = True
        db_table = 'user_info'

    def __str__(self):
        return str(self.user)
