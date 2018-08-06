'''
views for alphacheck api
'''
import json

from django.http import Http404
import coreapi
import coreschema
from rest_framework.response import Response
from rest_framework.schemas import AutoSchema
from rest_framework.views import APIView

from .utils import has_all_alphabet


class CheckAlphabet(APIView):
    '''
    simple APIView for alphacheck api
    '''
    schema = AutoSchema(manual_fields=[
        coreapi.Field(
            'case_insensitive',
            required=False,
            location='query',
            schema=coreschema.Boolean(),
        ),
    ])
    # pylint: disable=redefined-builtin, unused-argument
    def get(self, request, query, format=None):
        '''
        HTTP GET method that checks whether query contains all letters of the alphabet
        '''
        try:
            case_insensitive = json.loads(
                request.query_params.get('case_insensitive', 'false')
            )
        except json.JSONDecodeError:
            case_insensitive = False

        try:
            response = has_all_alphabet(
                query,
                case_insensitive=case_insensitive,
                version=request.version
            )
        except KeyError:
            raise Http404

        return Response({
            'response': response,
        })
