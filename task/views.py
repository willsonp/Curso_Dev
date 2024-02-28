from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    return render(request, "home.html")

def signup(request):
    if request.method == "GET":
        return render(request, "signUp.html",{
            'form': UserCreationForm(),
        })
    else:
        if (request.POST['password1'] != request.POST['password2']):
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                return render(request, "home.html", {
                    'error': "User created successfully"
                })
            except:
                return render(request, "signUp.html", {
                    'form': UserCreationForm(),
                    'error': "Username already exists"
                })                
        else:
            return render(request, "signUp.html", {
                'form': UserCreationForm(),
                'error': "Passwords didn't match"
            
    })

