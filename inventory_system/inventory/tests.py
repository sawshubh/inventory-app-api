from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Item


class ItemTests(APITestCase):

    def setUp(self):
        """Test settting up item data"""
        self.item_data = {
            'name': 'Test Item',
            'description': 'Test description',
            'quantity': 5
        }
        self.item = Item.objects.create(**self.item_data)

    def test_create_item(self):
        """Test create item"""
        url = reverse('item-list-create')
        data = {
            'name': 'New Item',
            'description': 'New description',
            'quantity': 10
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_read_item(self):
        """Test read item"""
        url = reverse('item-detail', args=[self.item.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.item_data['name'])

    def test_update_item(self):
        """Test update item"""
        url = reverse('item-detail', args=[self.item.id])
        updated_data = {
            'name': 'Updated Item',
            'description': 'Updated description',
            'quantity': 15
        }
        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], updated_data['name'])

    def test_delete_item(self):
        """Test delete item"""
        url = reverse('item-detail', args=[self.item.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
