# Overview:
The application is developed using Django and Postgresql as database


# Architecture:
## Models :
* TomatoPlant: has the following fields:
- name
- number_of_plants
- harvest_per_year
- environment_condition
- soil_condition

* Production: has the following fields:
- tomato_plant (foreign key)
- harvest_date
- weight_in_ton

* Sensor: has the following fields:
- id


* SensorData: has the following fields:
- sensor_id (foreign key)
- time
- target : The target that the sensor is attached to. That is environment or soil.
- data

I opted to make data a json field because this is an easier approach (given the time constraints) and it's more flexible (for example, some fields might not be present in data, no consistent schema)

## Endpoints :
All endpoints can be viewed in `/swagger-ui`
### CRUD:
* GET, PUT, PATCH, DELETE for each of those ressources: tomatoes, production, sensor data. Those operations have the following URI: `/api/ressource_name/{id}` and will modify/fetch/delete 1 instance of the ressource.
* GET, POST for each of those ressources: tomatoes, production, sensor data. Those operations have the following URI: `/api/ressource_name/`. the POST operation will create 1 instance and the GET operation will list all instances of the ressource.

The CRUD operations are generated with Django models, serializers and views.

### Other endpoints:
The following endpoints will be json-rendered if header `'Accept: application/json'` is used, else will be html rendered (called from within the browser)
* `/environment`: equivalent to `environment.json`
* `/soil`: equivalent to `soil.json`
* `/production`: equivalent to `production.json`
* `/tomatoes`: equivalent to `tomatoes.json`
* `/days`: returns a list of days that have the second highest temperature 