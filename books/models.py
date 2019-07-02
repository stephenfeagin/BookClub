from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    subtitle = models.CharField(max_length=200)
    author = models.ManyToManyField("Author")
    description = models.TextField(max_length=1000)
    pub_year = models.PositiveSmallIntegerField("Publication Year")


class Author(models.Model):
    last_name = models.CharField(max_length=100, db_index=True)
    given_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    date_of_death = models.DateField()
