from django.shortcuts import render,redirect
from item.models import Category,Item
from django.contrib.auth.models import auth
from .forms import SignupForm
# Create your views here.
def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()
    content = {
        'categories': categories,
        'items': items,
    }
    return render(request,'main/index.html',content)
def contact(request):
    return render(request,'main/contact.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()
    return render(request, 'main/signup.html', {
        'form': form
    })

def logout(request):
    auth.logout(request)
    return redirect('/')