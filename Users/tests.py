from django.test import TestCase

# Create your tests here.
from .models import User

class UserTestCase(TestCase):
    def setUp(self): #allows you to create entries in test database
        for i in range(0,3):
            User.objects.create(first_name="Test", last_name="Test", phone_number="12345789", email="Test@Test", role="Admin")
    def test_queryset_exists(self): #tests to see if the db is empty
        query_set = User.objects.all()
        self.assertTrue(query_set)
    def test_queryset_count(self):
        qs = User.objects.all()
        self.assertEqual(query_set.count(),3)
    def test_queryset_edit(self): #tests for user update functionality
        test_user = User.objects.get(id=1)
        User.objects.filter(id=1).update(first_name="First", last_name="Last", phone_number="98754321", email="test@test", role="Regular")
        self.assertEqual(test_user, User.objects.get(id=1))
    def test_queryset_delete(self): #tests for user delete
        User.objects.filter(id=2).delete()
        self.assertFalse(User.objects.get(id=1).exists())