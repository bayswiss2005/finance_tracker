from django import forms
from .models import Account, Category, Transaction


class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['name','balance', 'account_type']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name','type', 'icon']

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['amount', 'category', 'description', 'date', 'transaction_type', 'account']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }
        