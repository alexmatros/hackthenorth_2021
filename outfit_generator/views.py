from django.shortcuts import render

# Create your views here.
def starting_page(request):
    return render(request, "outfit_generator/index.html")

def outfit_generator(request):
    pass