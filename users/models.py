from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password_hash = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15, unique=True)

    class Meta:
        db_table = 'Users'


    def __str__(self):
        return self.name