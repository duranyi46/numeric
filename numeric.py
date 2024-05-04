import pandas as pd

data = {'t': [0, 0.25, 0.5, 0.75, 1, 1.25, 1.5],
        'x': [0, 4.3, 10.2, 17.2, 26.2, 33.1, 39.1]}
df = pd.DataFrame.from_dict(data)

delta = 0.5 - 0.25
velocity3 = []

# Three-point formulas for velocity. Endpoint for first and last point, midpoint for rest of the points.
# I assumed that since the error cannot be calculated, as long as delta is constant midpoint method gives less error.
for i in range(7):
        if i >= 1 and i < 6:
                velocity3.append(round((1 / (2 * delta)) * (data['x'][i+1] - data['x'][i-1]), 4))
        elif i == 0:
                velocity3.append(round((1 / (2 * delta)) * (-3 * data['x'][i] + 4 * data['x'][i+1] - data['x'][i+2]), 4))
        else:
                velocity3.append(round((1 / (2 * -delta)) * (-3 * data['x'][i] + 4 * data['x'][i-1] - data['x'][i-2]), 4))

df['Velocity_Three_Point(m/s)'] = velocity3

velocity5 = []
# Five-point formulas for velocity. Midpoint formula for x=10.2, x=17.2, x=26.2
# Endpoint formula for x = 0.0, x= 4.3(Forward), x=33.1, x=39.1(Backward)
for k in range(7):
        if k > 1 and k < 5:
                velocity5.append(round((1 / (12 * delta)) * (data['x'][k-2] - 8 * data['x'][k-1] + 8 * data['x'][k+1] - data['x'][k+2]), 4))
        elif k == 0 or k == 1:
                velocity5.append(round((1 / (12 * delta)) * (-25 * data['x'][k] + 48 * data['x'][k+1] - 36 * data['x'][k+2] + 16 * data['x'][k+3] - 3 * data['x'][k+4]), 4))
        elif k == 5 or k == 6:
                velocity5.append(round((1 / (12 * -delta)) * (-25 * data['x'][k] + 48 * data['x'][k-1] - 36 * data['x'][k-2] + 16 * data['x'][k-3] - 3 * data['x'][k-4]), 4))

df['Velocity_Five_Point(m/s)'] = velocity5

# Acceleration will be calculated both Three-point and Five-point velocity values.

# Acceleration for both Three-Point and Five-Point velocity values using Forward difference, Backward difference, Central difference respectively.

def acc_forward(v):
        acc_f = []
        for n in range(6):
                acc_f.append(round(((v[n+1] - v[n]) / delta), 4))
        acc_f.append(None)
        return acc_f
df["Acceleration_Forward_TP"] = acc_forward(velocity3)
df["Acceleration_Forward_FP"] = acc_forward(velocity5)

def acc_backward(v):
        acc_b = []
        acc_b.append(None)
        for n in range(1,7):
                acc_b.append(round(((v[n] - v[n-1]) / delta), 4))
        return acc_b
df["Acceleration_Backward_TP"] = acc_backward(velocity3)
df["Acceleration_Backward_FP"] = acc_backward(velocity5)

def acc_central(v):
        acc_c = []
        acc_c.append(None)
        for n in range(1,6):
                acc_c.append(round(((v[n+1] - v[n-1]) / (2 * delta)), 4))
        acc_c.append(None)
        return acc_c
df["Acceleration_Central_TP"] = acc_central(velocity3)
df["Acceleration_Central_FP"] = acc_central(velocity5)

print(df)
