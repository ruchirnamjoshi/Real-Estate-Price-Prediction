import pickle
import json
import numpy as np

_data_columns = None
_model = None

def get_predicted_price(bhk,sqft,bath,balcony,ar_type,ap_type,location):
    input = np.zeros(len(_data_columns))
    input[0] = bhk
    input[1] = sqft
    input[2] = bath
    input[3] = balcony

    bal = _data_columns.index(ar_type.lower())
    input[bal] = 1

    apt = _data_columns.index(ap_type.lower())
    input[apt] = 1

    loc = _data_columns.index(location.lower())
    input[loc] = 1

    return _model.predict([input])[0][0]

def load_artifacts():
    global _data_columns
    global _model
    
    print('Loading Artifacts...')

    with open('C:/Users/ruchi/Desktop/Data Science Projects/Real-estate price prediction/columns.json','r') as f:
        _data_columns = json.load(f)['data_columns']

    with open('./real_estate.pickle','rb') as f:
        _model = pickle.load(f)

    print('Artifacts...Loaded')


def column_names():
    return _data_columns
    

load_artifacts()
# print(get_predicted_price(2,1340,2,2,'Carpet Area','Under Construction','whitefield'))
# print(column_names())