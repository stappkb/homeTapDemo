import os
import uuid
import datetime
from service_objects import services

from django.conf import settings
from django.utils.module_loading import import_string

import requests

def homeDetailsplexer(cls):
    return import_string(getattr(settings, cls.api_settings))

class HouseCanaryService():
    """
    # example: https://api.housecanary.com/v2/property/details?address=123+Main+St&zipcode=94132
    # response = requests.post(url, json=post_data, auth=('my_api_key', 'my_api_secret'))

    params = {'address': '43 Valmonte Plaza',
          'zipcode': '90274'}

    response = requests.get(url, params=params, auth=('my_api_key', 'my_api_secret'))

    """
    base_url = 'https://api.housecanary.com/v2'
    property_details_end_point = 'property/details'

    def get_house_data(self, address, postal_code):
        res = {}
        status = 'success'
        try:
            url = os.path.join(self.base_url, self.property_details_end_point)
            params = {
                'address': address,
                'zipcode': postal_code}
            response = requests.get(url, params=params, auth=(
                settings.HOME_DETAIL_API_KEY, settings.HOME_DETAIL_API_SECRET))
            res = response.json()
            if 'property/details' not in res.keys():
                status = 'error'
        except Exception as e:
            print(f'House Canary Service get_house_data error: {e}')
            status = 'error'
        return status, res

class MockHouseCanaryService():
    def get_house_data(self, address, postal_code):
        res = {
            "property/details": {
                "api_code_description": "ok",
                "api_code": 0,
                "result": {
                    "property": {
                        "air_conditioning": "yes",
                        "attic": False,
                        "basement": "full_basement",
                        "building_area_sq_ft": 1824,
                        "building_condition_score": 5,
                        "building_quality_score": 3,
                        "construction_type": "Wood",
                        "exterior_walls": "wood_siding",
                        "fireplace": False,
                        "full_bath_count": 2,
                        "garage_parking_of_cars": 1,
                        "garage_type_parking": "underground_basement",
                        "heating": "forced_air_unit",
                        "heating_fuel_type": "gas",
                        "no_of_buildings": 1,
                        "no_of_stories": 2,
                        "number_of_bedrooms": 4,
                        "number_of_units": 1,
                        "partial_bath_count": 1,
                        "pool": True,
                        "property_type": "Single Family Residential",
                        "roof_cover": "Asphalt",
                        "roof_type": "Wood truss",
                        "site_area_acres": 0.119,
                        "style": "colonial",
                        "total_bath_count": 2.5,
                        "total_number_of_rooms": 7,
                        "sewer": "municipal",
                        "subdivision" : "CITY LAND ASSOCIATION",
                        "water": "municipal",
                        "year_built": 1957,
                        "zoning": "RH1"
                    },

                    "assessment":{
                        "apn": "0000 -1111",
                        "assessment_year": 2015,
                        "tax_year": 2015,
                        "total_assessed_value": 1300000.0,
                        "tax_amount": 15199.86
                    }
                }
            }
        }
        return 'success', res

@homeDetailsplexer
class HomeDetailsService:
    api_settings = "HOME_DETAIL_SERVICE"