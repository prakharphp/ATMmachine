from django.db import models

# Create your models here.


class UserAccount(models.Model):
    username = models.CharField(max_length=200, unique=True, null=False, blank=False)
    card_number = models.IntegerField(unique=True, null=False, blank=False)
    pin = models.IntegerField(null=False, blank=False)
    amount = models.IntegerField(default=0, null=False, blank=False)

    def __str__(self):
        """A string representation of the model."""
        return self.username
