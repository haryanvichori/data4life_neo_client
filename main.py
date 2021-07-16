import os
import requests
import logging

logger = logging.getLogger(__name__)

API_KEY = os.environ.get("NASA_API_KEY", "ewq4iP4V8O1FGmdY39dY6aRJ7TzeBcaRhg5A8tfu")
START_DATE = "2021-07-25"
END_DATE = "2021-07-31"


url = f"https://api.nasa.gov/neo/rest/v1/feed?start_date={START_DATE}&end_date={END_DATE}&api_key={API_KEY}"


def main():
    response = requests.get(url)
    response_json = response.json()

    neo_data = response_json["near_earth_objects"]

    for date in neo_data:
        neo_list = neo_data[date]
        for neo_raw_obj in neo_list:
            data = prepare_data(neo_raw_obj)
            send_data(data)


def prepare_data(neo_raw_json):
    neo_final = dict()
    neo_final["close_approach_date"] = neo_raw_json["close_approach_data"][0]["close_approach_date_full"]
    neo_final["id"] = neo_raw_json["id"]
    neo_final["name"] = neo_raw_json["name"]
    neo_final["nasa_jpl_url"] = neo_raw_json["nasa_jpl_url"]
    neo_final["is_potentially_hazardous_asteroid"] = neo_raw_json["is_potentially_hazardous_asteroid"]
    return neo_final


def send_data(json_data):
    url = os.environ.get("NEO_SERVER_POST_ENDPOINT", "http://127.0.0.1:5000/neo")
    logger.info(f'posting data for {json_data["name"]}')
    requests.post(url=url, json=json_data)


main()