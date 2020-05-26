from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from .forms import FahrerForm, Lieferform
from .models import Fahrer, Fahrzeug, Kunde, Produkte, Lieferungen

# Create your views here.

def liefer_list(request):
    lieferlist = Lieferungen.objects.order_by('-datum_von')[:10]
    context = {'lieferlist': lieferlist}
    return render(request, 'collect/liefer_list.html', context)

def test(request):
    if request.method == "POST":
        fahrer_form = FahrerForm(request.POST)
        if fahrer_form.is_valid():
            Fahrer = fahrer_form.save(commit=False)
            Fahrer.save()

    else:
        fahrer_form = FahrerForm()
    return render(request, 'collect/test.html', {'fahrerform': fahrer_form})

def lieferschein(request):
    if request.method == "POST":
        liefer_form = Lieferform(request.POST)
        if liefer_form.is_valid():
            Lieferungen = liefer_form.save(commit=False)
            Lieferungen.save()

    else:
        liefer_form = Lieferform()
    return render(request, 'collect/lieferschein.html', {'lieferform': liefer_form})

def liefer_form_data(request, pk):


        fahrzeug_form_data = Fahrzeug.objects.filter(pk=pk).values() #getting the liked posts
        fahrzeug_form_data = list(fahrzeug_form_data)
        return JsonResponse(fahrzeug_form_data, safe=False) # Sending an success response
        #return HttpResponse(is_private)

def validate_username(request, pk):
    username = request.GET.get('username', None)
    username = pk

    data = {
        'is_taken': username
    }
    return JsonResponse(data)


