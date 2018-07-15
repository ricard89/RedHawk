from django.shortcuts import render
from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from accounts.forms import RegisterForm


# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('index')
    else:
        form = RegisterForm()
    return render(request, 'accounts/signup.html', {'form': form})
