import pandas as pd
from sklearn.linear_model import LinearRegression

# Load the CSV file
df = pd.read_csv('sales.csv')

# Preprocess the data (if needed)
# No preprocessing steps mentioned in the question

# Split the data into features and target variables
X = pd.to_datetime(df['Month'])  # Convert Month column to datetime format
y = df['SalesPrice']

# Choose a regression model
reg_model = LinearRegression()

# Train the regression model
X_encoded = X.map(pd.Timestamp.to_julian_date).values.reshape(-1, 1)  # Convert dates to Julian dates
reg_model.fit(X_encoded, y)

# Make predictions
last_date = X.max()
new_dates = pd.date_range(start=last_date + pd.DateOffset(days=1), periods=6-*12*31, freq='D')  # Forecast for 4 years
new_dates_encoded = pd.Series(pd.to_datetime(new_dates)).map(pd.Timestamp.to_julian_date).values.reshape(-1, 1)
new_prices = reg_model.predict(new_dates_encoded)

# Generate the forecasted data DataFrame
forecasted_data = pd.DataFrame({'Month': new_dates.strftime('%m/%d/%Y'), 'SalesPrice': new_prices})

# Save the forecasted data as a CSV file
forecasted_data.to_csv('forecasted_data.csv', index=False)
print('Forecasted data generated and saved as forecasted_data.csv')
