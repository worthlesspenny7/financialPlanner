from django.db import models

class User(models.Model):
    user_name = models.CharField(max_length=50)
    profile_create_date = models.DateTimeField('User Since')
    min_balance = models.DecimalField('Minimum Balance', max_digits=10, decimal_places=2)
    
class Goal(models.Model):
    user = models.ForeignKey(User)
    name_goal = models.CharField(max_length=50)
    cost_goal = models.DecimalField('Goal Cost', max_digits=10, decimal_places=2)
    date_goal = models.DateTimeField('Goal Date')
    start_goal = models.DateTimeField('Goal Start')