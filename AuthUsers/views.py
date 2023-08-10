from django.shortcuts import render, redirect
from AuthUsers.forms import RegisterForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate

# Create your views here.
def register_user(request):

    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST) 

        if form.is_valid(): 
            new_user = form.save() 

            messages.success(request, f'Вы зарегистрированы! добро пожаловать {new_user.username}')

            login(request, new_user) 
            return redirect('my_manga')

        else:
            messages.success(request, 'Произошла ошибка, введите правильно свои данные для регистрации.')

    return render(request, 'register.html', {'form':form})

def login_user(request):
 
    
    if request.method == 'POST': 
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password) 

        if user is not None: 
            login(request, user)
            messages.success(request, f'Добро пожаловать!! {username.upper()} 🥳')

            return redirect('my_manga')

        else: 
            messages.error(request, 'Неверные данные...')

    return render(request, 'login.html')

def logout_user(request):

    logout(request)

    return redirect('my_login')