# Little-Lemon-Web-Application

## Description
This is the final assignment for the Bakend Developer Capstone Course of the Meta Backend Developer Professional Certificate on Coursera.
<br> <br>

## Project Structure
The project is composed of one app, `Restaurant`. The app serves API endpoints of the project, as well as the frontend of the application and its static content. The primary configurations for the project are stored within the `LittleLemon` directory.
<br> <br>

## Installation

install the dependencies
```jsx
pipenv install
```

Activate the virtual environment

```jsx
pipenv shell
```
<br>

## Setup
The default database settings are

```jsx
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'LittleLemon_Restaurant',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        }
    }
}
```
💡 Change those settings according to your local setup.
<br>
<br>

Apply the migrations
```jsx
python manage.py migrate
```
<br>

Example of super user credentials:
* username: superuser
* password: littlelemon!!!123

## Endpoints
The `Restaurant` app has a total of 12 endpoints, 4 for API testing, 1 for token generation, and 7 for static content and the front-end of the application. Additionally, `Djoser` endpoints are available.
<br>

Each endpoint of the 4 endpoints for API testing requires a Token for authorization.
<br>

### Endpoints for `Restaurant` app
```jsx
http:127.0.0.1:8000/restaurant/booking/tables/
http:127.0.0.1:8000/restaurant/booking/tables/<int:pk>
http:127.0.0.1:8000/restaurant/api/menu/
http:127.0.0.1:8000/restaurant/api/menu/<int:pk>

http:127.0.0.1:8000/restaurant/
http:127.0.0.1:8000/restaurant/about/
http:127.0.0.1:8000/restaurant/menu/
http:127.0.0.1:8000/restaurant/menu_item/<int:pk>/
http:127.0.0.1:8000/restaurant/book/
http:127.0.0.1:8000/restaurant/bookings/?date=YYYY-MM-DD
http:127.0.0.1:8000/restaurant/reservations/

http:127.0.0.1:8000/restaurant/api-token-auth/
```
<br>

* For the API endpoints, we have:

http:127.0.0.1:8000/restaurant/booking/tables/
| Method | Action | TOKEN AUTH | STATUS CODE |
| --- | --- | --- | --- |
| GET | Retrieves all bookings | Yes | 200 |
| POST | Creates a booking | Yes | 201 |
<br>

http:127.0.0.1:8000/api/bookings/pk
| Method | Action | TOKEN AUTH | STATUS CODE |
| --- | --- | --- | --- |
| GET | Retrieves the booking details | Yes | 200 |
| PUT | Update the booking | Yes | 200 |
| PATCH | Partially update the booking | Yes | 200 |
| DELETE | Delete the booking | Yes | 200 |
<br>

http:127.0.0.1:8000/restaurant/api/menu/
| Method | Action | TOKEN AUTH | STATUS CODE |
| --- | --- | --- | --- |
| GET | Retrieves all menu items | Yes | 200 |
| POST | Creates a menu item | Yes | 201 |
<br>

http:127.0.0.1:8000/restaurant/api/menu/pk/
| Method | Action | TOKEN AUTH | STATUS CODE |
| --- | --- | --- | --- |
| GET | Retrieves the menu item details | Yes | 200 |
| PUT | Update the menu item | Yes | 200 |
| PATCH | Partially update the menu item | Yes | 200 |
| DELETE | Delete the menu item | Yes | 200 |
<br>
<br>

* To implement the `TokenAutentication` feature of Django REST framework, we will use this endpoint:

http:127.0.0.1:8000/restaurant/api-token-auth/
| Method | Action | TOKEN AUTH | STATUS CODE |
| --- | --- | --- | --- |
| POST | Returns a Token String | No | 200 |

<br>
<br>

In Insomnia, to generate the token, add user and password credentials in a `POST` request as follow:

![Untitled](./static/token%20generation.PNG)
<br>
<br>
To get the response from a secured URL, select the Auth tab in Insomnia, choose the Bearer token from the drop down, and enter the token generated in the previous endpoint and then press the send button:

![Untitled](./static/menu%20items%20api.PNG)
<br>
<br>


* The rest endpoints are designed to serve the static content and the front-end of the application, no need for authorization.

### Endpoints for `djoser` app
```jsx
http://127.0.0.1:8000/auth/users/
http://127.0.0.1:8000/auth/users/me/
http://127.0.0.1:8000/auth/users/confirm/
http://127.0.0.1:8000/auth/users/resend_activation/
http://127.0.0.1:8000/auth/users/set_password/
http://127.0.0.1:8000/auth/users/reset_password/
http://127.0.0.1:8000/auth/users/reset_password_confirm/
http://127.0.0.1:8000/auth/users/set_username/
http://127.0.0.1:8000/auth/users/reset_username/
http://127.0.0.1:8000/auth/users/reset_username_confirm/
```
<br>

http://127.0.0.1:8000/auth/users/
| Method | Action | STATUS CODE | TOKEN AUTH |
| --- | --- | --- | --- |
| GET | Retrieves all users | 200 | No |
| POST | Creates a user | 201 | No |

💡 Please refer to the [Djoser documentation](https://djoser.readthedocs.io/en/latest/getting_started.html#available-endpoints) for further usage on these endpoints.
<br> <br>


## Testing
There are a total of 12.
<br>

Run the tests
```jsx
python manage.py test
```
<br>

It should output something similar to this
```jsx
Found 12 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
............
----------------------------------------------------------------------
Ran 12 tests in 4.141s

OK
Destroying test database for alias 'default'...
```
<br>

<aside>💡 These tests intrinsically test the models and the views.</aside>


