from django.test import TestCase
import restaurant.models as models

class MenuItemTest(TestCase):

    def test_get_item(self):
        item = models.Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(item, "IceCream : 80")

