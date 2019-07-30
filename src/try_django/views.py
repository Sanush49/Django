from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from .forms import ContactForm 

def home_page(request):
	my_title="Hello there..."
	context ={"title":my_title,"list":[1,2,3,4,5]}
	return render(request,"home.html",context)

def about_page(request):
	return render(request,"about.html",{"title": "About Us"})

def contact_page(request):
	form =ContactForm(request.POST or None)
	if form.is_valid():
		print(form.cleaned_data)
		form = ContactForm()
	context ={
		"title": "Contact Us",
		"form" : form
	}
	return render(request,"form.html",context)

def example_page(request):
	context = {"title":"Example"}
	template_name = "base.html"
	template_obj = get_template(template_name)
	return HttpResponse(template_obj.render(context)) 

def test_page(request):
	my_title = "Hey, there...."
	context = {"title":my_title}
	template_name="test.txt"
	template_obj=get_template(template_name)
	rendered_string=template_obj.render(context)
	print(rendered_string)
	return render(request,"base.html",{"title": rendered_string})
