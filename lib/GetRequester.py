import requests
import json

class GetRequester:

    def __init__(self, url):
        # Store the URL so other methods can use it
        self.url = url

    def get_response_body(self):
        # Send an HTTP GET request to the URL we stored on init
        response = requests.get(self.url)
        # .content gives us the raw response body as bytes
        return response.content

    def load_json(self):
        # Get the raw bytes first, reusing the method above
        response_body = self.get_response_body()
        # json.loads() converts JSON bytes/string into Python objects
        return json.loads(response_body)