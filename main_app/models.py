from django.db import models
from django.urls import reverse

# Create your models here.
class Finch(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()

def get_absolute_url(self):
    
    return reverse('detail', kwargs={'finch_id': self.id})

# Field Choices
MEALS = ( # This is an example of a constant
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner'),
)

class Feeding(models.Model):
    date = models.DateField()
    meal = models.CharField(
        max_length=1, # we set up a field choice!
        choices = MEALS, # dropdown, the value of the dropdown will be 'b' while the text that the human sees will be breakfast, lunch, dinner
        default = MEALS[0][0] # 'B'
        )

# Create the cat_id FK (foreign key)
# on_delete is saying if we delete a cat, delete all of the feedings the finch has, so no feedings exist without a finch
finch = models.ForeignKey(Finch, on_delete=models.CASCADE)

def __str__(self):
    return f"{self.get_meal_display()} on {self.date}"

class Meta:
		ordering = ['-date']