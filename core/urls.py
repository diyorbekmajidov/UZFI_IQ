from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from users.views import Index

urlpatterns = [
    path('admin/', admin.site.urls),
    
]+i18n_patterns (
    path('i18n/', include('django.conf.urls.i18n')),
    path('iq/', include("users.urls")),
    # path('', Index.as_view()),
)
