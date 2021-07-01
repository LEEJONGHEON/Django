from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="list"),
    path('<int:post_id>', views.detail, name="detail"),
    path('new', views.new, name="new"),
    path('create', views.create, name="create"),
    path('updateForm/<int:post_id>', views.updateForm, name="updateForm"),
    path('update/<int:post_id>', views.update, name="update"),
    path('delete/<int:post_id>', views.delete, name="delete"),
    path('result', views.result, name="result"),
]