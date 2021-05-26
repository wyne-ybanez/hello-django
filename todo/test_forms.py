from django.test import TestCase
from .forms import ItemForm


class TestItemForm(TestCase):

    def test_item_name_is_required(self):
        self.assertEqual(1, 1)

    def test_this_thing_works2(self):
        self.assertEqual(1, 3)
    
    def test_this_thing_works3(self):
        self.assertEqual(1, )

    def test_this_thing_works4(self):
        self.assertEqual(1, 4)