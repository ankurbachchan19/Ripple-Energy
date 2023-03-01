from django.urls import path, reverse, include, resolve
from django.test import SimpleTestCase
from api.views import SellerBidsPerCompetition, AllBidsListView, AllCompetitionsListView, AllSelllersListView, AllBuyersListView
from rest_framework.test import APITestCase, APIClient
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.views import APIView
from dotenv import dotenv_values

config = dotenv_values(".env")


class ApiUrlsTests(SimpleTestCase):

    def test_get_SellerBidsPerCompetition_is_resolved(self):
        url = reverse('api:SellerBidsPerCompetition')
        self.assertEquals(resolve(url).func.view_class,
                          SellerBidsPerCompetition)

    def test_get_AllBidsListView_is_resolved(self):
        url = reverse('api:AllBidsListView')
        self.assertEquals(resolve(url).func.view_class,
                          AllBidsListView)

    def test_get_AllCompetitionsListView_is_resolved(self):
        url = reverse('api:AllCompetitionsListView')
        self.assertEquals(resolve(url).func.view_class,
                          AllCompetitionsListView)

    def test_get_AllSelllersListView_is_resolved(self):
        url = reverse('api:AllSelllersListView')
        self.assertEquals(resolve(url).func.view_class,
                          AllSelllersListView)

    def test_get_AllBuyersListView_is_resolved(self):
        url = reverse('api:AllBuyersListView')
        self.assertEquals(resolve(url).func.view_class,
                          AllBuyersListView)


class SellerBidsPerCompetitionAPIViewTests(APITestCase):
    url = reverse("api:SellerBidsPerCompetition")

    def setUp(self):
        self.user = User.objects.create_user(
            username=config['USERNAME'], password=config['PASSWORD'])
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_get_api_authenticated(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_api_un_authenticated(self):
        self.client.force_authenticate(user=None, token=None)
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 401)


class AllBidsListViewAPIViewTests(APITestCase):
    url = reverse("api:AllBidsListView")

    def setUp(self):
        self.user = User.objects.create_user(
            username=config['USERNAME'], password=config['PASSWORD'])
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_get_api_authenticated(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_api_un_authenticated(self):
        self.client.force_authenticate(user=None, token=None)
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 401)


class AllCompetitionsListViewAPIViewTests(APITestCase):
    url = reverse("api:AllCompetitionsListView")

    def setUp(self):
        self.user = User.objects.create_user(
            username=config['USERNAME'], password=config['PASSWORD'])
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_get_api_authenticated(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_api_un_authenticated(self):
        self.client.force_authenticate(user=None, token=None)
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 401)


class AllSelllersListViewAPIViewTests(APITestCase):
    url = reverse("api:AllSelllersListView")

    def setUp(self):
        self.user = User.objects.create_user(
            username=config['USERNAME'], password=config['PASSWORD'])
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_get_api_authenticated(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_api_un_authenticated(self):
        self.client.force_authenticate(user=None, token=None)
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 401)


class AllBuyersListViewAPIViewTests(APITestCase):
    url = reverse("api:AllBuyersListView")

    def setUp(self):
        self.user = User.objects.create_user(
            username=config['USERNAME'], password=config['PASSWORD'])
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_get_api_authenticated(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_api_un_authenticated(self):
        self.client.force_authenticate(user=None, token=None)
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 401)
