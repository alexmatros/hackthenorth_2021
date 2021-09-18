from django.shortcuts import render

# Create your views here.
def starting_page(request):
    return render(request, "outfit_generator/index.html")

def select_style(request):
    return render(request, "outfit_generator/select_style.html")

def outfit_generator(request):
    pass