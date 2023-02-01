import unittest
from unittest import TestCase
from functions_magic import *


class TestMagic(TestCase):

    def test_expected_url(self):
        question = 'Will Arsenal win the league?'
        returned_url = f'https://magic-eight-ball.azurewebsites.net/magic/JSON/{question}'
        self.assertEqual(returned_url, generate_url_for_question(question))

    def test_expected_answer(self):
        expected_response = {
            'question': 'Will it be sunny tomorrow?',
            'answer': 'Yes',
            'type': 'Affirmative'
        }
        expected_answer = expected_response['answer']
        self.assertEqual(expected_answer, extract_answer_from_response(expected_response))

    def test_unexpected_answer(self):

        # testing for unexpected key names
        unexpected_response = {
            'Your q': 'Will it be sunny tomorrow?',
            'My ansy wansy': 'Yes',
            'type': 'Affirmative'
        }
        expected_answer = None
        self.assertEqual(expected_answer, extract_answer_from_response(unexpected_response))


if __name__ == '__main__':
    unittest.main()
""" TODO create a test case to test each of the following functions,
generate_url_for_question
 - check that the expected URL is returned for an example question. 
 
extract_answer_from_response
 - one test should create some example dictionaries that match the expected response from the API,
 and check that the correct answer is extracted and returned.
 - another test should create example dictionaries with a different structure to the one returned from the API, 
 and check that the function returns None. 

 
 TODO to think about - what else could you test about this program? 
 What types of expected and unexpected behavior might happen? You may be able to write tests for some 
 of your ideas now. We'll talk about ways to test other aspects of this program in class.

"""
