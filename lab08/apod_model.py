# apod_model.py
import requests

def fetch_apod(api_key, date=None):
    # Build the URL for the APOD API request
    url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"
    
    # If a date is provided, include it in the URL
    if date:
        url += f"&date={date}"
    
    # Make the API request
    response = requests.get(url)
    
    # Check if the response is successful
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}")
