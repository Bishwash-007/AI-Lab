import tkinter as tk
from tkinter import ttk
import pickle
import numpy as np

# Load the trained model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

# Function to perform prediction
def predict():
    try:
        # Get input values
        sepal_length = float(entry_sepal_length.get())
        sepal_width = float(entry_sepal_width.get())
        petal_length = float(entry_petal_length.get())
        petal_width = float(entry_petal_width.get())
        
        # Create input array and predict
        input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
        prediction = model.predict(input_data)
        
        # Display prediction
        result_label.config(text=f"Predicted Class: {prediction[0]}")
    except ValueError:
        result_label.config(text="Error: Please enter valid numbers.")
    except Exception as e:
        result_label.config(text=f"Error: {str(e)}")

# Create main window
root = tk.Tk()
root.title("Iris Flower Predictor")
root.geometry("400x400")
root.resizable(False, False)

# Style setup
style = ttk.Style()
style.configure('TLabel', font=('Helvetica', 12))
style.configure('TButton', font=('Helvetica', 12, 'bold'), background="#5F9EA0")
style.configure('TEntry', font=('Helvetica', 12))

# Title
title_label = ttk.Label(root, text="Iris Flower Prediction", font=('Helvetica', 16, 'bold'), anchor="center")
title_label.pack(pady=10)

# Input fields
frame = ttk.Frame(root)
frame.pack(pady=10, padx=20)

labels = ['Sepal Length', 'Sepal Width', 'Petal Length', 'Petal Width']
entries = []
for i, label in enumerate(labels):
    lbl = ttk.Label(frame, text=f"{label}:")
    lbl.grid(row=i, column=0, pady=5, sticky='w')
    entry = ttk.Entry(frame, width=20)
    entry.grid(row=i, column=1, pady=5)
    entries.append(entry)

entry_sepal_length, entry_sepal_width, entry_petal_length, entry_petal_width = entries

# Predict button
predict_button = ttk.Button(root, text="Predict", command=predict)
predict_button.pack(pady=20)

# Result label
result_label = ttk.Label(root, text="", font=('Helvetica', 14), foreground="#2E8B57")
result_label.pack(pady=10)

# Run the application
root.mainloop()