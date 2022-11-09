from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import Credit, Account, Client


def index(request):
    client = Client.objects.all()
    context = {
        'clients': clients,
    }
    return render(request, 'index.html', context)


class ClientView(generic.ListView):
    model = Client
    template_name = 'index.html'
    context_object_name = 'clients'


class ClientDetail(generic.DetailView):
    model = Client
    context_object_name = 'client'


class QuestionDetailView(ClientDetail):
    template_name = 'detail.html'
