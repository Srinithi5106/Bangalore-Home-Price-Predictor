import pickle
import json
import numpy as np
import os

__locations = None
__data_columns = None
__model = None

def get_estimated_price(location, sqft, bhk, bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1
    else:
        print(f"[WARN] Location '{location}' not found.")

    return round(__model.predict([x])[0], 2)

def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __data_columns
    global __locations
    global __model

    artifacts_path = os.path.join(os.path.dirname(__file__), 'artifacts')

    with open(os.path.join(artifacts_path, "columns.json"), "r") as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]  # first 3: sqft, bath, bhk

    if __model is None:
        with open(os.path.join(artifacts_path, 'banglore_home_prices_model.pickle'), 'rb') as f:
            __model = pickle.load(f)

    print("loading saved artifacts...done")

def get_location_names():
    return __locations

def get_data_columns():
    return __data_columns

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_estimated_price('1st Phase JP Nagar', 1000, 3, 3))
