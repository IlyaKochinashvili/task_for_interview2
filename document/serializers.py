from rest_framework import serializers

from document.models import LostDocument


class LostDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = LostDocument
        fields = [
            "identifier",
            "series",
            "number",
            "document_type",
            "status",
            "event_date",
            "date_recorded",
            "event_registration_authority",
        ]
