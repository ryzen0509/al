##Q.1

def means_end_analysis(current, goal):
    print("Current State:", current)

    if current == goal:
        print("Goal Reached!")
        return

    if current < goal:
        print("Action: Increase the value")
        current += 1

    elif current > goal:
        print("Action: Decrease the value")
        current -= 1

    means_end_analysis(current, goal)

start = 2
goal = 5

means_end_analysis(start, goal)

##Q.2

import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

dataset = {
    'Study_Hours': [2, 3, 4, 5, 6, 7, 1, 2, 5, 8],
    'Attendance': [60, 65, 70, 75, 80, 85, 55, 62, 78, 90],
    'Assignment_Score': [55, 60, 65, 70, 75, 80, 50, 58, 72, 85],
    'Result': [
        'Fail', 'Fail', 'Pass', 'Pass', 'Pass',
        'Pass', 'Fail', 'Fail', 'Pass', 'Pass'
    ]
}

df = pd.DataFrame(dataset)

print("Dataset:")
print(df)

X = df[['Study_Hours', 'Attendance', 'Assignment_Score']]
y = df['Result']

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X, y)

y_pred = model.predict(X)

print("\nActual Results:", list(y))
print("Predicted Results:", list(y_pred))

print("Accuracy:", model.score(X, y))