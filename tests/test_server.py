# -*- coding: utf-8 -*-
"""
- `File`: test_server.py

- `Author`: Me

- `Email`: 0

- `Github`: 0

- `Description`: Unit tests for translation server script
"""


import unittest
import json
from translator import server


class TestSequenceFunctions(unittest.TestCase):
    """
    Testcases for translation server script

    Attribute:

    - `app`: Class::Flask

    An reference to the Flash application

    - `client`: Class::Flask.testing.FlaskClient

    An reference to the client instance. Testing calls rely on this instance

    """
    @classmethod
    def setUpClass(cls):
        # Customize configuration for testing
        server.config({
            'DEBUG': False,
            'SERVER_NAME': '0.0.0.0:8080',
            'TESTING': True,
        })

        # Save the reference for flask application
        cls.app = server.app

        # Set the client reference to none at first
        cls.client = None

    def setUp(self):
        # Setup client reference
        self.client = self.app.test_client()

    def test_translate_single_word(self):
        """
        It should able to translate single word, from one to ten, from english
        to chinese
        """
        input_words = [
            'zero',
            'one',
            'two',
            'three',
            'four',
            'five',
            'six',
            'seven',
            'eight',
            'nine',
            'ten',
        ]
        expect_outputs = [
            u'零',
            u'一',
            u'二',
            u'三',
            u'四',
            u'五',
            u'六',
            u'七',
            u'八',
            u'九',
            u'十',
        ]

        for index, word in enumerate(input_words):
            # print('word=%s' % word)
            ret = self.client.get('/?words=%s' % word)

            expect_output = expect_outputs[index]
            actual_data = json.loads(ret.data)
            actual_output = actual_data['output']
            actual_message = actual_data['message']
            self.assertEqual(u'OK', actual_message)
            self.assertEqual(expect_output, actual_output)

    def test_translate_multiple_word(self):
        """
        It should able to translate more than one words which separated by
        space
        """

        input_words = [
            'one two three four',
            'five six seven eight',
            'nine ten',
            'ten one two',
            'three seven six',
            'nine ten zero',
        ]

        expect_outputs = [
            u'一 二 三 四',
            u'五 六 七 八',
            u'九 十',
            u'十 一 二',
            u'三 七 六',
            u'九 十 零',
        ]

        for index, word in enumerate(input_words):
            # print('word=%s' % word)
            ret = self.client.get('/?words=%s' % word)

            expect_output = expect_outputs[index]
            actual_data = json.loads(ret.data)
            actual_output = actual_data['output']
            actual_message = actual_data['message']
            self.assertEqual(u'OK', actual_message)
            self.assertEqual(expect_output, actual_output)

    def test_do_not_set_words_query(self):
        """
        It should set output be empty string and message be missing words
        query string
        """
        ret = self.client.get('/')

        actual_data = json.loads(ret.data)
        actual_output = actual_data['output']
        actual_message = actual_data['message']
        self.assertEqual(u'Missing "words" query string', actual_message)
        self.assertEqual(0, len(actual_output))

    def test_translate_error(self):
        """
        It should return message about translation error if given word other
        than one to ten
        """
        ret = self.client.get('/?words=a')

        actual_data = json.loads(ret.data)
        actual_output = actual_data['output']
        actual_message = actual_data['message']
        self.assertEqual(u'Translation error for word |a|', actual_message)
        self.assertEqual(0, len(actual_output))
