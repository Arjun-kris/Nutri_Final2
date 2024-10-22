# Nutrivisor

**Nutrivisor** is a web-based application designed to help users track and manage their nutritional intake. The app provides insights on daily food consumption, helps monitor nutritional goals, offers personalized recommendations, and features food recognition to make logging meals easier.

## Features

- **Food Logging**: Users can input their daily meals manually or use the food recognition feature to identify foods from images.
- **Food Recognition**: Upload a picture of your meal, and Nutrivisor will automatically recognize the food and provide nutritional data.
- **Nutritional Insights**: Get a detailed breakdown of calories, proteins, carbs, fats, and other vital nutrients.
- **Goal Tracking**: Set and monitor nutritional goals based on personal health needs.
- **Recommendations**: Receive tailored meal suggestions and tips to meet nutritional targets.
- **Progress Reports**: Track changes over time to maintain a healthy diet.

## Technologies Used

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Flask
- **Database**: SQLite
- **Packages**: No state management, no storage
- **Additional Feature**: Food recognition using a machine learning API

## Getting Started

### Prerequisites

- Python 3.x
- Flask
- SQLite
- Machine learning package for food recognition


### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Arjun-kris/Nutrivisor.git
   cd Nutrivisor
Install backend dependencies:


pip install -r requirements.txt


Set up the database:

SQLite is used as the database. The app will create the database automatically when you run the Flask app.
(some of the missing files can be found in https://drive.google.com/drive/folders/1vvJkeWn4g0l105goKrBlwLEOlnUFNEUr?usp=sharing )


Run the Flask server:


flask run
Open the application in your browser:

http://127.0.0.1:5000

(Optional) Set up food recognition by integrating with a machine learning

Usage
Register or log in to the platform.
Log your meals and view nutritional breakdowns.
Use the food recognition feature to upload images and get nutritional data automatically.
Set daily, weekly, or monthly goals.
Get personalized recommendations and track progress over time.
