"Unit tests for the dictionary module's Dict class."

from dictionary import Dict
import unittest		# TL;DR

class TestDictionaryFunctions(unittest.TestCase):

	def test_basic(self):
		d = Dict()
		d['davin'] = 'green'
		d['gabriel'] = 'purple'
		d['mara'] = 'pink'
		self.assertEqual(d['davin'], 'green')
		self.assertEqual(d['gabriel'], 'purple')
		self.assertEqual(d['mara'], 'pink')
		
if __name__ == '__main__':
	unittest.main(exit=False)
