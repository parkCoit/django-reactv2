from django.db import models

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True, max_length=30)
    username = models.TextField(100)
    password = models.TextField(255)
    created_at = models.DateTimeField(auto_now=True)

    rank = models.IntegerField()
    point = models.IntegerField()


    class Meta:
        db_table = 'user'

    def __str__(self):
        return f'{self.pk} {self.username} {self.password} {self.created_at} {self.rank} {self.point} '