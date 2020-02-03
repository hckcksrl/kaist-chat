from django.db import models


class DAY(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    day = models.CharField(null=True, max_length=255, default='')


class FCLT(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    time = models.CharField(null=True, max_length=255, default='')
    menu = models.TextField(null=True, default='')
    day = models.ForeignKey('DAY', on_delete=models.CASCADE)


class WEST(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    time = models.CharField(null=True, max_length=255, default='')
    menu = models.TextField(null=True, default='')
    day = models.ForeignKey('DAY', on_delete=models.CASCADE)


class EAST1(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    time = models.CharField(null=True, max_length=255, default='')
    menu = models.TextField(null=True, default='')
    day = models.ForeignKey('DAY', on_delete=models.CASCADE)


class EAST2(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    time = models.CharField(null=True, max_length=255, default='')
    menu = models.TextField(null=True, default='')
    day = models.ForeignKey('DAY', on_delete=models.CASCADE)


class EMP(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    time = models.CharField(null=True, max_length=255, default='')
    menu = models.TextField(null=True, default='')
    day = models.ForeignKey('DAY', on_delete=models.CASCADE)


class ICC(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    time = models.CharField(null=True, max_length=255, default='')
    menu = models.TextField(null=True, default='')
    day = models.ForeignKey('DAY', on_delete=models.CASCADE)


class HAWAM(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    time = models.CharField(null=True, max_length=255, default='')
    menu = models.TextField(null=True, default='')
    day = models.ForeignKey('DAY', on_delete=models.CASCADE)
