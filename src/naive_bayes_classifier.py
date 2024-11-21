import os
import pandas
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
import joblib

# Initializing dataset
current_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(current_dir, "..")
file_name = "code_smells.csv"
file_path = os.path.join(data_dir, file_name)

# Data pre-processing
dataset = pandas.read_csv(file_path)
dataset = dataset.drop(['file_name', 'method_name'], axis=1)
dataset['code_smell_detected'] = dataset['code_smell_detected'].fillna(False)
dataset['code_smell_detected'] = dataset['code_smell_detected'].map({True: 1, False: 0}).astype(int)
feature = dataset[['line_count', 'complexity']]
target = dataset['code_smell_detected']

# Training the model
feature_train, feature_test, target_train, target_test = train_test_split(feature, target, test_size=0.3, random_state=42, shuffle=True)
model = GaussianNB()
model.fit(feature_train, target_train)

# Testing the model
predictions = model.predict(feature_test)
accuracy = model.score(feature_test, target_test)
print(f"Model accuracy: {accuracy:.3f}")

# Test the model with new data
model_name = "naive_bayes_classifier.pkl"
joblib.dump(model, model_name)
load_model = joblib.load(model_name)
test_model = pandas.DataFrame({'line_count': [35], 'complexity': [12]})
prediction = load_model.predict(test_model)
print(f"Code smell detected for: {test_model}" if prediction[0] == 1 else f"No code smell detected for {test_model}")

def predict_code_smell(line_count, complexity):
    """Predicts if a code smell is detected in the given code snippet."""
    
    model = joblib.load("naive_bayes_classifier.pkl")
    prediction = model.predict([[line_count, complexity]])
    return prediction[0] == 1