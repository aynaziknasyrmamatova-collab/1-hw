from django.contrib import admin
from django.test import TestCase

from .admin import CustomUserAdmin
from .models import CustomUser


class CustomUserTests(TestCase):
    def test_profile_fields_and_default_role(self):
        user = CustomUser.objects.create_user(
            email="client@example.com",
            username="client",
            password="test-password",
        )

        self.assertEqual(user.role, CustomUser.Role.CLIENT)
        self.assertFalse(user.is_verified)
        self.assertEqual(user.bio, "")
        self.assertIsNone(user.birth_date)

    def test_email_is_login_field(self):
        self.assertEqual(CustomUser.USERNAME_FIELD, "email")


class CustomUserAdminTests(TestCase):
    def test_homepage_redirects_to_admin(self):
        response = self.client.get("/")

        self.assertRedirects(response, "/admin/", fetch_redirect_response=False)

    def test_admin_configuration(self):
        model_admin = CustomUserAdmin(CustomUser, admin.site)

        self.assertEqual(
            model_admin.list_display,
            ("email", "role", "is_verified", "is_active"),
        )
        self.assertEqual(model_admin.list_filter, ("role", "is_verified"))
        self.assertEqual(model_admin.search_fields, ("email", "username"))
        configured_fields = {
            field
            for _, options in model_admin.fieldsets
            for field in options["fields"]
        }
        self.assertTrue({"bio", "birth_date", "is_verified"} <= configured_fields)
