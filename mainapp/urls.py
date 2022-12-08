from django.urls import path

from mainapp import views
from mainapp.apps import MainappConfig

app_name = MainappConfig.name

urlpatterns = [
    path('contacts/', views.ContactsView.as_view(), name='contacts'),
    path('courses/', views.CoursesView.as_view(), name='courses'),
    path('docsite/', views.DocSiteView.as_view(), name='docsite'),
    path('', views.IndexView.as_view(), name='index'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('news/', views.NewsView.as_view(), name='news'),
    path('news/<pk>/', views.NewsDetail.as_view(), name='news_detail'),
]
