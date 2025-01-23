from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from myProject.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", book_collection, name="book_collection"),
    path("add_book/", add_book, name="add_book"),
    
    path("book_view/ <int:id>", book_view, name="book_view"),
    path("deletepage/ <int:id>", deletepage, name="deletepage"),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
