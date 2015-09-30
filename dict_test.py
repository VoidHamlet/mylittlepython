"Unit tests for the dictionary module's Dict class."

from dictionary import Dict
import unittest   # TL;DR


class TestDictionaryFunctions(unittest.TestCase):

    def test_basic(self):
        d = Dict()
        d['davin'] = 'green'
        d['gabriel'] = 'purple'
        d['mara'] = 'pink'
        self.assertEqual(d['davin'], 'green')
        self.assertEqual(d['gabriel'], 'purple')
        self.assertEqual(d['mara'], 'pink')

    def test_delete(self):
        d = Dict()
        d['davin'] = 'green'
        d['gabriel'] = 'purple'
        d['kanai'] = 'silver'
        del d['davin']
        with self.assertRaises(KeyError):
            d['davin']

    def test_update_value_for_an_existing_key(self):
        d = Dict()
        d['davin'] = 'green'
        d['gabriel'] = 'purple'
        d['kanai'] = 'silver'
        d['davin'] = 'blue'
        self.assertEqual(d['davin'], 'blue')

    def test_use_in_a_for_loop(self):
        d = Dict()
        d['davin'] = 'green'
        d['gabriel'] = 'purple'
        d['mara'] = 'pink'
        for key in d:
            pass

    def test_delete_something_not_there(self):
        d = Dict()
        d['davin'] = 'green'
        d['gabriel'] = 'purple'
        d['mara'] = 'pink'
        with self.assertRaises(KeyError):
            del d['kanai']
			
    def test_keys(self):
        d = Dict()
        d['davin'] = 'green'
        d['gabriel'] = 'purple'
        d['mara'] = 'pink'
        d['kanai'] = 'silver'
        self.assertEqual(sorted(d.keys()),
                         sorted(['davin', 'gabriel', 'mara', 'kanai']))



if __name__ == '__main__':
    unittest.main(exit=False)