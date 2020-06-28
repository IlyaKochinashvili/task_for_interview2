from django.contrib import admin

from document.models import DocumentType, LostDocument, ParsedFiles


@admin.register(DocumentType)
class DocumentTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(LostDocument)
class LostDocumentAdmin(admin.ModelAdmin):
    pass


@admin.register(ParsedFiles)
class ParsedFilesAdmin(admin.ModelAdmin):
    pass
