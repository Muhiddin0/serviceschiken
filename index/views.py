from django.shortcuts import render
from vet.models import VetUsers, VetClient
from delivered.models import DeliverUsers, Delivered

# Create your views here.
def index(request):
    vetUser = VetUsers.objects.all()
    delivred = DeliverUsers.objects.all()
    context = {
        "delivred":delivred,
        "vetuser":vetUser
    }

    if request.method == 'GET':
        return render(request, 'home.html', context=context)

def delivers(request):
    if request.method == "GET":
        delivers = Delivered.objects.all()
        print(delivers)
        context = {
            "delivers":delivers
        }
        return render(request, 'delivred.html', context)

def vets(request):
    if request.method == "GET":
        vet = VetClient.objects.all()
        context = {
            "vet":vet
        }
        return render(request, 'vet.html', context)
