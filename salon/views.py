import datetime
from django.shortcuts import render
from django.views import generic
from salon.models import Menu, Stylist, Booking, User
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .forms import BookingForm

# Create your views here.

def index(request):

  return render(request, 'index.html')


class MenuListView(generic.ListView):
  model = Menu


class MenuDetailView(generic.DetailView):
  model = Menu


class StylistView(generic.ListView):
  model = Stylist


class StylistDetailView(generic.DetailView):
  model = Stylist
  

class BookingCreate(LoginRequiredMixin, CreateView):
  model = Booking
  form_class = BookingForm
  # fields = ['username', 'phone_no', 'booking_date', 'stylist']
  

  def form_valid(self, form):
    form.instance.user = self.request.user
    form.instance.menu=get_object_or_404(Menu, pk = self.kwargs['pk'])
    return super(BookingCreate, self).form_valid(form)


  def get_context_data(self, **kwargs):
    context = super(BookingCreate, self).get_context_data(**kwargs)
    context['menu'] = get_object_or_404(Menu, pk = self.kwargs['pk'])
    return context

  def get_initial(self):
    initial = super().get_initial()
    username = User.objects.get(username=self.request.user)
    initial['username'] = username
    return initial  


  def get_success_url(self): 
    return reverse('menu-detail', kwargs={'pk': self.kwargs['pk'],})
