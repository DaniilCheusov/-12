from django.shortcuts import render, redirect
from .models import Client
from .forms import ClientForm
from .forms import RegistrForm
from .forms import ChangeSettingsForm
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.views.generic import DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse_lazy
from django.contrib.auth import logout, login


def regist(request):
    data = {}
    if request.method == 'POST':
        form = RegistrForm(request.POST)
        if form.is_valid():
            form.save()
            data['form'] = form
            messages.success(request, 'Регистрация успешно завершина!')
            return redirect('home')
    else:
        form = RegistrForm()
        data['form'] = form
        return render(request, 'database/regist.html', data)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

# def login(request):
#     data = {}
#     if request.method == 'POST':
#         form = AuthenticationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             data['form'] = form
#             messages.success(request, 'Вы вошли в аккаунт!')
#             return  render(request, 'main/index.html', data)
#     else:
#         form = AuthenticationForm()
#         data['form'] = form
#         return render(request, 'database/regist.html', data)

# def login(request):
#    return render(request, 'database/login.html')
# def Personal_area(request):
#     return render(request, 'database/Personal_area.html')

class LoginUser(LoginView):
    form_class =  AuthenticationForm
    template_name = 'database/login.html'

    def get_success_url(self):
        return reverse_lazy('Personal_area')

def Personal_area(request):
    data = {}
    if request.method == 'POST':
        form = ChangeSettingsForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            data['form'] = form
            messages.success(request, 'Изменения успешно применены!')
            return redirect('home')
    else:
        form = ChangeSettingsForm(instance=request.user)
        data['form'] = form
        return render(request, 'database/Personal_area.html', data)

# def Personal_area(request):
#     if request.method == 'POST':
#         form = ChangeSettingsForm(request.POST, instance=request.user)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Your profile is updated successfully')
#             return redirect('home')
#     else:
#         form = ChangeSettingsForm(instance=request.user)
#
#     return render(request, 'database/Personal_area.html')

def Service1(request):
    error = ''
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ваша заявка успешно отправлена! Ожидайте ответа на почту')
            return redirect('home')
        else:
            error = 'Некорректно заполнена форма'

    form = ClientForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'database/Personal_area.html', data)



def Service1(request):
    error = ''
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ваша заявка успешно отправлена! Ожидайте ответа на почту')
            return redirect('home')
        else:
            error = 'Некорректно заполнена форма'

    form = ClientForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'database/Service1.html', data)

def Service2(request):
    error = ''
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ваша заявка успешно отправлена! Ожидайте ответа на почту')
            return redirect('home')
        else:
            error = 'Некорректно заполнена форма'

    form = ClientForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'database/Service2.html', data)

def Service3(request):
    error = ''
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ваша заявка успешно отправлена! Ожидайте ответа на почту')
            return redirect('home')
        else:
            error = 'Некорректно заполнена форма'

    form = ClientForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'database/Service3.html')

def Service4(request):
    error = ''
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ваша заявка успешно отправлена! Ожидайте ответа на почту')
            return redirect('home')
        else:
            error = 'Некорректно заполнена форма'

    form = ClientForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'database/Service4.html')

def Service5(request):
    error = ''
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ваша заявка успешно отправлена! Ожидайте ответа на почту')
            return redirect('home')
        else:
            error = 'Некорректно заполнена форма'

    form = ClientForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'database/Service5.html')

def Service6(request):
    error = ''
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ваша заявка успешно отправлена! Ожидайте ответа на почту')
            return redirect('home')
        else:
            error = 'Некорректно заполнена форма'

    form = ClientForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'database/Service6.html')

def Service7(request):
    error = ''
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ваша заявка успешно отправлена! Ожидайте ответа на почту')
            return redirect('home')
        else:
            error = 'Некорректно заполнена форма'

    form = ClientForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'database/Service7.html')
