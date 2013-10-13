"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.http import HttpRequest
from django.core.urlresolvers import resolve

from lists.views import home_page

class SimpleTest(TestCase):
    def test_basic_addition(self):
      request = HttpRequest()
      response = home_page(request);
      self.assertTrue(response.content.startswith(b'<html>')) #3
      self.assertIn(b'<title>To-Do lists</title>', response.content) #4
      self.assertTrue(response.content.endswith(b'</html>')) #3
