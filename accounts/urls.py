from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('amdin/', admin.site.urls),
    path('accounts/', include('accounts.urls'))
]
