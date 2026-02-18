"""import pandas as pd
from tensorflow.keras.models import load_model
import numpy as np
import joblib

def predict():
    pred=ds.predict(d)
    ds=joblib.load("ML/svm_model.sav")
    df1=pd.read_csv("media/input/test/test.csv")
    df1
    d=df1.iloc[:,1:-1]
    pred=ds.predict(d)
    pred[0]
    if pred[0]==0:
            out='ANTIVIRUS BASED MALWARE  NOT DETECTED'
    elif pred[0]==1:
            out='ANTIVIRUS BASED MALWARE  DETECTED'
    return out"""

import pandas as pd 
import numpy as np
import joblib

def predict():
    # Load the model
    ds = joblib.load("ML/svm_model.sav")

    # Read the data
    df1 = pd.read_csv("media/input/test/test.csv")
    d = df1.iloc[:, 1:-1]

    # Make predictions
    pred = ds.predict(d)
    pred_value = pred[0]

    # Determine the result based on prediction
    if pred_value == 0:
        out = 'ANTIVIRUS BASED MALWARE NOT DETECTED'
    elif pred_value == 1:
        out = 'ANTIVIRUS BASED MALWARE DETECTED'

    return out
