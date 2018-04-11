import unittest

from sql_sanitizer import is_string_sanitized
from sql_sanitizer import is_array_sanitized
from sql_sanitizer import is_map_sanitized
from sql_sanitizer import is_sanitized

class StringSanitizerTest(unittest.TestCase):
    def test_is_string_sanitized_throws_exception_if_it_is_not(self):
        str='i\'nvalid_str;ing"'
        with self.assertRaisesRegexp(Exception,
                                     "Input contains un sanitized characters"):
            is_string_sanitized(str)

    def test_is_string_sanitized_returns_if_it_is_not(self):
        str='valid_string.'
        is_string_sanitized(str)

class ArraySanitizerTest(unittest.TestCase):
    def test_is_array_sanitized_throws_exception_if_it_is_not(self):
        arr=['i\'nvalid_str;ing"', 'another string which we don t care']
        with self.assertRaisesRegexp(Exception,
                                     "Input contains un sanitized characters"):
            is_array_sanitized(arr)

    def test_is_array_sanitized_returns_if_it_is(self):
        arr=['valid string', 'another.valid_string']
        is_array_sanitized(arr)

class DictSanitizerTest(unittest.TestCase):
    def test_is_map_sanitized_throws_exception_if_it_is_not(self):
        data={'key': 'invalid"value;'}
        with self.assertRaisesRegexp(Exception,
                                     "Input contains un sanitized characters"):
            is_map_sanitized(data)

    def test_is_map_sanitized_returns_if_it_is(self):
        data={'key': 'valid value', 'key1': 'another valid value'}
        is_map_sanitized(data)

class SanitizerTest(unittest.TestCase):
    def test_throws_exception_if_input_contains_invalid_characters(self):
        data=[{'source_key': 'test;drop tables;', 'target_key': 'another; drop table;',
               'values': [{'from': 'a', 'to': 'b'}]}]
        with self.assertRaisesRegexp(Exception,
                                     "Input contains un sanitized characters"):
            is_sanitized(data)

    def test_returns_if_input_contains_invalid_characters(self):
        data=[{'source_key': 'table1', 'target_key': 'table2',
               'values': [{'from': 'a', 'to': 'b'}]}]
        is_sanitized(data)

