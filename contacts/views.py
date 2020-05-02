from rest_framework import viewsets, mixins
from .serializers import ContactSerializer, UserSerializer
from .models import Contact
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from django.contrib.auth.models import User

class UserViewSet(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer

    def get_queryset(self):
        user = self.request.user
        return User.objects.filter(id=self.request.user.id)

    # def perform_create(self, serializer):
    #     username = self.request.POST.get('usernmae', None)
    #     password = self.request.POST.get('password', None)
    #     serializer.save(username=username, password=password)

class ContactsViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = ContactSerializer

    def get_queryset(self):
        user = self.request.user
        return Contact.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


    @action(methods=['GET'], detail=False, url_path='search')
    def search(self, request):
        user = self.request.user
        queryset = Contact.objects.filter(user=user)
        name = self.request.query_params.get('name', None)
        email = self.request.query_params.get('email', None)
        if name is not None:
            queryset = queryset.filter(name__icontains=name)
        if email is not None:
            queryset = queryset.filter(email__icontains=email)
        contacts = ContactSerializer(queryset, many=True).data
        return Response({"contacts": contacts}, status=200)