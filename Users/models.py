from django.db import models
from django.core.validators import MaxValueValidator

Roles =(
    ("Regular", "Regular- Can't delete members"),
    ("Admin", "Admin- Can delete members"),
)
# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_num = models.IntegerField(validators=[MaxValueValidator(9999999999)])
    email = models.CharField(max_length=50)
    role = models.CharField(max_length=50, choices=Roles)