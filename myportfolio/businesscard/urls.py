from django.urls import path
# from django.conf.urls import url
from . import views


urlpatterns = [
    # url(r'', views.businesscard_index, name="bootstrap_index"),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('skills/', views.skills, name='skills'),
    path('contact', views.contact, name='contact'),
    path('resume/', views.resume, name='resume'),
    path('projects/', views.projects, name='projects'),
    # path('favicon/', ),
]