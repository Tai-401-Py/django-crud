from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Snack


class SnackTests(TestCase):
    
    # CREATE A TEST USER FOR TESTING 
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="tester", email="tester@email.com", password="pass"
        )

        self.snack = Snack.objects.create(
            name="Twinkie", description=1, purchaser=self.user,
        )

    def test_string_representation(self):
        '''
        # Testing __str__ functionality
        '''
        self.assertEqual(str(self.snack), "Twinkie")

    def test_snack_content(self):
        '''
        # Asserting that the fields we want do exist and were populated from the setup properly. 
        '''
        self.assertEqual(f"{self.snack.name}", "Twinkie")
        self.assertEqual(f"{self.snack.purchaser}", "tester")
        self.assertEqual(self.snack.description, 1)

    def test_snack_list_view(self):
        '''
        Asserting that you can recieve and access page and that it contains the data from setup.
        '''
        response = self.client.get(reverse("snack_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Twinkie")
        self.assertTemplateUsed(response, "snack_list.html")

    def test_snack_detail_view(self):
        '''
        checking improper route and that you can use a pk to acess snack_details (in this case twinkie), make sure it has the right information as well as using the proper template 
        '''
        response = self.client.get(reverse("snack_detail", args="1"))
        no_response = self.client.get("/100000/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "Purchaser: tester")
        self.assertTemplateUsed(response, "snack_detail.html")

    def test_snack_create_view(self):
        '''
        Testing an attempt to create a new instance of snack, as well as check that the detail page at the proper pk does contain the info used to create.
        '''
        response = self.client.post(
            reverse("snack_create"),
            {
                "name": "Banana",
                "description": "Details about a banana",
                "purchaser": self.user.id,
            }, follow=True
        )

        self.assertRedirects(response, reverse("snack_detail", args="2"))
        self.assertContains(response, "Details about a banana")



    def test_snack_update_view_redirect(self):
        '''
        Check that updating will in fact update properly to contain information provided.
        '''
        response = self.client.post(
            reverse("snack_update", args="1"),
            {"name": "Updated name","description":"3","purchaser":self.user.id}
        )

        self.assertRedirects(response, reverse("snack_detail", args="1"))

    def test_snack_delete_view(self):
        '''
        checking taht you can access the delete page. 
        '''
        response = self.client.get(reverse("snack_delete", args="1"))
        self.assertEqual(response.status_code, 200)