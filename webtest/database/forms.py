from .models import Client, Halls
from django.forms import ModelForm, TextInput, DateTimeInput, EmailInput, EmailField, CharField
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django import forms


class HallsForm(ModelForm):
    class Meta:
        model = Halls
        fields = ['Hall_Name', 'Price_Weekdays_8_17', 'Price_Weekdays_17_8', 'Price_Weekends_8_17', 'Price_Weekends_17_8']

        widgets = {
            "Hall_Name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название зала'
            }),
            "Price_Weekdays_8_17": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Цена в будни с 8 до 17'
            }),
            "Price_Weekdays_17_8": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Цена в будни с 17 до 8'
            }),
            "Price_Weekends_8_17": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Цена в выходные с 8 до 17'
            }),
            "Price_Weekends_17_8": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Цена в выходные с 17 до 8'
            }),
        }

class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ['Surname', 'Name', 'Mid_Name', 'Number', 'Email', 'Date', 'Time_range', 'Type_of_Service']

        widgets = {
            "Surname": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Фамилия'
            }),
            "Name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя'
            }),
            "Mid_Name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Отчество'
            }),
            "Number": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номер'
            }),
            "Email": EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email'
            }),
            "Date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата дд.мм.гг чч.мм'
            }),
            "Time_range": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Время аренды в часах'
            }),
            "Type_of_Service": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Выбранная услуга'
            })
        }

class RegistrForm(UserCreationForm):
    username = forms.Field(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'myfield'}))
    last_name = forms.Field(label='Фамилия', widget=forms.TextInput(attrs={'class': 'myfield'}))
    first_name = forms.Field(label='Имя', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.Field(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': 'Не менее 8 симлов, цифры и буквы'}))
    password2 = forms.Field(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': 'Повторите ввод пароля'}))
    class Meta:
        model = User
        fields = ('last_name', 'first_name', 'username','email', 'password1', 'password2')
        widgets = {
            'last_name': forms.TextInput(attrs={'class': 'form-input','placeholder': 'Фамилия'}),
            'first_name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Имя'}),
            'email': forms.EmailInput(attrs={'class': 'form-input', 'placeholder': 'Email'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': 'Не менее 8 симлов, цифры и буквы'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': 'Повторите ввод пароля'}),
        }



class ChangeSettingsForm(UserChangeForm):
    username = forms.Field(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'change', 'id': 'username_change'}))
    last_name = forms.Field(label='Фамилия', widget=forms.TextInput(attrs={'class': 'change', 'id': 'last_change'}))
    first_name = forms.Field(label='Имя', widget=forms.TextInput(attrs={'class': 'change', 'id': 'first_change'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'change', 'id': 'email_change'}))
    class Meta:
        model = User
        fields = ('last_name', 'first_name', 'username','email')