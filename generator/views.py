from django.shortcuts import render, redirect
from .models import Passwords
from random import choice, shuffle
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from array import array


def home(request):
    flag = 0
    if request.user.is_authenticated:
        flag = 1
    return render(request,'generator/index.html', {'flag':flag})


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = UsernameField(widget=forms.TextInput(
                                                        attrs = {
                                                        'class': 'form-control',
                                                        'placeholder': 'Username',
                                                        }
                                                    )
                            )
    password = forms.CharField(widget=forms.PasswordInput(
                                                            attrs = {
                                                            'class': 'form-control',
                                                            'placeholder': 'Password',
                                                            }
                                                        )  
                            )


class SignupForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control','id':'Username'}),
            'email': forms.TextInput(attrs={'type':'email','class':'form-control','id':'Email'}),
            'password': forms.PasswordInput(attrs={'type':'password','class':'form-control','id':'Password'})
        }


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        print(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create(username=username, email=email)
            user.set_password(password)
            user.save()
            user2 = authenticate(username=username, password=password)
            login(request, user2)
            return redirect("home")
    else:
        form = SignupForm()

    return render(request ,'generator/signup.html', {'form':form})


def password(request):
    len = int(request.GET.get('length',8))

    Upercase = request.GET.get('Upercase')
    numbers = request.GET.get('numbers')
    special_sign = request.GET.get('special_sign')

    DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']  
    LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 
                        'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                        'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                        'z']
    
    UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 
                        'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
                        'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                        'Z']
    
    SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', 
            '*', '(', ')', '<']
    
    rand_digit = choice(DIGITS)
    rand_upper = choice(UPCASE_CHARACTERS)
    rand_lower = choice(LOCASE_CHARACTERS)
    rand_symbol = choice(SYMBOLS)

    temp_pass = rand_lower
    count = 0

    COMBINED_LIST = LOCASE_CHARACTERS
    if Upercase:
        COMBINED_LIST = COMBINED_LIST + UPCASE_CHARACTERS
        temp_pass = temp_pass + rand_upper
        count += 1
    if numbers:
        COMBINED_LIST = COMBINED_LIST + DIGITS
        temp_pass = temp_pass + rand_digit
        count += 1
    if special_sign:
        COMBINED_LIST = COMBINED_LIST + SYMBOLS
        temp_pass = temp_pass + rand_symbol
        count += 1
    
    for x in range(len - count):
        temp_pass = temp_pass + choice(COMBINED_LIST)
        temp_pass_list = array('u', temp_pass)
        shuffle(temp_pass_list)
    
    password = ""
    for x in temp_pass_list:
            password = password + x

    if request.GET.get('website'):
         website = request.GET.get('website')
    else:
        website = "Not entered"


    if request.user.is_authenticated:
        Passwords.objects.create(
                                    password = password,
                                    website = website,
                                    user = request.user
                                )


    return render(request,'generator/password.html',{ 'password' : password })


@login_required
def MyPassword(request):
    password = request.user.passwords.all()
    return render(request ,'generator/mypass.html', {"password": password})


def delete_password(request, id):
    password = Passwords.objects.get(id=id)
    password.delete()
    return redirect("panel")