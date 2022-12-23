from django.db import models

class Cinemas(models.Model):
    id = models.AutoField(primary_key=True, max_length=100)
    title = models.TextField(120)
    director = models.TextField(20)
    description = models.TextField()
    pster_url = models.TextField()
    running_time = models.IntegerField()
    age_ratin = models.IntegerField()


    class Meta:
        db_table = 'cinema'

    def __str__(self):
        return f'{self.pk} {self.title} {self.director} {self.description} {self.pster_url} {self.running_time} {self.age_ratin} '