import json
from rest_framework import status
from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from contacts.models import Contact
from contacts.views import ContactsViewset
from contacts.serializers import ContactSerializer
from rest_framework.test import APIRequestFactory, force_authenticate


# initialize the APIClient app
factory = APIRequestFactory()


class ContactApiTest(TestCase):  # Test the ContactApiTest api

    def setUp(self):
        self.client = factory
        self.user = get_user_model().objects.create_user(
            'abcde@gmail.com',
            'abcde'
        )
        self.contact_casper = Contact.objects.create(
            name='Casper', email='abcd@email.com', phone_number='1234567890', user_id=self.user.id)
        self.contact_muffine = Contact.objects.create(
            name='Muffin', email='abcdp@email.com', phone_number='1234567890', user_id=self.user.id)


    def test_retrieve_contacts_list(self):  # Test retrieving a list of contacts
        request = factory.get('api/v1/contacts/')
        force_authenticate(request, user=self.user)
        view = ContactsViewset.as_view({'get': 'list'})
        res = view(request)
        ingredients = Contact.objects.filter(user=self.user)
        serializer = ContactSerializer(ingredients, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_retrieve_single_contact(self):  # Test retrieving a  contact
        request = factory.get('api/v1/contacts/', args=[self.contact_casper.id])
        force_authenticate(request, user=self.user)
        contact_list = ContactsViewset.as_view({'get': 'retrieve'})
        res = contact_list(request, pk=self.contact_casper.id)
        ingredients = Contact.objects.filter(user=self.user)
        serializer = ContactSerializer(ingredients, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_create_contact(self):  # Test creation of  contact
        request = factory.post('api/v1/contacts/', {'name': 'casper_test', 'email':'abc1d@email.com',
                                                    'phone_number':'1234567890', 'user_id': self.user.id},
                               format='json')
        force_authenticate(request, user=self.user)
        view = ContactsViewset.as_view({'post': 'create'})
        res = view(request)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_update_contact(self):  # Test update of  contact
        request = factory.patch('api/v1/contacts/{}'.format(self.contact_casper.id), {'name': 'casper_test_updated'}, format='json')
        force_authenticate(request, user=self.user)
        view = ContactsViewset.as_view({'patch': 'partial_update'})
        res = view(request, pk=self.contact_casper.id)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_delete_single_contact(self):  # Test retrieving a  contact
        request = factory.delete('api/v1/contacts/{}'.format(self.contact_casper.id))
        force_authenticate(request, user=self.user)
        contact_detail = ContactsViewset.as_view({'delete': 'destroy'})
        res = contact_detail(request, pk=self.contact_casper.id)
        self.assertEqual(status.HTTP_204_NO_CONTENT, res.status_code, "Should delete the list from database.")

    def test_search_contacts_list(self):  # Test retrieving a list of contacts
        request = factory.get('api/v1/contacts/?name={}'.format(self.contact_casper.id))
        force_authenticate(request, user=self.user)
        view = ContactsViewset.as_view({'get': 'search'})
        res = view(request)
        self.assertEqual(res.status_code, status.HTTP_200_OK)