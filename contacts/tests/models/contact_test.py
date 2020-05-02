from django.test import TestCase
from contacts.models import Contact
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class ContactTest(TestCase):
    """ Test module for Contact model """

    def setUp(self):
        user = User.objects.create(username='test3')
        Contact.objects.create(
            name='Casper', email='abcd@email.com', phone_number='1234567890',  user_id=user.id)
        Contact.objects.create(
            name='Muffin', email='abcdp@email.com', phone_number='1234567890', user_id=user.id)

    def test_contact_creation(self):
        user = User.objects.get(username='test3')
        contact_test = Contact(name='Muffin_test', email='Muffin_test@email.com', phone_number='1234567890', user_id=user.id)
        self.assertEqual(contact_test.name, "Muffin_test")
        self.assertEqual(contact_test.email, "Muffin_test@email.com")
        self.assertEqual(contact_test.user_id, user.id)


