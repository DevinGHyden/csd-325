# Name: Devin G. Hyden
# Date: 23 July 2026
# Assignment: Module 7.2 Assignment

def city_country(city, country, population='', language=''):
    # Format the required city and country
    result = f"{city.title()}, {country.title()}"
    # Check if a population value was provided and append it
    if population:
        result += f" - population {population}"
    # Check if a language value was provided and append it in title case
    if language:
        result += f", {language.title()}"
    # Return the final built string
    return result


# Ensures the print statements only run if this file is executed directly
if __name__ == "__main__":
    # Provide only the required City and Country
    print(city_country('santiago', 'chile'))
    # Provide City, Country, and the optional Population
    print(city_country('tokyo', 'japan', population=13960000))
    # Provide all arguments: City, Country, Population, and Language
    print(city_country('paris', 'france', population=2161000, language='french'))