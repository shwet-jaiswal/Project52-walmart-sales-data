from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import pandas as pd
import sklearn
import datetime
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('model_rfr.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        
        df_train=pd.read_csv("sales_nonzero.csv")
        
        df_train["date"] = df_train["date"].map(pd.to_datetime)
        
        date_entry = (request.form['dates'])
        year, month, day = map(int, date_entry.split('-'))
        date_con = datetime.date(year, month, day)

        store_nbr = int(request.form['storeno'])
        item_nbr = int(request.form['itemno'])
        df_weather_store = pd.DataFrame({'date': date_con,
                   'store_nbr': store_nbr,
                   'item_nbr': item_nbr}, index=[0])
        
        df_weather_store["date"] = df_weather_store["date"].map(pd.to_datetime)
        df_weather_store_train= pd.merge(df_train,df_weather_store, on=['date','store_nbr','item_nbr'], how='inner')
        
        sales_features_updated= ["store_nbr","item_nbr","station_nbr","tmax","depart","dewpoint","wetbulb","cool",
             "sunrise","sunset","snowfall","preciptotal","stnpressure","sealevel","resultspeed","resultdir","avgspeed",
             "year","month","week","day","weekday","is_holiday"]

        df_weather_store_trainx= df_weather_store_train[sales_features_updated]
        
        if not df_weather_store_trainx.empty:
            prediction=model.predict(df_weather_store_trainx)
            output=round(prediction[0],2)
            if (output > 0):
                return render_template('index.html',prediction_text="Your Sales Units are {}".format(output))
        else:
            return render_template('index.html',prediction_text="Sorry! You don't have any sales today.")
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(host='0.0.0.0', port=80)

