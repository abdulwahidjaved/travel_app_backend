from django.db import models

class UserDetail(models.Model):
    name = models.CharField(max_length=50)
    select_country = models.CharField(max_length=50)
    select_destination_type = models.CharField(max_length=50)
    date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to="home/images", default="")

    def __str__(self):
        return self.name