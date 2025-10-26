import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pandas as pd
import shap
from sklearn.metrics import classification_report, roc_auc_score, accuracy_score, f1_score
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import pickle


df = pd.read_csv('dataset/synthetic_employee_burnout.csv')

df['TaskScore'] = (
    0.4 * df['WorkHoursPerWeek'] +        # più ore, più responsabilità
    0.3 * df['StressLevel'] * 10 -         # stress aumenta peso
    0.2 * df['SatisfactionLevel'] * 10 +   # più soddisfazione = meno carico percepito
    0.1 * df['Experience'] * 2             # più esperienza = più task importanti
)

# Normalizza i valori per renderli confrontabili
df['TaskScore'] = (df['TaskScore'] - df['TaskScore'].min()) / (df['TaskScore'].max() - df['TaskScore'].min())

# Categorizza in livelli qualitativi
df['Task'] = pd.cut(
    df['TaskScore'],
    bins=[-np.inf, 0.33, 0.66, np.inf],
    labels=['Low', 'Medium', 'High']
)

X = df.drop(columns=["Burnout"])
print(X.head(10))
X = pd.get_dummies(X, drop_first=True)


y = df["Burnout"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(len(X_train), len(X_test))

print(X)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
model = LogisticRegression(max_iter=1000,class_weight="balanced")
model.fit(X_train_scaled, y_train)

with open('burnout_predictor.pkl', 'wb') as f:
    pickle.dump((model, scaler, X.columns), f)
with open('burnout_predictor.pkl', 'rb') as f:
    model, scaler, feature_names = pickle.load(f)

X_test_scaled = scaler.transform(X_test)

y_pred = model.predict(X_test_scaled)
y_prob = model.predict_proba(X_test_scaled)[:, 1]

print(classification_report(y_test, y_pred))
print("ROC-AUC:", roc_auc_score(y_test, y_prob))
print("Accuracy:", accuracy_score(y_test, y_pred))
print("F1 Score:", f1_score(y_test, y_pred))



# cm = confusion_matrix(y_test, y_pred)
# disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=["No Burnout", "Burnout"])
# # disp.plot(cmap="Blues")
# # plt.title("Matrice di confusione per il modello di burnout")
# # plt.show()
with open('burnout_predictor.pkl', 'rb') as f:
    model, scaler, feature_names = pickle.load(f)

explainer = shap.Explainer(lambda x: model.predict_proba(x)[:, 1], 
                           scaler.transform(X), 
                           feature_names=X.columns)

shap_values = explainer(scaler.transform(X_test))

# # i = 0

# # print(X_test.iloc[i])

# # shap.plots.waterfall(shap_values[i])

# ####### TEST NEW SAMPLE INPUT
new_employee = {
     'Age': 23,
     'Gender': 'Male',
     'JobRole': 'Sales',
     'Experience': 10,
     'WorkHoursPerWeek': 40,
     'RemoteRatio': 0,
     'SatisfactionLevel': 5,
     'StressLevel': 0,
     'TaskScore': 0.2,
     'Task': 'Low'
}

new_df = pd.DataFrame([new_employee])
new_df = pd.get_dummies(new_df, drop_first=True)
new_df = new_df.reindex(columns=X.columns, fill_value=0)
new_df_scaled = scaler.transform(new_df)


new_pred = model.predict(new_df_scaled)[0]
new_prob = model.predict_proba(new_df_scaled)[0, 1]

print(f"Predizione: {'BURNOUT' if new_pred == 1 else 'NO BURNOUT'}")
print(f"Probabilità stimata di burnout: {new_prob:.2f}")

shap_values_new = explainer(new_df_scaled)
plt.figure(figsize=(6, 4))
shap.plots.waterfall(shap_values_new[0], show=False)
plt.tight_layout()
plt.show()