from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from rest_framework import generics
from rest_framework import permissions
from rest_framework import authentication

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer

from .models import Clipboard
from .serializers import ClipboardSerializer


class ClipboardList(generics.ListCreateAPIView):
    queryset = Clipboard.objects.all()
    serializer_class = ClipboardSerializer
    authentication_classes = (authentication.SessionAuthentication,
                              authentication.TokenAuthentication)
    permission_classes = (permissions.IsAuthenticated,)


class ClipboardDetail(generics.RetrieveUpdateAPIView):
    queryset = Clipboard.objects.all()
    serializer_class = ClipboardSerializer
    authentication_classes = (authentication.SessionAuthentication,
                              authentication.TokenAuthentication)
    permission_classes = (permissions.IsAuthenticated,)

class ClipboardSnippetList(generics.ListCreateAPIView):
    serializer_class = SnippetSerializer
    authentication_classes = (authentication.SessionAuthentication,
                              authentication.TokenAuthentication)
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        clipboard = get_object_or_404(Clipboard, pk=self.kwargs['pk'])
        return Snippet.objects.filter(clipboard=clipboard)