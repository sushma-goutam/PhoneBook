from django.db import models


class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)

    class Meta:
        db_table = "Contact"

    def __str__(self):
        return self.first_name + ' ' + self.last_name
