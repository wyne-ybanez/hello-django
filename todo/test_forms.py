from django.test import TestCase
from .forms import ItemForm


class TestItemForm(TestCase):

    def test_item_name_is_required(self):
        form = ItemForm({'name': ''})

        # Name should no be valid when empty
        self.assertFalse(form.is_valid())

        # If assert is false, send back dictionary of fields and error messages
        # Check for name key
        self.assertIn('name', form.errors.keys())

        # Assert equal to check whether the error message on the name field is 'this field is required'.
        # Using zero index because we only want first item in our list of errors
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_done_field_is_not_required(self):
        form = ItemForm({'name': 'Test Todo Item'})
        self.assertTrue(form.is_valid())

    # Fields are defined in forms.py
    def test_fields_are_explicit_in_form_metaclass(self):
        """
        Ensuring fields are defined explicitly.
        Won't accidentally display information we don't want it to.
        Stops reordering of fields.
        """
        form = ItemForm()
        self.assertEqual(form.Meta.fields, ['name', 'done'])


