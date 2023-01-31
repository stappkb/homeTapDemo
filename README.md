# homeTapDemo

cd into /homeTapDemo/api_demo
# setup api server
$ virtualenv -p python3 .venv

$ source .venv/bin/activate

$ pip install -r requirements.txt

$ python manage.py migrate
# create user
$ python manage.py shell

$ from django.contrib.auth.models import User
$ user = User.objects.create_user(username='fillMeIn', email='fillMeIn', password='fillMeIn')

# should get this as output
$ user.id
1

ctrl + c to exit shell

# start server
$ python manage.py runserver

# generate a token

$ curl  -d 'username=fillMeIn&password=fillMeIn'  http://127.0.0.1:8000/api/login

response should look like this: 
{"token":"2186ef06094ee967eeb9ca0c1ddcb67835b0bda7"}

copy token

$ curl -H 'Authorization:Token 2186ef06094ee967eeb9ca0c1ddcb67835b0bda7'  -d 'address="123 test"&postal_code=12344'  http://127.0.0.1:8000/home_details/get_details/

response should look like this:

{"status":"success","data":{"property/details":{"api_code_description":"ok","api_code":0,"result":{"property":{"air_conditioning":"yes","attic":false,"basement":"full_basement","building_area_sq_ft":1824,"building_condition_score":5,"building_quality_score":3,"construction_type":"Wood","exterior_walls":"wood_siding","fireplace":false,"full_bath_count":2,"garage_parking_of_cars":1,"garage_type_parking":"underground_basement","heating":"forced_air_unit","heating_fuel_type":"gas","no_of_buildings":1,"no_of_stories":2,"number_of_bedrooms":4,"number_of_units":1,"partial_bath_count":1,"pool":true,"property_type":"Single Family Residential","roof_cover":"Asphalt","roof_type":"Wood truss","site_area_acres":0.119,"style":"colonial","total_bath_count":2.5,"total_number_of_rooms":7,"sewer":"municipal","subdivision":"CITY LAND ASSOCIATION","water":"municipal","year_built":1957,"zoning":"RH1"},"assessment":{"apn":"0000 -1111","assessment_year":2015,"tax_year":2015,"total_assessed_value":1300000.0,"tax_amount":15199.86}}}}}

# to toggle between testing and prod external api add a .env file here:
## api_demo/api_demo/.env
## add this values:
$HOME_DETAIL_SERVICE='home_details.services.HouseCanaryService'

$HOME_DETAIL_API_KEY='FillMeIn'
$HOME_DETAIL_API_SECRET='FillMeIn'
