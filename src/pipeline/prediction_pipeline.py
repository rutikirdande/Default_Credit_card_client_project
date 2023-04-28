import sys
import os
from src.exception import CustomException
from src.logger import logging
from src.utils import load_object
import pandas as pd

class PredictionPipeline:
    def __init__(self):
        pass

    def predict(self, features):
        try:
            x,y=make_classification(n_samples=1000,n_features=5,random_state=123)
            x_data=os.path.join('artifacts', 'x_data.pkl')
            y_data=os.path.join('artifacts', 'y_data.pkl')
            model_score=model.score(x_train, y_train)
            y_pred=model.predict(x_test)
            accuracy_score=accuracy_score(y_test, y_pred)
            return accuracy_score
        except Exception as e:
            logging.info("Exception occured in prediction")
            raise CustomException(e, sys)

class CustomData:
    def __init__(self, LIMIT_BAL:int,
    AGE:int,
    PAY_0:int,
    PAY_2:int,
    PAY_3:int,
    PAY_4:int,
    PAY_5:int,
    PAY_6:int,
    BILL_AMT1:int,
    BILL_AMT2:int,
    BILL_AMT3:int,
    BILL_AMT4:int,
    BILL_AMT5:int,
    BILL_AMT6:int,
    PAY_AMT1:int,
    PAY_AMT2:int,
    PAY_AMT3:int,
    PAY_AMT4:int,
    PAY_AMT5:int,
    PAY_AMT6:int,
    default_payment_next_month:int):
        self.LIMIT_BAL=LIMIT_BAL
        self.AGE=AGE
        self.PAY_0=PAY_0
        self.PAY_2=PAY_2
        self.PAY_3=PAY_3
        self.PAY_4=PAY_4
        self.PAY_5=PAY_5
        self.PAY_6=PAY_6
        self.BILL_AMT1=BILL_AMT1
        self.BILL_AMT2=BILL_AMT2
        self.BILL_AMT3=BILL_AMT3
        self.BILL_AMT4=BILL_AMT4
        self.BILL_AMT5=BILL_AMT5
        self.BILL_AMT6=BILL_AMT6
        self.PAY_AMT1=PAY_AMT1
        self.PAY_AMT2=PAY_AMT2
        self.PAY_AMT3=PAY_AMT3
        self.PAY_AMT4=PAY_AMT4
        self.PAY_AMT5=PAY_AMT5
        self.PAY_AMT6=PAY_AMT6
        self.default_payment_next_month =default_payment_next_month

    def get_data_as_dataframe(self):
        try:
            custom_data_input_dict = {
             'LIMIT_BAL':[self.LIMIT_BAL],
             'AGE':[self.AGE],
             'PAY_0':[self.PAY_0],
             'PAY_2':[self.PAY_2],
             'PAY_3':[self.PAY_3],
             'PAY_4':[self.PAY_4],
             'PAY_5':[self.PAY_5],
             'PAY_6':[self.PAY_6],
             'BILL_AMT1':[self.BILL_AMT1],
             'BILL_AMT2':[self.BILL_AMT2],
             'BILL_AMT3':[self.BILL_AMT3],
             'BILL_AMT4':[self.BILL_AMT4],
             'BILL_AMT5':[self.BILL_AMT5],
             'BILL_AMT6':[self.BILL_AMT6],
             'PAY_AMT1':[self.PAY_AMT1],
             'PAY_AMT2':[self.PAY_AMT2],
             'PAY_AMT3':[self.PAY_AMT3],
             'PAY_AMT4':[self.PAY_AMT4],
             'PAY_AMT5':[self.PAY_AMT5],
             'PAY_AMT6':[self.PAY_AMT6],
             'default payment next month':[self.default_payment_next_month]

            }
            df=pd.DataFrame(custom_data_input_dict)
            logging.info('DataFrame Gathered')
            return df

        except Exception as e:
            logging.info('Exception occured in prediction pipeline')
            raise CustomException(e, sys)

