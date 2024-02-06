from django.test import TestCase
from django.urls import reverse
from rest_framework import status


class RequestAPIViewTest(TestCase):

    def test_create(self):
        response = self.client.post(
            reverse('main:request_fulfillment'),
            data={
                "cadastral_number": "78:36:7784467:6666",
                "latitude": 27.12,
                "longitude": 46.15,
            }
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json(), {
            "id": 6,
            "cadastral_number": "78:36:7784467:6666",
            "latitude": "27.12",
            "longitude": "46.15",
        })


class AnswerAPIViewTest(TestCase):

    def setUp(self):
        self.response = self.client.post(
            reverse('main:request_fulfillment'),
            data={
                "cadastral_number": "78:36:7784467:6666",
                "latitude": 27.12,
                "longitude": 46.15,
            }
        )

    def test_get(self):
        response = self.client.get(
            reverse('main:result_receipt', args=[self.response.json()['id']])
        )

        resp_json = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(resp_json.get('id'), self.response.json()['id'])
        self.assertEqual(tuple(resp_json.keys()),
                         ('id', 'answer', 'cadastral_number', 'latitude', 'longitude'))


class HistoryAPIViewTest(TestCase):

    def setUp(self):
        self.response_1 = self.client.post(
            reverse('main:request_fulfillment'),
            data={
                "cadastral_number": "78:36:7784467:6666",
                "latitude": 27.12,
                "longitude": 46.15,
            }
        )

        self.response_2 = self.client.post(
            reverse('main:request_fulfillment'),
            data={
                "cadastral_number": "78:36:7784467:5555",
                "latitude": 25.12,
                "longitude": 46.01,
            }
        )

    def test_get(self):
        response = self.client.get(
            reverse('main:history_receipt')
        )

        resp_json = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(resp_json), 2)
        self.assertEqual(resp_json[0]['id'], self.response_1.json()['id'])
        self.assertEqual(resp_json[1]['id'], self.response_2.json()['id'])

    def test_get_with_filter(self):
        response = self.client.get(
            reverse('main:history_receipt') + '?search=78:36:7784467:6666'
        )

        resp_json = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(resp_json), 1)
        self.assertEqual(resp_json[0]["id"], self.response_1.json()['id'])
