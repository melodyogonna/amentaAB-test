import unittest

from src.main import return_dataframes

class TestingMainEntryPoint(unittest.TestCase):
    def test_df_object(self):
        print(return_dataframes())
        self.assertEqual(True, return_dataframes())

