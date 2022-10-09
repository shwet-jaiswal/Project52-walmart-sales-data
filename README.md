## Project No: 52

## Project Title: To predict the sales of weather sensitive products of Walmart during major weather events

Walmart has provided us with a dataset which contains sales data for 111 products whose sales may get affected by the weather. These 111 products are sold in stores at 45 different locations which are covered by 20 weather stations. Considering data is provided on a daily basis and our main objective is to predict sales of stores in a day factorizing the weather on that particular day.

#### Dataset : https://www.kaggle.com/c/walmart-recruiting-sales-in-stormy-weather/data

The data description of all the attributes in our dataset is described as follows:
<li>Key.CSV : store_nbr, station_nbr</li>
<li>Weather.CSV: station_nbr, date, tmax, tmin, tavg, depart, dewpoint, Wetbulb-heat, heat, cool, sunrise, sunset, codesum, snowfall, preciptotal, stnpressure, sealevel, resultspeed, resultdir, avgspeed</li>
<li>‘noaa_weather_qclcd_documentation.pdf’ used for the definition of the weather data column.</li>
<li>Train.CSV: date, station_nbr, item_nbr, units</li>
<li>Test.CSV: date, station_nbr, item_nbr, units</li>
sampleSubmission.CSV: id, units</li>

#### Error Evaluation Metric: Root Mean Squared Logarithmic Error (RMSLE) 
![image](https://user-images.githubusercontent.com/55212528/156655401-2cd17e21-ff50-47d5-8bb4-16b997f8ad6a.png)

#### Base Model : Random Forest 
<li>	R^2 error:  0.6723484182079371 </li>
<li>	Root mean squared error (RMSE):  6.672133771918248 </li>
<li>	Root mean squared log error (RMSLE):  0.5155852875749393 </li>

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




