from django.test import TestCase, Client


class ListMoviesTest(TestCase):
    """
    Test module for List Movies view
    """
    def setUp(self):
        self.base_url = 'http://0.0.0.0:8000/movies/'
        self.client = Client()

    def test_list_movies(self):
        """ Test list movies view """
        response = self.client.get(self.base_url)
        # Test success listing
        self.assertEqual(response.status_code, 200)
        # Test empty object in html
        # self.assertContains(response, "No movies available.")


class ListPeopleTest(TestCase):
    """
    Test module for List People view
    """
    def setUp(self):
        self.base_url = 'http://0.0.0.0:8000/movies/people/'
        self.client = Client()
    
    def test_list_people(self):
        """ Test list people view """
        response = self.client.get(self.base_url)
        # Test success listing
        self.assertEqual(response.status_code, 200)
        # Test empty object in html
        # self.assertContains(response, "No people available.")
