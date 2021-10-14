from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm
from django.contrib.auth.decorators import login_required
from store.utils import *


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been succesfully created!')
            return redirect('login')
    else:
        form = UserRegisterForm()

    context = {'form': form}
    return render(request, 'users/register.html', context)


@login_required # impide acceder si no se está autenticado
def account(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('account')
    else:
        form = UserUpdateForm(instance=request.user)

    context = {'form': form}
    return render(request, 'users/account.html', context)
