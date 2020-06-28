from django.urls import path

from document.views import LostDocumentView, LostDocumentApiView, information

urlpatterns = [
    path("", LostDocumentView.as_view(), name="lost_document"),
    path("find-documents", LostDocumentApiView.as_view(), name="find-documents"),
    path("info/", information, name="info")
]
