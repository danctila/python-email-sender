import requests
import json

def randomFact():
    api_url = "https://uselessfacts.jsph.pl/api/v2/facts/today?language=en"

    # pull API data with get request to /api/v2/facts/random endpoint
    response = requests.get(api_url)

    # convert JSON data to dictionary
    response = json.loads(response.text)
    
    # pull text value using 'text' key from response dictionary
    return(response["text"])

randomFact()