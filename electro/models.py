from django.db import models

class CarCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Car(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(CarCategory, on_delete=models.CASCADE, related_name='cars')
    brand = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    image = models.ImageField(upload_to='cars_images/', blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.brand}, {self.year})"
