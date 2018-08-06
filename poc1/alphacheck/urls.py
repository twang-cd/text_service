'''
urls for alphacheck api
'''
from django.urls import include, path

from . import views
from .utils import VERSION_REGISTRY


# pylint: disable=invalid-name
urls = [
    path('<str:query>', views.CheckAlphabet.as_view()),
]

urlpatterns = [
    path('%s/' % version, include((urls, version), namespace=version))
    for version in VERSION_REGISTRY.keys()
]
