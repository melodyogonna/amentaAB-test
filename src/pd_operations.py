import pandas as pd

from src import api_calls


class DataHandler():

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

        return df
            
        

