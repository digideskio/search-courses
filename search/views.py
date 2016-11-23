from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
from search.tasks import TaskSearchCourses

class IndexView(TemplateView):
    template_name = 'search/index.html'

    def get_context_data(self, **kwargs):
        TaskSearchCourses()
