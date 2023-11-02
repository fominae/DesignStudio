from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import RegisterUserForm
from .models import Application


# Create your views here.

def index(request):
    Application_title = Application.objects.all()
    Application_description = Application.description
    Application_category = Application.category
    return render(request, 'index.html', context={'Application_title': Application_title,
                                                  'Application_description': Application_description,
                                                  'Application_category': Application_category})


class RegisterView(CreateView):
    template_name = 'registration/register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('login')
