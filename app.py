from flask import Flask, render_template, request
from weather import main as get_weather
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    data = None
    city_placeholder = "City"
    state_placeholder = "State/Province"
    country_placeholder = "Country"

    if request.method == 'POST':
        city = request.form['cityName']
        state = request.form['stateName']
        country = request.form['countryName']
        data = get_weather(city, state, country)

        # Set new placeholders to user input
        city_placeholder = city
        state_placeholder = state
        country_placeholder = country

    return render_template('index.html',data=data, city_placeholder=city_placeholder, state_placeholder=state_placeholder, country_placeholder=country_placeholder)

if __name__ == '__main__':
    app.run(debug=True, port=5001)