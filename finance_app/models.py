from django.db import models
from django.contrib.auth.models import User
from datetime import date



class Category(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=10, choices=[('expense', 'Expense'), ('income', 'Income')])
    icon = models.CharField(max_length=50, blank=True)  # For frontend display
    
    def __str__(self):
        return self.name

class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    account_type = models.CharField(max_length=20, choices=[
        ('cash', 'Cash'), 
        ('bank', 'Bank Account'),
        ('credit', 'Credit Card'),
        ('investment', 'Investment')
    ])
    
    def __str__(self):
        return f"{self.name} ({self.account_type})"

class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    description = models.CharField(max_length=200)
    date = models.DateField(default=date.today)
    transaction_type = models.CharField(max_length=10, choices=[('expense', 'Expense'), ('income', 'Income')])
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.transaction_type}: {self.amount} on {self.date}"

class Budget(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    monthly_limit = models.DecimalField(max_digits=10, decimal_places=2)
    year = models.IntegerField()
    month = models.IntegerField()
    
    class Meta:
        unique_together = ('user', 'category', 'year', 'month')
    
    def __str__(self):
        return f"Budget for {self.category.name}: {self.monthly_limit}"

class FinancialGoal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    target_amount = models.DecimalField(max_digits=10, decimal_places=2)
    current_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    target_date = models.DateField()
    created_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    def progress_percentage(self):
        return (self.current_amount / self.target_amount) * 100
