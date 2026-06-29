import numpy as np
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import seaborn as sns
import matplotlib.pyplot as plt

# Data
df = pd.read_csv("Ice Cream.csv")


# Handle Missing values :-
# print(df.isnull().sum())
# There is no missing values in dataset

# Polynomial Regression :-
x = df[['Temperature']]
y = df['Revenue']

poly = PolynomialFeatures(degree=2)
x_poly = poly.fit_transform(x)

# model
model = LinearRegression()
model.fit(x_poly, y)

# Predict
input_data = float(input("Enter the current Temperature in your area (eg: 35.5): "))
new_data = pd.DataFrame({
    'Temperature': [input_data]
})

# input data into poly. regression form 
u_new_data = poly.transform(new_data)

# Prediction
predicted_data = model.predict(u_new_data)
predicted_data = max(0, predicted_data[0])
print(f"Estimated Revenue from Ice Cream Sales: ₹{predicted_data:,.2f}")

if input_data > 55 or input_data < 5 :
    print("Warning: Temperature is outside the training range. Prediction may not be reliable.")


# Save Model by pickle
import pickle

with open("ice_cream_model.pkl", "wb") as file:
    pickle.dump(model, file)

print("Model saved successfully!")



# Graph :-
plt.scatter(
    input_data,
    predicted_data,
    color="red",
    marker="*",
    s=250,
    label="User Prediction"
)

sns.lineplot(data=df, x='Temperature', y='Revenue')


plt.title("Temperature vs Ice Cream Revenue")
plt.xlabel("Temperature (°C)")
plt.ylabel("Revenue (Rs)")

plt.savefig("temperature_vs_ice_cream_revenue.jpg")
plt.show()