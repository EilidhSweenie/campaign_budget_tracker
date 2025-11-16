from django.db import models

class Campaign(models.Model):
    STATUS_CHOICES = [
        ('IN_BUDGET', 'In Budget'),
        ('WARNING', 'Warning'),
        ('OUT_OF_BUDGET', 'Out of Budget'),
    ]
        
    name = models.CharField(max_length=50)
    budget = models.DecimalField(max_digits=1000, decimal_places=2)
    spend= models.DecimalField(max_digits=1000, decimal_places=2)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='IN_BUDGET',
    )

    def __str__(self):
        return self.name
