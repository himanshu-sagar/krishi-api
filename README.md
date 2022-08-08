# krishi-api

### [Krishi - API Heroku](https://krishi-app.herokuapp.com/)
### [Postman API DOC](https://documenter.getpostman.com/view/15206589/UyrGCZqA)

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
# Steps To Run
- [Install Poetry](https://python-poetry.org/docs/)
- Run These Commands in linux terminal to start app
    
    ```bash
    1. Create Virtual Env & Install All Dependencies: poetry install
    2. Activate Environment: poetry shell
    3. Add .env File with: SECRET_KEY, DATABASE_URL_POSTGRES, WEATHER_API_KEY
    4. Run App: gunicorn -w 1 -b 0.0.0.0:8088 "application:initialize_app(testing=False)" --timeout 9600 --reload
    ```
