import io
import unittest
from pytest import MonkeyPatch
import final
import requests
from unittest.mock import patch

class TestMapQuest(unittest.TestCase):
    def test_app(self):
        self.assertEqual(final.json_status, 0)

    def test_api(self):
        self.assertEqual(final.main_api, "https://www.mapquestapi.com/directions/v2/route?")

    def test_api(self):
        self.assertIsNotNone(final.key, None)
    
    def test_input(self):
        MonkeyPatch.setattr('sys.stdin', io.StringIO('Malolos, Bulacan'))
       

if __name__ == '__main__':
    unittest.main()

#if we run this directly run the code within that conidition 