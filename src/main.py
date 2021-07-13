from src import api_calls
from src.pd_operations import DataHandler
from src.utils import helpers

dataHandler = DataHandler()
fortnoxHandler = api_calls.FortNoxRequestHandler()

articles = fortnoxHandler.get_all_articles()
articles_df = dataHandler.create_df(articles)
filter_df = dataHandler.update_quantiy(dataHandler.filter_df(articles_df, helpers.filter_for_articles))
new_articles = dataHandler.create_new_article_from_df(filter_df)

customers = fortnoxHandler.get_customers()
customer_df = dataHandler.create_df(customers)

save_customers = dataHandler.save_to_excel(customer_df[['CustomerNumber','Name', 'Email']], 'customers_names.xlsx', sheet_name='sheet1')
updated_customer_df = dataHandler.update_customers(customer_df)

def return_dataframes():
    return {
            'articles_df': articles_df, 'filter_df':filter_df,
            'customer_df':customer_df
            }

