import unittest
from unittest.mock import MagicMock

from src import api_calls

fortnoxHandler = api_calls.FortNoxRequestHandler()

class TestApiCalls(unittest.TestCase):
    def test_customer_retrieval(self):
        mock_value = [{'item':1}]
        fortnoxHandler.get_customers = MagicMock(return_value=mock_value)
        customers = fortnoxHandler.get_customers(pages=3)
        fortnoxHandler.get_customers.assert_called()



if __name__ == '__main__':
    unittest.main()
