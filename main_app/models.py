from django.db import models

# A tuple of 2-tuples
MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)

# Create your models here.
class Dog(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()

    def __str__(self):
        return self.name

# Add new Feeding model below Dog model
class Feeding(models.Model):
    date = models.DateField()
    meal = models.CharField(
        max_length=1,
        # Add the 'choices' field option
        choices=MEALS,
        # Set the default value for meal to be 'B'
        default=MEALS[0][0]
    )
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)
  
    def __str__(self):
        return f"{self.get_meal_display()} on {self.date}"
