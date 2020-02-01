from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from basic_app import models
from django.urls import reverse_lazy

# Create your views here.


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        ''' Adds a context to the template '''
        context = super().get_context_data(**kwargs)
        context["injected"] = "Basic injection"
        return context


class SchoolListView(ListView):
    context_object_name = "school_list"
    model = models.School
    template_name = "basic_app/school_list.html"


class SchoolDetailView(DetailView):
    context_object_name = "school_detail"
    model = models.School
    template_name = "basic_app/school_detail.html"


class SchoolCreateView(CreateView):
    # template_name = "basic_app/school_create.html"
    model = models.School
    fields = ("name", "principal", "location")


class SchoolUpdateView(UpdateView):
    # template_name = "basic_app/school_update.html"
    model = models.School
    fields = ("name", "principal", "location")


class SchoolDeleteView(DeleteView):
    # template_name = "basic_app/school_delete.html"
    # context_object_name = school
    model = models.School
    success_url = reverse_lazy("basic_app:school_list")


class CBView(View):
    def get(self, request):
        return HttpResponse("This is a class based view")
