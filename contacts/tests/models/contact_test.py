from django.test import TestCase
from contacts.models import Contact
from django.contrib.auth.models import User
class ContactTest(TestCase):
    """ Test module for Contact model """

    def setUp(self):
        user = User.objects.create(username='test3')
        Contact.objects.create(
            name='Casper', email='abcd@email.com', phone_number='1234567890',  user_id=user.id)
        Contact.objects.create(
            name='Muffin', email='abcd@email.com', phone_number='1234567890', user_id=user.id)

    def test_puppy_breed(self):
        contact_casper = Contact.objects.get(name='Casper')
        contact_muffin = Contact.objects.get(name='Muffin')
        self.assertEqual(contact_casper.name, "Casper")
        self.assertEqual(contact_muffin.name, "Muffin")
