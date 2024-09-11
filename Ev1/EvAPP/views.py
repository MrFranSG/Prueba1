from django.shortcuts import render

# Create your views here.


def Juego1(request):
    data = {"MH" : "Monster Hunter", "R6": "Rainbow Six", "LOL" : "League of legends"}
    return render(request, "templates/templatesapp/menu1.html", data)

def Juego2(request):
    data = {"VG":"Monster hunter", "DS":"Un juego de cazar criaturas"}
    return render(request, "templates/templatesapp/juego.html", data)