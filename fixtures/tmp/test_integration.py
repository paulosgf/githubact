#!/usr/bin/env python3

import unittest
import json

class TestComplexData(unittest.TestCase):
    def setUp(self):
        with open('fixtures/test_complex.json', 'r') as myfile:
            data = json.load(myfile)
        for self.clientname in data["customer"]:
            if self.clientname["id"] == 9999:
                self.clienttest = self.clientname
        return self.clienttest

    def test_existence_of_custome(self):
        self.assertEqual(self.clienttest["name"], u"バナナ")
        self.assertEqual(self.clienttest["address"], "1 Red Road, Akihabara, Tokyo")

if __name__ == '__main__':
    unittest.main()
