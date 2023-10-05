import requests
import time
import csv
import boto3
from botocore.exceptions import NoCredentialsError

# Replace 'YOUR_API_KEY' with your OpenWeatherMap API key
API_KEY = 'YOUR_API_KEY'

# List of city IDs and city names for multiple cities
CITIES = [
    {"id": 1259229, "name": "Pune, IN"},
    {"id": 2643743, "name": "London, UK"},
    # Add more cities as needed in the same format
]

# OpenWeatherMap API URL
API_BASE_URL = 'http://api.openweathermap.org/data/2.5/weather?id={city_id}&appid={api_key}'

# AWS S3 configuration
AWS_ACCESS_KEY_ID = 'YOUR_ACCESS_KEY_ID'
AWS_SECRET_ACCESS_KEY = 'YOUR_SECRET_ACCESS_KEY'
S3_BUCKET_NAME = 'your-s3-bucket-name'
S3_OBJECT_KEY = 'weather_data.csv'  # Name of the CSV file in S3

# Get the current time as the start time
start_time = time.time()

# Define the duration in seconds (8 hours)
duration = 8 * 3600  # 8 hours * 3600 seconds/hour

# Create a dictionary to store weather data for each city
city_weather_data = {city['name']: [] for city in CITIES}

while True:
    try:
        for city in CITIES:
            # Make a GET request to OpenWeatherMap API for each city
            api_url = API_BASE_URL.format(city_id=city['id'], api_key=API_KEY)
            response = requests.get(api_url)
            
            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                weather_data = response.json()
                
                # Extract relevant weather information
                temperature = weather_data['main']['temp']
                humidity = weather_data['main']['humidity']
                description = weather_data['weather'][0]['description']
                
                # Append data for the city to the dictionary
                city_weather_data[city['name']].append({
                    'Time': time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()),
                    'Temperature (°C)': temperature,
                    'Humidity (%)': humidity,
                    'Condition': description
                })
            else:
                print(f'Failed to fetch data for {city["name"]}. Status code: {response.status_code}')
        
        # Check if 8 hours have passed, and if so, exit the loop
        if time.time() - start_time >= duration:
            break
        
        # Wait for 30 minutes before fetching data again (you can adjust this interval)
        time.sleep(1800)  # 1800 seconds = 30 minutes
        
    except Exception as e:
        print(f'An error occurred: {str(e)}')

# Create or append to a CSV file locally
with open('weather_data.csv', 'a', newline='') as csvfile:
    fieldnames = ['Time'] + [city['name'] for city in CITIES]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    # Write the header if the file is empty
    if csvfile.tell() == 0:
        writer.writeheader()
    
    # Write the weather data for each city to the CSV file
    while True:
        try:
            data_row = {'Time': ''}
            for city in CITIES:
                if city_weather_data[city['name']]:
                    data_row[city['name']] = city_weather_data[city['name']].pop(0)
                else:
                    data_row[city['name']] = ''
            
            writer.writerow(data_row)
            
            # Upload the CSV file to S3
            s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
            s3.upload_file('weather_data.csv', S3_BUCKET_NAME, S3_OBJECT_KEY)
            
            print(f'Data saved to S3 bucket: {S3_BUCKET_NAME}/{S3_OBJECT_KEY}')
            
            # Check if 8 hours have passed, and if so, exit the loop
            if time.time() - start_time >= duration:
                break
            
            # Wait for 30 minutes before writing data again (you can adjust this interval)
            time.sleep(1800)  # 1800 seconds = 30 minutes
        
        except Exception as e:
            print(f'An error occurred: {str(e)}')

# The code will exit after 8 hours of execution.

