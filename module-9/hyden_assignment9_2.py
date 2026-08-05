# Name: Devin G. Hyden
# Date: 05 August 2026
# Assignment: Module 9.2 Assignment

import json
import requests


def check_got_api_connection(url):
    """Tests connection to Ice and Fire API"""
    try:
        # Make GET request to Ice and Fire API
        response = requests.get(url)

        # Print status code result
        print(f"Connection Status Code: {response.status_code}")
        return response

    except requests.exceptions.RequestException as e:
        # Handle potential connection failure
        print(f"Error connecting to API: {e}")
        return None


def print_raw_got_response(response):
    """Outputs raw unformatted HTTP response string"""
    print("\n--- Raw Response ---")
    # Prints direct raw text string
    print(response.text)


def print_formatted_got_response(response):
    """Outputs response formatted with JSON indentation"""
    if response and response.status_code == 200:
        # Parse response body into Python dictionary object
        data = response.json()

        print("\n--- Formatted Response ---")
        # Use json.dumps with indent parameter to format JSON cleanly
        formatted_json = json.dumps(data, indent=4)
        print(formatted_json)
    else:
        print("Failed to parse response.")


def main():
    """Main execution function"""
    # Define endpoint for book 1 in An API of Ice and Fire
    got_url = "https://anapioficeandfire.com/api/books/1"

    # Test API connection status
    response = check_got_api_connection(got_url)

    if response:
        # Display raw, unformatted response
        print_raw_got_response(response)

        # Display formatted response
        print_formatted_got_response(response)


if __name__ == "__main__":
    main()