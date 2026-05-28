from django.http import FileResponse

from rest_framework.decorators import api_view

from rest_framework.response import Response

from rest_framework import status

from .models import Document

from .serializers import DocumentSerializer

@api_view(['POST'])

#logic behind the upload document service
def upload_document(request):

    serializer = DocumentSerializer(
        data=request.data
    )

    if serializer.is_valid():

        serializer.save()

        return Response(

            serializer.data,

            status=status.HTTP_201_CREATED
        )

    return Response(

        serializer.errors,

        status=status.HTTP_400_BAD_REQUEST
    )

#logic behind the get all documents service

@api_view(['GET'])

def list_documents(request):

    documents = Document.objects.all()

    serializer = DocumentSerializer(
        documents,
        many=True
    )

    return Response(

        {
            'message': 'Documents fetched successfully',

            'data': serializer.data
        },

        status=status.HTTP_200_OK
    )

#logic behind the get single document service
@api_view(['GET'])

def get_document(request, document_id):

    try:

        document = Document.objects.get(
            id=document_id
        )

    except Document.DoesNotExist:

        return Response(

            {
                'message': 'Document not found'
            },

            status=status.HTTP_404_NOT_FOUND
        )

    serializer = DocumentSerializer(
        document
    )

    return Response(

        {
            'message': 'Document fetched successfully',

            'data': serializer.data
        },

        status=status.HTTP_200_OK
    )

#logic behind the delete document service
@api_view(['DELETE'])

def delete_document(request, document_id):

    try:

        document = Document.objects.get(
            id=document_id
        )

    except Document.DoesNotExist:

        return Response(

            {
                'message': 'Document not found'
            },

            status=status.HTTP_404_NOT_FOUND
        )

    document.delete()

    return Response(

        {
            'message': 'Document deleted successfully'
        },

        status=status.HTTP_200_OK
    )

#logic behind download document service
@api_view(['GET'])

def download_document(request, document_id):

    try:

        document = Document.objects.get(
            id=document_id
        )

    except Document.DoesNotExist:

        return Response(

            {
                'message': 'Document not found'
            },

            status=status.HTTP_404_NOT_FOUND
        )

    return FileResponse(

        document.file.open(),

        as_attachment=True
    )