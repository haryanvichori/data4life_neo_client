from main import prepare_data

raw_data = {
    'links': {'self': 'http://www.neowsapp.com/rest/v1/neo/3532365?api_key=ewq4iP4V8O1FGmdY39dY6aRJ7TzeBcaRhg5A8tfu'},
    'id': '3532365', 'neo_reference_id': '3532365', 'name': '(2010 MH1)',
    'nasa_jpl_url': 'http://ssd.jpl.nasa.gov/sbdb.cgi?sstr=3532365', 'absolute_magnitude_h': 21.3,
    'estimated_diameter': {
        'kilometers': {'estimated_diameter_min': 0.1460679643, 'estimated_diameter_max': 0.3266178974},
        'meters': {'estimated_diameter_min': 146.0679642714, 'estimated_diameter_max': 326.6178974458},
        'miles': {'estimated_diameter_min': 0.090762397, 'estimated_diameter_max': 0.2029508896},
        'feet': {'estimated_diameter_min': 479.2256199, 'estimated_diameter_max': 1071.581062656}},
    'is_potentially_hazardous_asteroid': False, 'close_approach_data': [
        {'close_approach_date': '2015-09-10', 'close_approach_date_full': '2015-Sep-10 08:30',
         'epoch_date_close_approach': 1441873800000,
         'relative_velocity': {'kilometers_per_second': '9.9341869749', 'kilometers_per_hour': '35763.0731095124',
                               'miles_per_hour': '22221.7828440745'},
         'miss_distance': {'astronomical': '0.4805302904', 'lunar': '186.9262829656',
                           'kilometers': '71886307.914321448', 'miles': '44668080.4515460624'},
         'orbiting_body': 'Earth'}], 'is_sentry_object': False}


def test_prepare_data():
    data = prepare_data(raw_data)
    neo = dict()
    neo["id"] = raw_data["id"]
    neo["name"] = raw_data["name"]
    neo["nasa_jpl_url"] = raw_data["nasa_jpl_url"]
    neo["close_approach_date"] = raw_data["close_approach_data"][0]["close_approach_date_full"]
    neo["is_potentially_hazardous_asteroid"] = raw_data["is_potentially_hazardous_asteroid"]

    assert neo == data

