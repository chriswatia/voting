from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name


class County(models.Model):
    county_name = models.CharField(max_length=100)

    def __str__(self):
        return self.county_name


class Candidate(models.Model):
    county_name = models.ForeignKey(County, on_delete=models.CASCADE)
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE)
    candidate_name = models.CharField(max_length=100)
    nick_name = models.CharField(max_length=100)
    manifesto = models.TextField()

    def __str__(self):
        return self.candidate_name




