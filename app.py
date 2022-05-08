import pickle
f = open("model.pkl","rb")
model = pickle.load(f)
def Price_prediction(Year,Presentprice,kmsdriven,Owners,CNG,Diesel,Petrol,Dealer,Individual,Automatic,Manual):
    newvalues = [[Year,Presentprice,kmsdriven,Owners,CNG,Diesel,Petrol,Dealer,Individual,Automatic,Manual]]
    price = model.predict(newvalues)
    return price
print(Price_prediction(2018,500000,20000,1,1,0,0,1,0,0,1))
import streamlit as st
st.title("Car Price Prediction App")
st.info("The app is in testing phase")
col1,col2 = st.columns(2)
Year = col1.number_input("Year of Manufacturing",2012,2022)
Presentprice = col1.number_input("Enter the Present Price of the car")
kmsdriven = col1.number_input("Enter the kmsdriven")
Owners = col1.number_input("Number of Owners changed",0,10)
Fueltype = col2.selectbox("Select the Fuel type",["CNG","Diesel","Petrol"])
Sellertype = col2.selectbox("Select the seller type",["Dealer","Individual"])
Transmissiontype = col2.selectbox("Select the transmission type",["Automatic","Manual"])
col2.markdown(" ")
if Fueltype == "CNG":
    CNG = 1
    Diesel = 0
    Petrol = 0
if Fueltype == "Diesel":
    CNG = 0
    Diesel = 1
    Petrol = 0
if Fueltype == "Petrol":
    CNG = 0
    Diesel = 0
    Petrol = 1
if Sellertype == "Dealer":
    Dealer=1
    Individual = 0
if Sellertype == "Individual":
    Dealer= 0
    Individual = 1
if Transmissiontype == "Automatic":
    Automatic = 1
    Manual = 0
if Transmissiontype == "Manual":
    Automatic = 0
    Manual = 1
if col2.button("Predict Car Price"):
    Price_car = Price_prediction(Year,Presentprice,kmsdriven,Owners,CNG,Diesel,Petrol,Dealer,Individual,Automatic,Manual)
    st.success("The Predicted Price for car is {}".format(Price_car[0][0]))