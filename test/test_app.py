import unittest
import final
import requests

class TestMapQuest(unittest.TestCase):
    def test_app(self):
        self.assertEqual(final.json_status, 0)

    def test_api(self):
        self.assertEqual(final.main_api, "https://www.mapquestapi.com/directions/v2/route?")

    def test_api(self):
        self.assertIsNotNone(final.key, None)
       

if __name__ == '__main__':
    unittest.main()

#if we run this directly run the code within that conidition 