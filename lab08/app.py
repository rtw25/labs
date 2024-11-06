from flask import Flask, render_template_string, request
from apod_model import fetch_apod  # Import the model
import datetime

app = Flask(__name__)

api_key = "KB33eu86UWu6eDQc6fZPrVWCBfUnTZfWZ4AVAssQ"  # Your API key

@app.route("/")
def home():
    # Fetch the APOD data from the model
    apod_data = fetch_apod(api_key)
    
    # Return the template with the APOD data
    return render_template_string("""
        <h1>{{ apod_data['title'] }}</h1>
        <img src="{{ apod_data['url'] }}" alt="APOD Image">
        <p>{{ apod_data['explanation'] }}</p>
        <p><strong>Copyright:</strong> {{ apod_data.get('copyright', 'No copyright info available') }}</p>
        <a href="/history">Go to History Page</a>
    """, apod_data=apod_data)

@app.route("/history", methods=["GET", "POST"])
def history():
    # Get the current date dynamically
    current_date = datetime.date.today().strftime('%Y-%m-%d')  # Format as 'YYYY-MM-DD'
    
    if request.method == "POST":
        # Get the date input from the user
        date = request.form["date"]
        # Fetch the APOD data for the specified date from the model
        apod_data = fetch_apod(api_key, date)
        
        # Return the template with the APOD data for the given date
        return render_template_string("""
            <h1>{{ apod_data['title'] }}</h1>
            <img src="{{ apod_data['url'] }}" alt="APOD Image">
            <p>{{ apod_data['explanation'] }}</p>
            <p><strong>Copyright:</strong> {{ apod_data.get('copyright', 'No copyright info available') }}</p>
            <a href="/">Back to Home Page</a>
        """, apod_data=apod_data)
    
    # Render the date input form for the user to input a date
    return render_template_string("""
        <h1>Enter a Date to See the APOD</h1>
        <form method="post">
            <label for="date">Enter a valid date (from June 16, 1995):</label>
            <input type="date" name="date" min="1995-06-16" max="{{ current_date }}" required>
            <button type="submit">Get APOD</button>
        </form>
        <a href="/">Back to Home Page</a>
    """, current_date=current_date)  # Pass the dynamically generated current date

if __name__ == "__main__":
    app.run(debug=True)
