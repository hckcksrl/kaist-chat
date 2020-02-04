from django.db import models
from kaist.chat.entities.entity import MenuEntity


class DAY(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    day = models.CharField(null=True, max_length=255, default='')


class FCLT(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    time = models.CharField(null=True, max_length=255, default='')
    menu = models.TextField(null=True, default='')
    day = models.ForeignKey('DAY', on_delete=models.CASCADE)

    def to_entity(self) -> MenuEntity:
        return MenuEntity(
            id=self.id,
            time=self.time,
            menu=self.menu,
            day=self.day
        )


class WEST(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    time = models.CharField(null=True, max_length=255, default='')
    menu = models.TextField(null=True, default='')
    day = models.ForeignKey('DAY', on_delete=models.CASCADE)

    def to_entity(self) -> MenuEntity:
        return MenuEntity(
            id=self.id,
            time=self.time,
            menu=self.menu,
            day=self.day
        )


class EAST1(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    time = models.CharField(null=True, max_length=255, default='')
    menu = models.TextField(null=True, default='')
    day = models.ForeignKey('DAY', on_delete=models.CASCADE)

    def to_entity(self) -> MenuEntity:
        return MenuEntity(
            id=self.id,
            time=self.time,
            menu=self.menu,
            day=self.day
        )


class EAST2(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    time = models.CharField(null=True, max_length=255, default='')
    menu = models.TextField(null=True, default='')
    day = models.ForeignKey('DAY', on_delete=models.CASCADE)

    def to_entity(self) -> MenuEntity:
        return MenuEntity(
            id=self.id,
            time=self.time,
            menu=self.menu,
            day=self.day
        )


class EMP(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    time = models.CharField(null=True, max_length=255, default='')
    menu = models.TextField(null=True, default='')
    day = models.ForeignKey('DAY', on_delete=models.CASCADE)

    def to_entity(self) -> MenuEntity:
        return MenuEntity(
            id=self.id,
            time=self.time,
            menu=self.menu,
            day=self.day
        )


class ICC(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    time = models.CharField(null=True, max_length=255, default='')
    menu = models.TextField(null=True, default='')
    day = models.ForeignKey('DAY', on_delete=models.CASCADE)

    def to_entity(self) -> MenuEntity:
        return MenuEntity(
            id=self.id,
            time=self.time,
            menu=self.menu,
            day=self.day
        )


class HAWAM(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    time = models.CharField(null=True, max_length=255, default='')
    menu = models.TextField(null=True, default='')
    day = models.ForeignKey('DAY', on_delete=models.CASCADE)

    def to_entity(self) -> MenuEntity:
        return MenuEntity(
            id=self.id,
            time=self.time,
            menu=self.menu,
            day=self.day
        )
