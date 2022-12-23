from django.db import models

# Create your models here.
class Showtimes(models.Model):
    id = models.AutoField(primary_key=True, max_length=30)
    start_time = models.DateTimeField(auto_now=True)
    end_time = models.DateTimeField(auto_now=True)

class ShowtimeModel(models.Model):
    pass


    class Meta:
        db_table = 'showtimes'

    def __str__(self):
        return f'{self.pk} {self.username} {self.password} {self.created_at} {self.rank} {self.point} '