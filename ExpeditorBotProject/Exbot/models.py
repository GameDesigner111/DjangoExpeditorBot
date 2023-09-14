from django.db import models
from datetime import datetime as dt


# Create your models here.
class User(models.Model):
    roles = (
        ("DR", "ВОДИТЕЛЬ"),
        ("LT", "ЛОГИСТ")
        )

    statuses = (
        ("SLEEP", "СПИТ"),
        ("AWAKE", "ПРОСНУЛСЯ"),
        ("ONROAD", "В ДОРОГЕ"),
        ("ARRIVED", "ПРИБЫЛ"),
        )
    
    first_name = models.CharField("Имя", max_length=20, blank=False)
    last_name = models.CharField("Фамилия", max_length=30, blank=False)
    tg_id = models.IntegerField("Телеграм ID", blank=False)
    role = models.CharField("Роль", choices=roles, max_length=2, blank=False, default="DR")
    status = models.CharField("Статус", max_length=20, blank=False, null=False, default="SLEEP", choices=statuses)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.role}"  


class Point(models.Model):
    address = models.CharField("Адрес точки", max_length=50, blank=False, null=False)
    driver = models.ForeignKey(User, related_name="points", on_delete=models.CASCADE)
    arrived_at = models.DateTimeField("Прибыл", blank=True, null=True)
    left_at = models.DateTimeField("Уехал", blank=True, null=True)

    def __str__(self):
        return f"{self.address}"  
