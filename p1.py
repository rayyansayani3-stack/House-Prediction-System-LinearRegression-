import pandas as pd
from sklearn.linear_model import LinearRegression

# ---------------------------------
# STUDENT MARKS PREDICTION SYSTEM
# ---------------------------------

# Sample Dataset
data = {
    "Study_Hours": [
        1,2,3,4,5,
        6,7,8,9,10,
        2.5,3.5,4.5,5.5,6.5,
        7.5,8.5,9.5,1.5,5
    ],

    "Attendance": [
        60,65,70,75,80,
        82,85,88,90,95,
        68,72,77,81,84,
        87,91,94,63,79
    ],

    "Marks": [
        30,40,48,55,63,
        70,76,83,90,98,
        44,52,59,66,73,
        80,86,94,35,61
    ]
}

df = pd.DataFrame(data)

# Features
X = df[["Study_Hours", "Attendance"]]

# Target
y = df["Marks"]

# Train Model
model = LinearRegression()
model.fit(X, y)

print("=" * 50)
print("      STUDENT MARKS PREDICTION")
print("=" * 50)

while True:

    print("\nEnter Student Details")

    hours = float(input("Study Hours per Day: "))
    attendance = float(input("Attendance Percentage: "))

    prediction = model.predict([[hours, attendance]])

    if prediction[0] > 100:
        prediction[0] = 100

    if prediction[0] < 0:
        prediction[0] = 0

    print("\nPredicted Marks")
    print("-" * 30)
    print(f"{prediction[0]:.2f} / 100")

    if prediction[0] >= 90:
        grade = "A+"
    elif prediction[0] >= 80:
        grade = "A"
    elif prediction[0] >= 70:
        grade = "B"
    elif prediction[0] >= 60:
        grade = "C"
    elif prediction[0] >= 50:
        grade = "D"
    else:
        grade = "F"

    print("Grade:", grade)

    choice = input("\nPredict Another Student? (y/n): ")

    if choice.lower() != "y":
        print("\nThank You!")
        break