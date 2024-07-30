import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import OneHotEncoder

# Path to the CSV file
file_path = 'C:/Users/User/Desktop/PYTHON PROGRAMS/annual-enterprise-survey-2023-financial-year-provisional.csv'

# Load the CSV file
data = pd.read_csv(file_path)

# Display the first few rows of the dataset
print(data.head())

# Define the feature columns and the target column
# Replace 'Year', 'Industry_aggregation_NZSIOC' with actual feature column names from your dataset
# Replace 'Value' with the actual target column name
features = ['Year', 'Industry_aggregation_NZSIOC']  # Example feature columns
target = 'Value'  # Example target column

# One-hot encode categorical features
encoder = OneHotEncoder(sparse_output=False)  # Correct parameter for newer scikit-learn versions
encoded_features = encoder.fit_transform(data[['Industry_aggregation_NZSIOC']])
encoded_feature_names = encoder.get_feature_names_out(['Industry_aggregation_NZSIOC'])

# Create a DataFrame with the encoded features
encoded_df = pd.DataFrame(encoded_features, columns=encoded_feature_names)

# Combine encoded features with the numerical features
X = pd.concat([data[['Year']], encoded_df], axis=1)
y = data[target]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a Linear Regression model
model = LinearRegression()

# Train the model on the training data
model.fit(X_train, y_train)

# Predict on the test data
y_pred = model.predict(X_test)

# Calculate the Mean Squared Error
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')

# Calculate the R-squared score
r2 = r2_score(y_test, y_pred)
print(f'R-squared score: {r2}')
