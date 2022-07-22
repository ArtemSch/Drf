# Drf test project

## Running project

To run project you should have `docker` and `docker-compose`.

`docker-compose up --build`

Project will be available at HOST_NAME:8000.


To seed the database with food data:
`docker exec -it drftest_web_1 sh`
`python manage.py loaddata $PROJECT_ROOT/foods/fixtures/foods.json`

Follow the link to submit a request:

`0.0.0.0:8000/api/v1/foods/`