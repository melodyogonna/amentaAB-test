import pandas as pd

from src import api_calls


class DataHandler():
    def __init__(self):
        self.api_handler = api_calls.FortNoxRequestHandler()

    def create_df(self, frame_object) -> pd.DataFrame:
        '''Create a data frame from a given frame object'''
        return pd.DataFrame(frame_object)
    
    def filter_df(self, df:pd.DataFrame, fiter_function) -> pd.DataFrame:
        '''Run a filter function through the pandas data frame'''
        return df.filter(fiter_function)

    def update_quantiy(self, df:pd.DataFrame) -> pd.DataFrame:
        '''Iterate through a dataframe and update the quantity'''
        for index, row in df.iterrows():
            row.update({'Quantity': 340})
            self.api_handler.update_article(row)

        return df

    def create_new_article_from_df(self, df):
        ''' Iterate through the dataframe and create new articles from the
        series
        '''
        for index, row in df.iterrows():
            row.update({'Quantity':50, 'Description': row.Description + 'TEST'})
            self.api_handler.create_article(row)

        return df

    def update_customers(self, df):
        '''Update email of every customer'''
        for index, row in df.iterrows():
            row.update({'Email': 'testing555@hotmail.com'})
        return df


            
        

