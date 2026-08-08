import pandas as pd
from sklearn.linear_model import LinearRegression

# ----------------------------
# HOUSE PRICE PREDICTION SYSTEM
# ----------------------------

# Sample Dataset
data = {
    "Area": [
        1000, 1200, 1500, 1800, 2000,
        2200, 2500, 2700, 3000, 3200,
        900, 1100, 1400, 1700, 2100,
        2300, 2600, 2900, 3100, 3300
    ],

    "Bedrooms": [
        2,3,3,4,4,
        5,5,6,6,7,
        2,2,3,4,5,
        5,6,6,7,7
    ],

    "Age": [
        10,5,8,2,4,
        3,1,2,1,1,
        15,12,10,6,5,
        4,3,2,1,1
    ],

    "Price": [
        300000,350000,420000,500000,550000,
        600000,680000,720000,800000,850000,
        280000,310000,390000,470000,580000,
        620000,700000,780000,840000,900000
    ]
}

df = pd.DataFrame(data)

# Features
X = df[["Area", "Bedrooms", "Age"]]

# Target
y = df["Price"]

# Train Model
model = LinearRegression()
model.fit(X, y)

print("=" * 50)
print("      HOUSE PRICE PREDICTION SYSTEM")
print("=" * 50)

while True:

    print("\nEnter House Details")

    area = float(input("Area (sq.ft): "))
    bedrooms = int(input("Bedrooms: "))
    age = int(input("Age of House: "))

    prediction = model.predict([[area, bedrooms, age]])

    print("\nPredicted House Price")
    print("----------------------------------")
    print(f"${prediction[0]:,.2f}")

    choice = input("\nPredict another house? (y/n): ")

    if choice.lower() != 'y':
        print("\nThank You!")
        break