from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_uer_with_email_successful(self):
        """
        Test creating new user
        """
        email = 'test@whatever.com'
        password = '123'
        user = get_user_model().objects.create_user(
            email=email, password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalised(self):
        """
        Test email of a new user is normalised
        """

        email = "ttttest@TESTDOMAIN.COM"
        user = get_user_model().objects.create_user(
            email, '1234'
        )

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """
        Test invalid email raises error
        """

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, '123')

    def test_create_new_superuser(self):
        """
        Test creating a superuser
        """

        user = get_user_model().objects.create_superuser(
            'test@whatever.com', '12345'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
