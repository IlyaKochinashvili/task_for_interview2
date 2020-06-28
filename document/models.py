from django.db import models


class DocumentType(models.Model):
    name = models.CharField(max_length=100)
    validity_period = models.BooleanField(default=True)
    series = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class LostDocument(models.Model):
    identifier = models.CharField(max_length=100, unique=True)
    series = models.CharField(max_length=100)
    number = models.CharField(max_length=100)
    document_type = models.ForeignKey(DocumentType, on_delete=models.CASCADE)
    status = models.CharField(max_length=100)
    event_date = models.CharField(max_length=100)
    date_recorded = models.CharField(max_length=100)
    event_registration_authority = models.CharField(max_length=100)

    def __str__(self):
        return self.identifier


class ParsedFiles(models.Model):
    file_id = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.file_id
