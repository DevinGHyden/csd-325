# Name: Devin G. Hyden
# Date: 05 August 2026
# Assignment: Module 9.2 Assignment

import json
import requests

def check_api_connection(url):
    """Sends an HTTP GET request to the provided URL and prints the HTTP
    status code."""
    try:
        # Send HTTP Get request
        response = requests.get(url)
        # Output HTTP status code
        print(f"Connection Status Code: {response.status_code}")

        # Return the response object
        return response

    except requests.exceptions.RequestException as e:
        # Catch and display any connection errors
        print("Error connecting to API: {e}")
        return None


def print_raw_response(response):
    """Prints the raw, unformatted text from the API response."""
    print("\n--- Raw Response ---")
    # response.text contains the raw JSON string from the server
    print(response.text)


def print_formatted_astronauts(response):
    """Prints a clean, formatted list of astronauts."""
    # Verify response exists and request was successful
    if response and response.status_code == 200:
        # Parse teh JSON string into a Python dictionary
        data = response.json()

        print("\n--- Formatted Astronaut Information ---")
        # Extract the value associated with the 'number' key
        print(f"Number of people in space: {data['number']}\n")

        # Print header columns with field formatting
        print(f"{'Name':<30} | {'Craft'}")
        print("-" * 45)

        # Iterate through list of dictionaries inside the 'people' key
        for person in data["people"]:
            # Extract and display the astronaut's name and spacecraft name
            print(f"{person['name']:<30} | {person['craft']}")
    else:
        print("Failed to retrieve valid astronaut data.")


def main():
    """Main function coordinating script tasks."""
    # Define target endpoint from Open Notify API
    astros_url = "http://api.open-notify.org/astros.json"

    # Call function to check API connection
    response = check_api_connection(astros_url)

    #Proceed if connection succeeded
    if response:
        print_raw_response(response)
        print_formatted_astronauts(response)

if __name__ == "__main__":
    main()
