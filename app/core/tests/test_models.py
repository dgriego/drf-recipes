from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models


# Create helper method for creating a user
def sample_user(email='dan@dan.com', password='12345'):
    """
    Create a sample user

    :param email: String
    :param password: String
    :return: User
    """
    return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """
        Test creating a new user when an email is successful
        """
        email = 'test@dan.com'
        password = '12345'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password, password)

    def test_new_user_email_normalized(self):
        """
        Test email for new user is normalized
        """
        email = 'test@LONDON.com'
        user = get_user_model().objects.create_user(email, '12345')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """
        Test creating user with no email raises error
        """
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, '12345')

    def test_create_new_superuser(self):
        """
        Test create a superuser
        """
        user = get_user_model().objects.create_superuser(
            'test@blah.com',
            '12345'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_tag_str(self):
        """
        Test the tag string representation
        """
        tag = models.Tag.objects.create(
            user=sample_user(),
            name='Vegan'
        )

        self.assertEqual(str(tag), tag.name)

    def test_ingredient_str(self):
        """
        Test the ingredient string representation
        """
        ingredient = models.Ingredient.objects.create(
            user=sample_user(),
            name='Cucumber'
        )

        self.assertEqual(str(ingredient), ingredient.name)

    def test_recipe_str(self):
        """
        Test the ingredient string representation
        """
        recipe = models.Recipe.objects.create(
            user=sample_user(),
            title='potato cakes',
            time_minutes=30,
            price=5.00
        )

        self.assertEqual(str(recipe), recipe.title)
