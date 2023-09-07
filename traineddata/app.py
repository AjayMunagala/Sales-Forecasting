from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib
matplotlib.use('Agg')  # Set the backend to Agg
import matplotlib.pyplot as plt
import base64
from io import BytesIO
import numpy as np

app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/forecast', methods=['POST'])
def generate_sales_forecast():
    csv_file = request.files['csvFile']
    periodicity = request.form.get('periodicity')
    periodic_number = int(request.form.get('periodicNumber'))

    # Step 2: Load the CSV file
    df = pd.read_csv(csv_file)

    # Step 3: Preprocess the data (if needed)
    # No preprocessing steps mentioned in the question

    # Step 4: Split the data into features and target variables
    X = pd.to_datetime(df['Month'])  # Convert Month column to datetime format
    y = df['SalesPrice']

    # Step 5: Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Step 6: Choose a regression model
    reg_model = LinearRegression()

    # Step 7: Train the regression model
    X_train_encoded = X_train.map(pd.Timestamp.to_julian_date).values.reshape(-1, 1)  # Convert dates to Julian dates
    reg_model.fit(X_train_encoded, y_train)

    # Step 8: Evaluate the model
    X_test_encoded = X_test.map(pd.Timestamp.to_julian_date).values.reshape(-1, 1)
    y_pred = reg_model.predict(X_test_encoded)
    mse = mean_squared_error(y_test, y_pred)

    # Step 9: Calculate additional metrics (RMSE, MAPE, Accuracy)
    rmse = mean_squared_error(y_test, y_pred, squared=False)
    mape = calculate_mape(y_test, y_pred)
    accuracy = calculate_accuracy(y_test, y_pred)

    # Step 10: Make predictions (optional)
    new_dates = generate_new_dates(X_test.max(), periodicity, periodic_number)
    new_dates_encoded = pd.Series(pd.to_datetime(new_dates)).map(pd.Timestamp.to_julian_date).values.reshape(-1, 1)
    new_prices = reg_model.predict(new_dates_encoded)

    # Step 11: Generate the actual values graph as an image
    plt.scatter(X_test, y_test, color='blue', label='Actual')
    plt.xlabel('Date')
    plt.ylabel('Sales Price')
    plt.title('Actual Sales Price')
    plt.legend()

    # Save the actual values plot to a base64-encoded image
    actual_buffer = BytesIO()
    plt.savefig(actual_buffer, format='png')
    actual_buffer.seek(0)
    actual_image_base64 = base64.b64encode(actual_buffer.getvalue()).decode()
    plt.close()

    # Step 12: Generate the predicted values graph as an image
    plt.scatter(X_test, y_pred, color='red', label='Predicted')
    plt.xlabel('Date')
    plt.ylabel('Sales Price')
    plt.title('Predicted Sales Price')
    plt.legend()

    # Save the predicted values plot to a base64-encoded image
    predicted_buffer = BytesIO()
    plt.savefig(predicted_buffer, format='png')
    predicted_buffer.seek(0)
    predicted_image_base64 = base64.b64encode(predicted_buffer.getvalue()).decode()
    plt.close()

    # Step 13: Generate the combined values graph as an image
    plt.scatter(X_test, y_test, color='blue', label='Actual')
    plt.scatter(X_test, y_pred, color='red', label='Predicted')
    plt.scatter(new_dates, new_prices, color='green', label='Forecast')
    plt.xlabel('Date')
    plt.ylabel('Sales Price')
    plt.title('Combined Sales Price')
    plt.legend()

    # Save the combined values plot to a base64-encoded image
    combined_buffer = BytesIO()
    plt.savefig(combined_buffer, format='png')
    combined_buffer.seek(0)
    combined_image_base64 = base64.b64encode(combined_buffer.getvalue()).decode()
    plt.close()

    # Step 14: Generate the forecasted values graph as an image
    plt.scatter(new_dates, new_prices, color='green', label='Forecast')
    plt.xlabel('Date')
    plt.ylabel('Sales Price')
    plt.title('Forecasted Sales Price')
    plt.legend()

    # Save the forecasted values plot to a base64-encoded image
    forecast_buffer = BytesIO()
    plt.savefig(forecast_buffer, format='png')
    forecast_buffer.seek(0)
    forecast_image_base64 = base64.b64encode(forecast_buffer.getvalue()).decode()
    plt.close()

    # Step 15: Prepare the response data
    response_data = {
        'mse': mse,
        'rmse': rmse,
        'mape': mape,
        'accuracy': accuracy,
        'actualGraphImageUrl': f"data:image/png;base64,{actual_image_base64}",
        'predictedGraphImageUrl': f"data:image/png;base64,{predicted_image_base64}",
        'combinedGraphImageUrl': f"data:image/png;base64,{combined_image_base64}",
        'forecastGraphImageUrl': f"data:image/png;base64,{forecast_image_base64}"
    }

    return jsonify(response_data)


def calculate_mape(y_true, y_pred):
    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100


def calculate_accuracy(y_true, y_pred):
    return 100 - calculate_mape(y_true, y_pred)


def generate_new_dates(last_date, periodicity, periodic_number):
    if periodicity == 'weeks':
        freq = 'W'
    elif periodicity == 'months':
        freq = 'M'
    elif periodicity == 'years':
        freq = 'Y'
    elif periodicity == 'days':
        freq = 'D'
    else:
        raise ValueError('Invalid periodicity')

    new_dates = pd.date_range(start=last_date, periods=periodic_number + 1, freq=freq)
    return new_dates[1:].strftime('%Y-%m-%d')


if __name__ == '__main__':
    app.run(debug=True)
