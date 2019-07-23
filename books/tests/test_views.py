from django.shortcuts import reverse
from django.test import TestCase

from books.models import Author


class TestAuthorListView(TestCase):

    PAGINATION = 10
    NUM_TEST_AUTHORS = 15

    @classmethod
    def setUpTestData(cls):
        # Create 15 authors for pagination test

        for i in range(cls.NUM_TEST_AUTHORS):
            Author.objects.create(given_name=f"Author {i}", last_name=f"Surname {i}")

    def test_view_exists_at_desired_location(self):
        response = self.client.get("/books/authors/")
        self.assertEqual(response.status_code, 200)

    def test_view_accessible_by_name(self):
        response = self.client.get(reverse("author-list"))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse("author-list"))
        self.assertTemplateUsed(response, "books/author_list.html")

    def test_pagination_is_correct(self):
        response = self.client.get(reverse("author-list"))
        self.assertIn("is_paginated", response.context)
        self.assertEqual(len(response.context["author_list"]), self.PAGINATION)

    def test_lists_all_authors(self):
        response = self.client.get(reverse("author-list")+"?page=2")
        self.assertEqual(len(response.context["author_list"]),
                         self.NUM_TEST_AUTHORS - self.PAGINATION)
