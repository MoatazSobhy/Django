from django.shortcuts import render
# from django.http import HttpResponse


# Create your views here.
def index(request):
    # return HttpResponse("<h1> This is mart <h1/>")
    # varname = "Moataz"
    # varname2 = ["Moataz", "Sobhy", "Zaki"]
    # varname3 = {"Glasses":150, "Paper":110, "Scissors": 210}
    varname4 = {
        "Glasses": {"price": 150, "image_url": "https://m.media-amazon.com/images/I/31QPu+05EaL._AC_SY580_.jpg"},
        "Paper": {"price": 110, "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSF2m7CWtSAkz8qzir-kHKgjG_GkfAfnbGFSQ&s"},
        "Scissors": {"price": 210, "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT30gTJwD7UdsQCeU1F1hNKM7Soymu5PI65lQ&s"},
    }
    if request.method == "post":
        print(request.post)
    # return render(request, "mart/index.html", {"name":varname})
    # return render(request, "mart/index.html", {"namelist":varname2})
    # return render(request, "mart/index.html", {"namedic":varname3})
    return render(request, "mart/index.html", {"namedic2":varname4})

