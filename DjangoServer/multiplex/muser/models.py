from django.db import models

class Buser(models.Model):
    id = models.CharField(primary_key=True, max_length=30)
    email = models.TextField(120)
    nickname = models.TextField(20)
    password = models.TextField(255)
    age = models.IntegerField()

    class Meta:
        db_table = "muser"

    def __str__(self):
        return f'{self.pk} {self.email} {self.nickname} {self.password} {self.age} '