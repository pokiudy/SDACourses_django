from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

import professor
from professor.forms import ProfessorForm
from professor.models import Professor


class ProfessorCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    template_name = 'professor/create_professor.html'
    model = Professor
    form_class = ProfessorForm
    success_url = reverse_lazy('home')
    permission_required = 'professor.add_professor'


class ProfessorListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    template_name = 'professor/list_of_professors.html'
    model = Professor
    context_object_name = 'all_professors'
    permission_required = 'professor.view_list_of_professors'

    def get_queryset(self):
        return Professor.objects.filter(active=True)


class ProfessorUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = 'professor/update_professor.html'
    model = Professor
    form_class = ProfessorForm
    success_url = reverse_lazy('list_of_professors')
    permission_required = 'professor.view_list_of_professors'


class ProfessorDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    template_name = 'professor/delete_professor.html'
    model = Professor
    success_url = reverse_lazy('list_of_professors')
    permission_required = 'professor.delete_professor'


class ProfessorDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    template_name = 'professor/details_professor.html'
    model = Professor
    permission_required = 'professor.view_professor'


@login_required
def inactivate_professor(request,pk):
    Professor.objects.filter(id=pk).update(active=False)
    return redirect('list_of_professors')


@login_required
def delete_professor(request,pk):
    Professor.objects.filter(id=pk).delete()
    return redirect('list_of_professors')