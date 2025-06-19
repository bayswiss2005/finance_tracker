from django.shortcuts import render, redirect
from .forms import AccountForm, CategoryForm,TransactionForm
from django.contrib.auth.decorators import login_required
from  .models import Account, Category , Transaction
from django.contrib.auth.forms import UserCreationForm
from datetime import date



def register(request): 
    if request.method == 'POST': 
        form = UserCreationForm(request.POST) 
        if form.is_valid(): 
            form.save() 
            return redirect('login')
    else: 
        form = UserCreationForm() 
    return render(request, 'finance_app/register.html', {'form': form})


@login_required
def dashboard(request):
    accounts = Account.objects.filter(user=request.user)
    transactions = Transaction.objects.filter(account__user=request.user).order_by('-date')

    total_income = sum(t.amount for t in transactions if t.transaction_type == 'income')
    total_expense = sum(t.amount for t in transactions if t.transaction_type == 'expense')
    balance = total_income - total_expense

    context = {
        'transactions': transactions,
        'total_income': total_income,
        'total_expense': total_expense,
        'balance': balance
    }
    return render(request, 'finance_app/dashboard.html', context)


@login_required
def add_account(request):
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            account = form.save(commit=False)
            account.user = request.user
            account.save()
            return redirect('dashboard')
    else:
        form = AccountForm()
    return render(request, 'finance_app/add_account.html', {'form': form })

@login_required
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = CategoryForm()
    return render(request, 'finance_app/add_category.html', {'form': form})


@login_required
def add_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user
            transaction.save()
            return redirect('dashboard')
    else:
        form = TransactionForm()
    return render(request, 'finance_app/add_transaction.html',{'form': form})


# Create your views here.
