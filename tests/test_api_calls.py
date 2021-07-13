import unittest

from src import api_calls

fortnoxHandler = api_calls.FortNoxRequestHandler()

class TestApiCalls(unittest.TestCase):
    def test_customer_retrieval(self):
        customers = fortnoxHandler.get_customers()
        print(customers)
        self.assertEqual(customers, True)



if __name__ == '__main__':
    unittest.main()
