from django.test import TestCase
from .models import Item


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
    
    def test_get_add_item_page(self):
        """ 
        Test add Item URL response.
        """
        response = self.client.get('/add')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/add_item.html')

    def test_get_edit_item_page(self):
        """
        Test Edit item.
        Create Item object as sample and generate URL reponse to edit item.
        Check for URL response if successful.
        """
        item = Item.objects.create(name='Test Todo Item')
        response = self.client.get(f'/edit/{item.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/edit_item.html')

    def test_can_add_item(self):
        """ 
        Test adding an item.
        Check post response via key and value.
        """
        response = self.client.post('/add', {'name': 'Test Added Item'})
        self.assertRedirects(response, '/')

    def test_can_delete_item(self):
        """ 
        Test deleting an item.
        Create item object as sample.
        Get URL and item ID in response.
        """
        item = Item.objects.create(name='Test Todo Item')
        response = self.client.get(f'/delete/{item.id}')
        self.assertRedirects(response, '/')

        # Variable to contain deleted item
        # Check if deleted by testing if len of 'existing items' is 0
        existing_items = Item.objects.filter(id=item.id)
        self.assertEqual(len(existing_items), 0)

    def test_can_toggle_item(self):
        """
        Checking Toggling functionality.
        Check done status of True.
        Call Toggle URL on its ID.
        Get Updated Item through its item ID.
        Assert False to check its done status.
        """
        item = Item.objects.create(name='Test Todo Item', done=True)
        response = self.client.get(f'/toggle/{item.id}')
        self.assertRedirects(response, '/')
        updated_item = Item.objects.get(id=item.id)
        self.assertFalse(updated_item.done)

