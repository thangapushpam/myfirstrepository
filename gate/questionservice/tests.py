from django.test import TestCase
from myapp.models import Count

class MyTests(TestCase):
	    def setUp(self):
	    	Count.objects.create(count=1, score_value=1)

        def test_forms(self):
            response = self.client.get("/questionservice/login/")
            self.assertEqual(response.status_code, 200)

        def test_admin(self):
            response = self.client.get("/questionservice/view_adminpage/")
            self.assertEqual(response.status_code, 200)
        
        def test_student(self):
        	response = self.client.get("/questionservice/view_studentpage/")
            self.assertEqual(response.status_code, 200)

        '''def test_call_view_fails_blank(self):
            self.client.login(username='user', password='test')
            response = self.client.post(('/url/to/view'), {}) # blank data dictionary
            self.assertFormError(response, 'form', 'some_field', 'This field is required.')'''