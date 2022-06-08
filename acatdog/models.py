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
    name = models.CharField(max_length=10 ,default="旺仔")
    cd = models.CharField(max_length=10)
    age = models.IntegerField(blank=True, null=True)
    photo = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=11)
    fur = models.CharField(max_length=11)
    sex = models.CharField(max_length=11)
    chara = models.CharField(max_length=11, blank=True, null=True)
    addr = models.CharField(max_length=11)
    is_adopt = models.CharField(max_length=11,default="否")
    jveyu = models.CharField(max_length=11, blank=True, null=True)
    vacc = models.CharField(max_length=11, blank=True, null=True)
    ill = models.CharField(max_length=11, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'animal_info'


class AssistInfo(models.Model):
    动物id = models.IntegerField(db_column='动物ID')
    救助日期 = models.DateTimeField()
    救助单编号 = models.AutoField(primary_key=True,default=1)
    用户名 = models.CharField(db_column='用户名',max_length=20,default="admin")  # Field name made lowercase.
    是否可被领养 = models.CharField(max_length=10)

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
