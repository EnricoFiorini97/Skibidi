from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User
from backend.models import Kind


class TestLogin(TestCase):   
    def test__can_user_login(self):
        User.objects.create_user(username="test", password="test")
        self.assertTrue(Client().login(username="test", password="test"))

    def test_wrong_username_login(self):
        User.objects.create_user(username="test", password="test")
        self.assertFalse(Client().login(username="test1", password="test"))
 
    def test_wrong_password_login(self):
        User.objects.create_user(username="test", password="test")
        self.assertFalse(Client().login(username="test", password="test1"))

class TestListAPIViews(TestCase):
    def test__can_backend_protect_all_kind_api_view_to_not_staff_user(self):
        User.objects.create_user(username="test", password="test")
        c = Client()
        c.login(username="test", password="test")
        url = "/backend/search/serializers/kind/all/"
        response = c.get(url)
        self.assertEqual(response.status_code, 403)

    def test__can_backend_protect_all_kind_api_view_to_anonymous_user(self):
        c = Client()
        url = "/backend/search/serializers/kind/all/"
        response = c.get(url)
        self.assertEqual(response.status_code, 401)

    def test__can_backend_protect_all_kind_api_view_to_staff_user(self):
        User.objects.create_user(username="test", password="test", is_staff=True)
        c = Client()
        c.login(username="test", password="test")
        url = "/backend/search/serializers/kind/all/"
        response = c.get(url)
        self.assertEqual(response.status_code, 200)

class TestCreateViews(TestCase):
    def test__can_create_kind(self):
        User.objects.create_user(username="test", password="test", is_staff=True)
        c = Client()
        c.login(username="test", password="test")
        url = "/backend/create/kind/"
        c.post(url, {'kind_name':"Test Kind Name"})
        self.assertEqual(Kind.objects.last().kind_name, "Test Kind Name")

class TestUpdateViews(TestCase):
    def test__can_update_kind(self):
        User.objects.create_user(username="test", password="test", is_staff=True)
        c = Client()
        c.login(username="test", password="test")
        url = "/backend/create/kind/"
        c.post(url, {'kind_name':"Test Kind Name"})
        update_url = f"/backend/update/kind/{Kind.objects.last().kind_id}/"
        c.post(update_url, {'kind_name':"Test Kind Name Update"})
        self.assertEqual(Kind.objects.last().kind_name, "Test Kind Name Update")

class TestUpdateViews(TestCase):
    def test__can_update_kind(self):
        User.objects.create_user(username="test", password="test", is_staff=True)
        c = Client()
        c.login(username="test", password="test")
        url = "/backend/create/kind/"
        c.post(url, {'kind_name':"Test Kind Name"})
        delete_url = f"/backend/delete/kind/{Kind.objects.last().kind_id}/"
        c.post(delete_url)
        self.assertFalse(Kind.objects.filter(kind_name="Test Kind Name").exists())
