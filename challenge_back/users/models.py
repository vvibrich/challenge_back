from django.db import models

class User(models.Model):

    class Meta:

        db_table = 'users'

    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(blank=False)
    password = models.CharField(max_length=100, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
            return  self.name
