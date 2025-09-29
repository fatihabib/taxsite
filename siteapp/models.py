from django.db import models

class Division(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='divisions/', blank=True, null=True)  # add this ✅


    def __str__(self):
        return self.name


class Department(models.Model):
    division = models.ForeignKey(Division, on_delete=models.CASCADE, related_name='departments')
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='divisions/', blank=True, null=True)


    def __str__(self):
        return f"{self.name} ({self.division.name})"


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='events/')
    date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title
