from django.shortcuts import render, redirect
from .models import HomeSlider, HomeSliderActive, Category, SubCategory
from .forms import NewUserForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.


def index(request):
    slider_active = HomeSliderActive.objects.all()[0]
    slider = HomeSlider.objects.all()
    category_list = Category.objects.all()
    sub_category_list = SubCategory.objects.all()
    return render(request, 'main/index.html', context={
        'slider_active':slider_active,
        'slider':slider,
        'category_list':category_list,
        'sub_category_list':sub_category_list
    })


def index_detail(request, id):
    slider_active = HomeSliderActive.objects.all()[0]
    slider = HomeSlider.objects.all()
    category_list = Category.objects.all()
    category_list_detail = Category.objects.filter(pk=id)
    sub_category_list = SubCategory.objects.all()
    return render(request, 'main/index_detail.html', context={
        'slider_active':slider_active,
        'slider':slider,
        'category_list':category_list,
        'sub_category_list':sub_category_list,
        'category_list_detail':category_list_detail
    })

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("index")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render(request=request, template_name="main/register.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("index")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="main/login.html", context={"login_form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("index")