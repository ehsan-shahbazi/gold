from django.urls import path
from . import views
from .tasks import wrap_news, wrap_all

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('news', views.news, name='news'),
    path('contact', views.contact, name='contact'),
    path('do_your_job_man', views.tasks, name='ok'),
    path('new_user/', views.new_user, name='make_user')
]


