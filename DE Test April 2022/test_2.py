# A team of analysts wish to discover how far people are travelling to their nearest
# desired court. We have provided you with a small test dataset so you can find out if
# it is possible to give the analysts the data they need to do this. The data is in
# `people.csv` and contains the following columns:
# - person_name
# - home_postcode
# - looking_for_court_type

# The courts and tribunals finder API returns a list of the 10 nearest courts to a
# given postcode. The output is an array of objects in JSON format. The API is
# accessed by including the postcode of interest in a URL. For example, accessing
# https://courttribunalfinder.service.gov.uk/search/results.json?postcode=E144PU gives
# the 10 nearest courts to the postcode E14 4PU. Visit the link to see an example of
# the output.

# Below is the first element of the JSON array from the above API call. We only want the
# following keys from the json:
# - name
# - dx_number
# - distance
# dx_number is not always returned and the "types" field can be empty.

"""
[
    {
        "name": "Central London Employment Tribunal",
        "lat": 51.5158158439741,
        "lon": -0.118745425821452,
        "number": null,
        "cci_code": null,
        "magistrate_code": null,
        "slug": "central-london-employment-tribunal",
        "types": [
            "Tribunal"
        ],
        "address": {
            "address_lines": [
                "Victory House",
                "30-34 Kingsway"
            ],
            "postcode": "WC2B 6EX",
            "town": "London",
            "type": "Visiting"
        },
        "areas_of_law": [
            {
                "name": "Employment",
                "external_link": "https%3A//www.gov.uk/courts-tribunals/employment-tribunal",
                "display_url": "<bound method AreaOfLaw.display_url of <AreaOfLaw: Employment>>",
                "external_link_desc": "Information about the Employment Tribunal"
            }
        ],
        "displayed": true,
        "hide_aols": false,
        "dx_number": "141420 Bloomsbury 7",
        "distance": 1.29
    },
    etc
]
"""

# Use this API and the data in people.csv to determine how far each person's nearest
# desired court is. Generate an output (of whatever format you feel is appropriate)
# showing, for each person:
# - name
# - type of court desired
# - home postcode
# - nearest court of the right type
# - the dx_number (if available) of the nearest court of the right type
# - the distance to the nearest court of the right type

import csv
import requests as req

COURT_API_URL = "https://courttribunalfinder.service.gov.uk/search/results.json?postcode="

def get_court_data(postcode: str) -> list:
    """Function to get court data from the API for a given postcode."""

    if not isinstance(postcode, str):
        raise TypeError("Error: Please input a valid postcode.")

    if len(postcode) < 6:
        raise ValueError("Error: Postcode not long enough. Please check postcode is correct.")

    response = req.get(f"{COURT_API_URL}{postcode}")

    json = response.json()

    return json


def read_csv() -> list:
    """Function to read data from people.csv"""

    people_list = []

    with open("people.csv", "r") as people_csv:
        contents = csv.DictReader(people_csv)

        for row in contents:
            people_list.append(row)

    return people_list


def create_nearest_courts_csv() -> None:
    """Create an output csv file with initial line if none exists."""
    with open("nearest_courts.csv", "w") as court_csv:
        court_csv.write("name,desired_court_type,home_postcode,nearest_court,dx_number,distance\n")


def write_to_nearest_courts_csv(person: dict, court: dict) -> None:
    """Function to write desired data in csv format"""

    with open("nearest_courts.csv", "a") as court_csv:
        name = person["person_name"]
        desired_court_type = person["looking_for_court_type"]
        home_postcode = person["home_postcode"]
        nearest_court = court["name"]
        dx_number = court["dx_number"]
        distance = court["distance"]
        court_csv.write(f"{name},{desired_court_type},{home_postcode},{nearest_court},{dx_number},{distance}\n")


if __name__ == "__main__":
    create_nearest_courts_csv()
    people = read_csv()

    for person in people:
        possible_courts = get_court_data(person["home_postcode"])
        matching_courts = []
        for court in possible_courts:
            if person["looking_for_court_type"] in court["types"]:
                matching_courts.append(court)

        matching_courts.sort(key=lambda x: x["distance"])

        write_to_nearest_courts_csv(person, matching_courts[0])







