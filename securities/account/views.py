from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Securities
from django.db.models import F


class Home(ListView):
    model = Securities
    template_name = 'account/all_page.html'
    context_object_name = 'home_security'

    def get_queryset(self):
        return Securities.objects.all()



class SecurityPage(ListView):
    pass
