from django.db import models


class Subscribes(models.Model):
    subscribe_name = models.CharField(max_length=150, null=False)
    monthly_price = models.IntegerField(default=1, blank=True)

    def __str__(self):
        return f"Subscribe plan: {self.subscribe_name}.\tMonthly price: {self.monthly_price}."


class Activities(models.Model):
    name = models.CharField(max_length=50, null=False)
    starting_time = models.DateTimeField('activity starting time')

    def __str__(self):
        return f'{self.name} starts in: {self.starting_time}.'


class Customer(models.Model):
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    subscribe_plan = models.ForeignKey(Subscribes, on_delete=models.CASCADE)
    activities = models.ManyToManyField('Activities', related_name='customer')

    def activity_names(self):
        return ', '.join([a.name for a in self.activities.all()])
    activity_names.short_description = ' Activity name'

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.activity_names()} {self.subscribe_plan}"
