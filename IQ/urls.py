from django.urls import path, include
from .views import (
    Registration,
)

urlpatterns = [
    # ... your other urls here...
    path("registration/", Registration.as_view()),
]
