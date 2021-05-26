from django.test import TestCase


class TestViews(TestCase):

    def test_get_todo_list(self):
        """ 
        Getting client response for home page.
        Ensure it's status 200, a successful response.
        Tell it what template we expect to be used in response.
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/todo_list.html')
    
    # def test_get_add_item_page(self):

    # def test_get_edit_item_page(self):

    # def test_can_add_item(self):

    # def test_can_delete_item(self):

    # def test_can_toggle_item(self):
