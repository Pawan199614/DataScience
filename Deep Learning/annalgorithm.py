import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler,LabelEncoder, OneHotEncoder
import pickle


data = pd.read_csv('Churn_Modelling.csv')

# preprocessing drop unnecessary columns
data = data.drop(['RowNumber', 'CustomerId', 'Surname'], axis=1)

# Encoding categorical variables
label_encoder = LabelEncoder()
data["Gender"] = label_encoder.fit_transform(data["Gender"])

#print(data.head)

# One-hot encoding for 'Geography' column
one_encoder_geo = OneHotEncoder()
geo_encoded = one_encoder_geo.fit_transform(data[['Geography']])

#print(one_encoder_geo.get_feature_names_out(['Geography']))

geo_encoder_df = pd.DataFrame(geo_encoded.toarray(), columns=one_encoder_geo.get_feature_names_out(['Geography']))

# Combine one-hot encoded columns with the original dataframe
data = pd.concat([data.drop('Geography',axis=1), geo_encoder_df], axis=1)

#print(data.head())

# Save the encoders and scaler
"""with open('label_encoder_gender.pkl', 'wb') as f:   
    pickle.dump(label_encoder, f)

with open('onehot_encoder_geo.pkl', 'wb') as f:
    pickle.dump(one_encoder_geo, f)"""

#divide the data into features and target variable
X = data.drop('Exited', axis=1)
y = data['Exited']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale the features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

with open('scaler.pkl', 'wb') as f:
    pickle.dump(scaler, f)
