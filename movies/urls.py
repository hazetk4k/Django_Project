from django.urls import path, re_path
from django.utils import archive

from .views import *

urlpatterns = [
    path('', index),
    path('category/<int:cat_id>/', category),
    re_path(r"archive/(?P<year>[0-9]{4})/", archive)
]
