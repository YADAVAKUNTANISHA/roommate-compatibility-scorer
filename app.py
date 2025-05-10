from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Load the CSV file with roommate profiles (if needed)
# roommate_df = pd.read_csv('roommate_profiles.csv')

# Route for the homepage
@app.route('/')
def index():
    return render_template('index.html')

# Route to calculate compatibility score
@app.route('/calculate', methods=['POST'])
def calculate():
    # Get user preferences from the form
    sleep1 = request.form.get('sleep1')
    cleanliness1 = request.form.get('cleanliness1')
    work_schedule1 = request.form.get('workSchedule1')
    food_habits1 = request.form.get('foodHabits1')

    sleep2 = request.form.get('sleep2')
    cleanliness2 = request.form.get('cleanliness2')
    work_schedule2 = request.form.get('workSchedule2')
    food_habits2 = request.form.get('foodHabits2')

    # Calculate compatibility score
    score = 0
    if sleep1 == sleep2:
        score += 10
    if cleanliness1 == cleanliness2:
        score += 20
    if work_schedule1 == work_schedule2:
        score += 30
    if food_habits1 == food_habits2:
        score += 40

    return render_template('index.html', score=score)

if __name__ == '__main__':
    app.run(debug=True)
