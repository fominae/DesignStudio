from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from .forms import RegisterUserForm
from .models import Application


# Create your views here.


class RegisterView(CreateView):
    template_name = 'registration/register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('login')


class ViewRequests(ListView):
    model = Application
    template_name = 'index.html'
    context_object_name = 'applications'

    def get_queryset(self):
        return Application.objects.filter(status__exact='Выполнено').order_by('-date_create')[:4]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['number_of_applications'] = Application.objects.filter(status__exact='Принято в работу').count()
        return context

class MyLoginView(LoginView):
    template_name = 'registration/login.html'


class MyLogoutView(LogoutView):
    template_name = 'registration/logged_out.html'


