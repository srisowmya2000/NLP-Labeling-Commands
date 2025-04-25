import os
import pandas as pd
from transformers import pipeline
from flask import Flask, render_template, request, jsonify

# Get absolute path to the web folder where your index.html is located
current_dir = os.path.dirname(os.path.abspath(__file__))
template_dir = os.path.join(current_dir, 'web')

app = Flask(__name__, template_folder=template_dir)

classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

# Define labels
labels = ["benign", "suspicious", "malicious"]

# Load commands database
def load_commands_db(csv_path):
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"CSV file not found at {csv_path}")
    
    df = pd.read_csv(csv_path)
    return df['command'].tolist()  # Assumes the column is named 'command'

# Route for home page
@app.route('/')
def index():
    return render_template('index.html')

# Route for command classification
@app.route('/classify', methods=['POST'])
def classify_command():
    # Get command from request
    command = request.form['command']
    
    # Classify the command
    result = classifier(command, candidate_labels=labels)
    
    # Prepare response
    response = {
        'command': command,
        'prediction': result["labels"][0],
        'score': round(result["scores"][0], 3)
    }
    
    return jsonify(response)

if __name__ == '__main__':
    # Use the exact path from your working code
    csv_path = r"<path>"
    
    try:
        commands = load_commands_db(csv_path)
        print(f"Successfully loaded {len(commands)} commands")
        
        # Run Flask app
        app.run(debug=True)
    except Exception as e:
        print(f"Error: {e}")
        print("Please check the file path and try again.")
