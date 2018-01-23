from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView, RedirectView, TemplateView, ListView, DetailView, UpdateView, \
    DeleteView

from wishlist.models import wish


class HomePage(ListView):
    model = User
    template_name = 'home.html'

class WishListView(ListView):
    model = wish
    template_name = 'home.html'


class WishDetailView(DetailView):
    model = wish
    template_name = 'wish_detail.html'

class WishCreateView(CreateView):
    model = wish
    template_name = 'wish_new.html'
    fields = '__all__'

class WishUpdateView(UpdateView):
    model = wish
    fields = ['description']
    template_name = 'wish_edit.html'

class WishDeleteView(DeleteView):
    model = wish
    template_name = 'wish_delete.html'
    success_url = reverse_lazy('home')
