'''
views for alphacheck api
'''
from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView

from .utils import has_all_alphabet


class CheckAlphabet(APIView):
    '''
    simple APIView for alphacheck api
    '''
    # pylint: disable=redefined-builtin, unused-argument
    def get(self, request, query, format=None):
        '''
        HTTP GET method that checks whether query contains all letters of the alphabet
        '''
        try:
            response = has_all_alphabet(
                query,
                case_insensitive=request.query_params.get('case_insensitive', False),
                version=request.version
            )
        except KeyError:
            raise Http404

        return Response({
            'response': response,
        })
