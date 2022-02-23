from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import add_view, edit_view

urlpatterns = [
    path('add', actions/add_view), #add team members page
    path('edit', actions/edit_view), #edit team members page
]

urlpatterns += staticfiles_urlpatterns()