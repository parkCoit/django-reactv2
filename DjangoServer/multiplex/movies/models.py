from django.db import models

class Movies(models.Model):
    id = models.AutoField(int, primary_key=True, max_length=100)
    title = models.TextField(30)
    image_url = models.TextField()
    address = models.TextField(50)
    detail_address = models.TextField(30)


    class Meta:
        db_table = 'multiplex'

    def __str__(self):
        return f'{self.pk} {self.title} {self.image_url} {self.address} {self.detail_address}  '