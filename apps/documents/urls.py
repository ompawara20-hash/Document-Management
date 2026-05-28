from django.urls import path

from .views import (

    upload_document,

    list_documents,

    get_document,

    delete_document,

    download_document
)


urlpatterns = [

    path(
        'upload/',
        upload_document
    ),

    path(
        '',
        list_documents
    ),

    path(
        '<int:document_id>/',
        get_document
    ),

    path(
        '<int:document_id>/delete/',
        delete_document
    ),

    path(
        '<int:document_id>/download/',
        download_document
    ),
]