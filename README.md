
# Matchmaking App

This Matchmaking App is designed to help users find potential matches based on various compatibility factors. The app uses algorithms to evaluate factors such as common interests, hobbies, location, and personality traits to suggest the best matches for each user.




## Features

- Health Check: Verify that the app is running correctly.
- Generate Matches for a User: Get a list of recommended matches for a given user.
- Check Compatibility Between Two Users: Evaluate compatibility between two users.




## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/matchmaking-app.git
cd matchmaking-app

```

Create a virtual environment:

```bash
python -m venv venv
```
Activate the virtual environment:

 ```bash
.\venv\Scripts\activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

## API Endpoints

Health Check

Method: GET

URL: /

-Exprected Response
```bash
{
    "message": "Welcome to the Dating App Matchmaking API"
}
```

Generate Matches for a User

Method: POST

- URL: /api/v1/match/{user_id}

Request Body: None required

Expected Response: 
- A list of recommended matches based on compatibility factors.

Check Compatibility Between Two Users

Method: GET

- URL: /api/v1/compatibility/{user_id1}/{user_id2}

Expected Response: Compatibility score between two users.


### Technical Implementation
- Algorithm Overview

The app uses a compatibility scoring algorithm that takes into account factors such as:

- Common hobbies: Score based on overlap in hobbies.
- Common interests: Score based on shared interests.
- Location match: Score based on similarity in user location.
- Education level match: Score based on similarity in education levels.
- Personality traits similarity: Score based on overlap in personality traits.

### Code Structure
The app is organized into different modules, each responsible for handling specific features, such as:

- main.py: Contains routes and API endpoints.
- models.py: Defines data models for users and matches.
- utils.py: Contains helper functions for processing data and matching logic.

Libraries Used

- FastAPI: For building the API.
- Uvicorn: ASGI web server for serving the FastAPI app.
- numpy: For performing mathematical calculations.
- set: To manage sets of data for comparing common interests, hobbies, and traits.

### Future Improvements
- Scalability Considerations: Implement caching, use asynchronous database calls, and optimize data queries for large-scale deployments.
- Additional Features: Add chat functionality, user profiles, notifications, and machine learning models for better match recommendations.



