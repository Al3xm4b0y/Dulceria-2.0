from django.shortcuts import render

# Create your views here.
# creaciom de ruta hacia el archivo html 'principal.html'
def home(request):
    return render(request,'core/principal.html')
# creaciom de ruta hacia el archivo html 's.nosotros.html'
def nosotros(request):
    return render(request,'core/s.nosotros.html')
# creaciom de ruta hacia el archivo html 'colaboradores'
def colaborador(request):
    return render(request,'core/colaborador.html')
# creaciom de ruta hacia el archivo html 'contactos'
def contacto(request):
    return render(request,'core/contactos.html')
