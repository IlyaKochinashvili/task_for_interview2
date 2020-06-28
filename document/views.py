from django.shortcuts import render
from django.views.generic import FormView
from rest_framework.views import APIView
from document.forms import LostDocumentForm
from document.models import LostDocument
from document.serializers import LostDocumentSerializer
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist


class LostDocumentView(FormView):
    template_name = 'home.html'
    form_class = LostDocumentForm
    success_url = "info"


def information(request):
    form = LostDocumentForm(request.POST)
    if form.is_valid():
        search_phrase = form['document'].value()
        series = search_phrase[0:2]
        number = search_phrase[2:]
        try:
            document = LostDocument.objects.get(series=series, number=number)
            context = {"document": document}
            return render(request, "info.html", context)
        except ObjectDoesNotExist:
            context = {"document": ""}
            return render(request, "info.html", context)
    else:
        context = None
        return render(request, "info.html", context)


class LostDocumentApiView(APIView):

    @staticmethod
    def post(request, ):
        report_type = request.data['report_type']
        search_phrase = request.data['search_phrase'].replace(" ", "")
        series = search_phrase[0:2]
        number = search_phrase[2:]
        doc = LostDocument.objects.filter(series=series, number=number).first()
        if not doc:
            if report_type == 'full':
                return Response([])
            elif report_type == 'compact':
                return Response({0})
        if doc and report_type == 'compact':
            return Response({1})
        elif doc and report_type == 'full':
            serializer = LostDocumentSerializer(doc)
            return Response(serializer.data)
