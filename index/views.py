from django.shortcuts import render
from django.contrib import messages
from vet.models import VetClient, VetUsers

# Create your views here.
def index(request):
    VetClient = VetClient.objects.all()
    vetUser = VetUsers.objects.all()
    
    context = {
        "vetclient":VetClient,
        "vetuser":VetUsers
    }

    if request.method == 'GET':
        return render(request, 'home.html', context=context)
    
