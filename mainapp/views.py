from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView


class ContactsView(TemplateView):
    template_name = 'mainapp/contacts.html'


class CoursesView(TemplateView):
    template_name = 'mainapp/courses_list.html'


class DocSiteView(TemplateView):
    template_name = 'mainapp/doc_site.html'


class IndexView(TemplateView):
    template_name = 'mainapp/index.html'


class LoginView(TemplateView):
    template_name = 'mainapp/login.html'


class NewsView(TemplateView):
    template_name = 'mainapp/news.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['object_list'] = [
            {
                'title': 'Новость',
                'preview': 'Предварительное описание новости',
                'date': '2021-04-29 20-50-26'
            }, {
                'title': 'Новость',
                'preview': 'Предварительное описание новости',
                'date': '2021-04-29 20-50-26'
            }, {
                'title': 'Новость',
                'preview': 'Предварительное описание новости',
                'date': '2021-04-29 20-50-26'
            }, {
                'title': 'Новость',
                'preview': 'Предварительное описание новости',
                'date': '2021-04-29 20-50-26'
            }, {
                'title': 'Новость',
                'preview': 'Предварительное описание новости',
                'date': '2021-04-29 20-50-26'
            }
        ]
        return context_data
