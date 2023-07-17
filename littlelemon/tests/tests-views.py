from django.test import TestCase
import restaurant.models as models
import restaurant.serializers as serializers

class MenuViewTest(TestCase):

    def setUp(self):
        models.Menu.objects.create(title="IceCream", price=80, inventory=100)
        models.Menu.objects.create(title="Pizza", price=25, inventory=250)

    def test_getall(self): 
        menu_items = models.Menu.objects.all()
        serialized_obj = serializers.MenuSerializer(menu_items, many=True)
        self.assertEqual(serialized_obj.data, {"IceCream : 80"})
