from django.shortcuts import render

# Create your views here.

def projetos(request):
    if request.method == "GET":
        return render(request, 'projetos/projetos.html')


