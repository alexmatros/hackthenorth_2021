from django.shortcuts import render

# Create your views here.
def starting_page(request):
    return render(request, "outfit_generator/index.html")

def select_style(request):
    return render(request, "outfit_generator/select_style.html")

def outfit_generator(request, style):
    style_name = style[style.index("-") + 1:style.rindex("-")].replace("-", " ")
    return render(request, "outfit_generator/outfit_generator.html", {
        "style": style_name
    })