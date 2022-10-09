## Project No: 52

## Project Title: To predict the sales of weather sensitive products of Walmart during major weather events

Walmart has provided us with a dataset which contains sales data for 111 products whose sales may get affected by the weather. These 111 products are sold in stores at 45 different locations which are covered by 20 weather stations. Considering data is provided on a daily basis and our main objective is to predict sales of stores in a day factorizing the weather on that particular day.

#### Dataset : https://www.kaggle.com/c/walmart-recruiting-sales-in-stormy-weather/data

#### Error Evaluation Metric: Root Mean Squared Logarithmic Error (RMSLE) 
![image](https://user-images.githubusercontent.com/55212528/156655401-2cd17e21-ff50-47d5-8bb4-16b997f8ad6a.png)

#### Best Model: LSTM
<li>Train loss: 0.0056</li> 
<li>val_loss: 0.0170</li>

#### Project files:
<li>requirements.txt - Hold information of all required libaries to execute the app</li>
<li>runtime.txt - Pyhton version for Buildpack platform detetion</li>
<li>Procfile - Gunicorn for Python HTTP server for WSGI Applications</li>
<li>Phase_5_Project_No_52_ShwetKumarJaiswal.ipynb</li>
<li>model_rfr.pkl- Serialize Pyhton object which hold the model</li>
<li>app.py- API to predict the sales units</li>
<li>template-index.html- Interface for user input</li>

#### Deployed App link:
https://project52-shwet.herokuapp.com/



