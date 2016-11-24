from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
# Create your views here.
from search.tasks import TaskSearchCourses

class IndexView(TemplateView):
    template_name = 'search/index.html'

    def get_context_data(self, **kwargs):
        return {}


class TaskCallView(View):
    def get(self, request, *args, **kwargs):
        TaskSearchCourses()
        return redirect('search:index')

