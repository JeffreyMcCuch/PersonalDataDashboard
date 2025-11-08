Personal Data Dashboard

Description:
This is a simple Personal Data Dashboard built using Python and Streamlit. The dashboard allows users to enter their first and last name,
input a favorite number to calculate its square root, enter a 5-digit ZIP code to fetch local weather information via the OpenWeatherMap API, 
and upload a profile picture to display in the dashboard. The app uses session state to manage multi-step inputs and ensure a smooth user experience.

Features

- Multi-step input workflow through session states: Name → Favorite Number → ZIP Code → Profile Picture → Finished Dashboard

- Square root calculation with validation for negative numbers

- Weather API integration **requires an API key in GetWeatherAPI.py**

- File uploader for profile pictures (jpg, jpeg, png)

Input validation:

- Names cannot be empty

- Favorite number cannot be negative

- ZIP code must be exactly 5 digits

Dependencies

- Python 3.x

Libraries:

streamlit

requests

math (built-in)
