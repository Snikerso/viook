from django.test import TestCase, Client
from rest_framework.test import APIRequestFactory
import json

class TestWordListApiView(TestCase):

    def setUp(self):
        self.client = Client()


    def test_get_books_list_without_any_filtrations(self):
        # Prepare
        url = "/books/"
        data = {"q":"war"}
        self.client.post('/db/', json.dumps(data), content_type='application/json')

        # Make
        response = self.client.get(url)

        # Check
        assert response.status_code == 200

    def test_get_sorted_books_list_by_published_date_descending(self):
        # Prepare
        url = "/books/?sort=-published_date"
        data = {"q":"war"}
        self.client.post('/db/', json.dumps(data), content_type='application/json')

        # Make
        response = self.client.get(url)
        first = int(response.data[1].get("published_date"))
        second = int(response.data[2].get("published_date"))

        # Check
        assert first >= second

    def test_sorted_books_by_published_date(self):
        # Prepare
        url = "/books/?published_date=1991"
        data = {"q":"war"}
        self.client.post('/db/', json.dumps(data), content_type='application/json')

        # Make
        response = self.client.get(url)
        published_date = int(response.data[0].get("published_date"))

        # Check
        assert published_date == 1991

    def test_filter_books_by_authors_names(self):
        # Prepare
        url = "/books/?author=United%20States.%20Committee"
        body = {"q":"war"}
        self.client.post('/db/', json.dumps(body), content_type='application/json')

        # Make
        response = self.client.get(url)
        author_data = response.data[0].get("authors")[0]
        print(author_data)

        # Check
        assert author_data.find("United States. Committee") == 0


    def test_post_books_to_database(self):
        # Prepare
        data = {"q":"war"}
        
        # Make
        response = self.client.post('/db/', json.dumps(data), content_type='application/json')

        # Check
        assert response.status_code == 201

    def test_post_books_to_database_where_without_any_books(self):
        # Prepare
        data = {"q":"Nielnjknjkniil"}
        
        # Make
        response = self.client.post('/db/', json.dumps(data), content_type='application/json')

        # Check
        assert response.status_code == 400


