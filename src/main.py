from src import api_calls
from src.pd_operations import DataHandler
from src.utils import helpers

dataHandler = DataHandler()
fortnoxHandler = api_calls.FortNoxRequestHandler()

articles = fortnoxHandler.get_all_articles()
articles_df = dataHandler.create_df(articles.get('Customers', {}))
filter_df = dataHandler.update_quantiy(dataHandler.filter_df(articles_df, helpers.filter_for_articles))



