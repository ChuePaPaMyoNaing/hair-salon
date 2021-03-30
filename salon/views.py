import datetime
from django.shortcuts import render
from django.views import generic
from salon.models import Menu, Stylist
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

# Create your views here.

def index(request):

  context = {
  }

  return render(request, 'index.html', context=context)


class MenuListView(generic.ListView):
  model = Menu


class MenuDetailView(generic.DetailView):
  model = Menu


class StylistView(generic.ListView):
  model = Stylist


class StylistDetailView(generic.DetailView):
  model = Stylist    
