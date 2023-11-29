from flask import Flask, render_template
import pandas as pd
import logic as logic

app = Flask(__name__)

@app.route("/")
def display_html():
    accuracy, predictions = logic.train_and_predict()

    template_variables = {
        'accuracy': accuracy,
        'predictions': predictions
    }
    
    return render_template('display_template.html', **template_variables)
if __name__ == '__main__':
    app.run(debug=True)