# -*- coding: utf-8 -*-


import re
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
# Create your views here.
from search.tasks import Task
from search.dbase import DataBase, MongoBase

class IndexView(TemplateView):
    template_name = 'search/index.html'

    def get_context_data(self, **kwargs):
        r = "^http[s]?"
        iter = DataBase().get_all()
        context = []
        for i in iter:
            address = i[1]
            if re.match(r, i[1]) is None:
                address = "http://%s" % i[1]
            context.append(
                {
                    "name": i[0],
                    "address": address
                }
            )
        print context
        return {'context': context, 'count': len(context)}


class TaskCallView(View):
    def get(self, request, *args, **kwargs):
        Task().TaskSearchCourses()
        return redirect('search:index')


class BlackListView(View):
    def get(self, request, *args, **kwargs):
        url = kwargs['url']
        name = kwargs['name']
        DataBase().remove(name)
        DataBase().save_black(url)
        return redirect('search:index')
