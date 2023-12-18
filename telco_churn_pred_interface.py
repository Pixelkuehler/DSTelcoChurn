import tkinter as tk
from tkinter import ttk
from sklearn.ensemble import RandomForestClassifier
import pandas as pd

class ChurnPredictionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Churn Prediction App")

        # Create labels and entry widgets
        self.create_input_widgets()

        # Create a button to trigger the prediction
        self.predict_button = ttk.Button(root, text="Predict", command=self.predict_churn)
        self.predict_button.grid(row=25, column=0, columnspan=2, pady=10)

        # Create a label to display the prediction result
        self.prediction_label = ttk.Label(root, text="")
        self.prediction_label.grid(row=26, column=0, columnspan=2, pady=10)

    def create_input_widgets(self):
        self.input_widgets = {}

        labels = ['gender', 'SeniorCitizen', 'Partner', 'Dependents', 'tenure',
       'PhoneService', 'MultipleLines', 'OnlineSecurity', 'OnlineBackup',
       'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies',
       'Contract', 'PaperlessBilling', 'MonthlyCharges', 'TotalCharges',
       'InternetService_DSL', 'InternetService_Fiber optic',
       'InternetService_No', 'PaymentMethod_Bank transfer (automatic)',
       'PaymentMethod_Credit card (automatic)',
       'PaymentMethod_Electronic check', 'PaymentMethod_Mailed check']

        for i, label_text in enumerate(labels):
            label = ttk.Label(self.root, text=label_text)
            label.grid(row=i, column=0, padx=10, pady=5, sticky="e")

            entry = ttk.Entry(self.root)
            entry.grid(row=i, column=1, padx=10, pady=5, sticky="w")

            self.input_widgets[label_text] = entry

    def predict_churn(self):
        # Get user inputs from entry widgets
        input_values = {key: entry.get() for key, entry in self.input_widgets.items()}

        # Convert input values to the appropriate data types
        for key in input_values:
            if key in ["Tenure", "Monthly Charges", "Total Charges"]:
                input_values[key] = float(input_values[key])
            else:
                input_values[key] = int(input_values[key])

        # Create a DataFrame from the input data
        input_df = pd.DataFrame([input_values])

        import pickle
        datei = open("telco_churn_RandomForestClassifier(n_estimators=500).pkl", "rb") # r wie read, b wie binary
        model = pickle.load(datei)
        datei.close()

        # Make predictions
        prediction = model.predict(input_df)

        # Display the prediction result
        self.prediction_label.config(text=f"Churn Prediction: {prediction[0]}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ChurnPredictionApp(root)
    root.mainloop()