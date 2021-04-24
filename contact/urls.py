from django.urls import path

from .views import ContactDetailView, ContactList




urlpatterns = [
    path('', ContactList.as_view(), name=""),
    path('<int:id>/', ContactDetailView.as_view(), name=""),
]