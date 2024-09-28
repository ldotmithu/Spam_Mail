import joblib 
import numpy as np
import pandas as pd
from pathlib import Path

class PredictionPipeline:
    def __init__(self):
        self.vector = joblib.load('artifacts/model_train/vector.joblib')
        self.model = joblib.load(Path('artifacts\model_train\model.joblib'))
    
    def predict(self, data):
        data = self.preprocessor.transform(data)
        prediction = self.model.predict(data)

        return prediction