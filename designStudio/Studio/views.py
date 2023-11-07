from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from .forms import *
from .models import Application, Category


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
        return Application.objects.filter(status__exact='Выполнено').order_by('-date_create', 'time_create')[:4]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['number_of_applications'] = Application.objects.filter(status__exact='Принято в работу').count()
        return context


class MyLoginView(LoginView):
    template_name = 'registration/login.html'


class MyLogoutView(LogoutView):
    template_name = 'registration/logged_out.html'
    success_url = reverse_lazy('login')


class User_requests(LoginRequiredMixin, generic.ListView):
    model = Application
    template_name = 'Studio/application_list_by_user.html'
    context_object_name = 'applications'

    def get_queryset(self):
        status = self.request.GET.get('status')
        filter_application = Application.objects.filter(owner=self.request.user)
        if status:
            filter_application = filter_application.filter(status=status)
        return filter_application


class ApplicationCreate(LoginRequiredMixin, CreateView):
    model = Application
    fields = ['application_title', 'description', 'category', 'photo_of_room']
    success_url = reverse_lazy('my_application')

    def form_valid(self, form):
        form.instance.owner = self.request.user

        return super().form_valid(form)


class ApplicationDelete(LoginRequiredMixin, DeleteView):
    model = Application
    success_url = reverse_lazy('my_application')


class CategoryAdmin(generic.ListView):
    model = Application
    template_name = 'Studio/application_list_by_admin.html'
    context_object_name = 'categoryA'


class CategoryView(ListView):
    model = Category
    template_name = 'Studio/CategoryListView.html'
    context_object_name = 'categoryAd'


class CategoryDelete(DeleteView):
    model = Category
    template_name = 'Studio/category_confirm_delete.html'
    success_url = reverse_lazy('categoryList')


class CategoryCreate(CreateView):
    model = Category
    fields = ['category']
    template_name = 'Studio/Category_form.html'
    success_url = reverse_lazy('categoryList')


class ChangeApplicationStatus(LoginRequiredMixin, UpdateView):
    model = Application
    form_class = ApplicationStatusForm
    template_name = 'Studio/change_application_status.html'
    success_url = reverse_lazy('categoryAdmin')
    context_object_name = 'applications'

    def test_func(self):
        return self.request.user.is_superuser

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        print(self.request.FILES)
        form = ApplicationStatusForm(self.request.POST, self.request.FILES, instance=self.object)
        form.save()
        return super().form_valid(form)