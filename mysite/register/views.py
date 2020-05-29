from django.shortcuts import render, redirect
from django.contrib import messages
from .registerform import CreateUserForm
from django.contrib.auth import authenticate, login, logout


def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, '¡La cuenta de ' + user + ' se a creado!')
                return redirect('singin')

        return render(request, 'register.html', {'form': form})


def entrar(request):
    context = {}
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'El nombre de usuario o contraseña son incorrectos.')
                return render(request, 'login.html', context)

        return render(request, 'login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('singin')

