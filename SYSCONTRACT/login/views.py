from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# View para o login
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Redireciona para a página do dashboard
        else:
            messages.error(request, 'Usuário ou senha inválidos.')
    
    return render(request, 'login/login.html')

# View para o registro
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Conta criada com sucesso! Agora faça login.')
            return redirect('login')
    else:
        form = UserCreationForm()
    
    return render(request, 'login/register.html', {'form': form})

# View para fazer logout
def logout_view(request):
    logout(request)
    return redirect('login')  # Redireciona o usuário para a página de login após o logout

# View para o dashboard, requer login
@login_required
def dashboard_view(request):
    return render(request, 'login/dashboard.html')  