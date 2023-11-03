from sklearn.neighbors import KNeighborsClassifier
import joblib
import numpy as np

# Function to calculate features (mean and standard deviation)
def calculate_features(angle_set):
    return [np.mean(angle_set), np.std(angle_set)]

# Function to train and save the classifier
def train_and_save_model(good_angles_1, good_angles_2, bad_angles_1, bad_angles_2, model_filename):
    X_train = np.array([
        calculate_features(good_angles_1),
        calculate_features(good_angles_2),
        calculate_features(bad_angles_1),
        calculate_features(bad_angles_2)
    ])
    y_train = np.array(['good', 'good', 'bad', 'bad'])
    
    knn = KNeighborsClassifier(n_neighbors=2)
    knn.fit(X_train, y_train)
    
    # Save the trained model to a file
    joblib.dump(knn, model_filename)
    print(f"Model saved to {model_filename}")

# Function to load the model and predict the class of new angles
def classify_angles(new_angles, model_filename):
    # Load the trained model from the file
    knn = joblib.load(model_filename)
    
    # Calculate features for the new set of angles
    new_features = calculate_features(new_angles)
    
    # Classify the new set of angles
    prediction = knn.predict([new_features])
    
    return prediction[0]

# Example usage:
# Assuming good_angles_1, good_angles_2, bad_angles_1, bad_angles_2 are defined:
train_and_save_model(good_angles_1, good_angles_2, bad_angles_1, bad_angles_2, 'knn_model.joblib')

# Then, when you need to classify new angles:
# new_angles = [...]  # Replace with your new angles data
# result = classify_angles(new_angles, 'knn_model.joblib')
# print(f"The new set of angles is likely {result}")
