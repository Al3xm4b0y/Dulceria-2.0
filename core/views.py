from django.shortcuts import render

# Create your views here.
# metodos que llaman a los html
def home(request):  # resiven siempre como parametro request
    return render(request ='core/principal.html')