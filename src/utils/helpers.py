import pandas as pd

def filter_for_articles(frame_object:pd.Series):
    return (frame_object.Active == True and
            frame_object.Description.contains(["A", "K", "M", "C"]) and
            frame_object.QuantityInStock > 20)
