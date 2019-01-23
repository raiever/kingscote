from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField

NATION_CHOICES = (
    ('KOR', 'South Korea'),
    ('GER', 'Germany'),
)

LEVEL_CHOICES = (
    ('ADV', 'Advanced'),
    ('UI', 'Upper Intermediate'),
    ('I', 'Intermediate'),
    ('PI', 'Pre Intermediate'),
)


class Student(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200, blank=True)
    mobile = models.CharField(max_length=30, blank=True)
    email = models.EmailField()
    age = models.IntegerField(blank=True)
    # nationality = models.CharField(max_length=20, choices=NATION_CHOICES)
    country = CountryField(blank_label='(Select Country)', blank=True)
    en_level = models.CharField('English Level', max_length=40, choices=LEVEL_CHOICES)
    attached_files = models.FileField(upload_to='uploads/', blank=True)
    submitted = models.DateField(auto_now_add=True)
    username = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id) 