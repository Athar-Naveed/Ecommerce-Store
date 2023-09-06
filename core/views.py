from django.shortcuts import render,redirect
from item.models import Item,Category
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth import logout
# Create your views here.
def index(request):
    items = Item.objects.filter(is_sold=False)
    categories = Category.objects.all()
    return render(request,'index.html',{
        'items':items,
        'categories':categories
    })

def signup(request):
    if request.method == "POST":
       form = SignUpForm(request.POST)
       if form.is_valid():
        form.save()
        messages.success(request,"User Registration Success!")
        return redirect('/login/')

    else:
        form = SignUpForm()
    return render(request,'signup.html',{'form':form})

def logout_user(request):
   logout(request)
   return redirect('login')