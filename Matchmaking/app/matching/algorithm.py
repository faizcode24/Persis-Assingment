# from typing import List, Dict, Tuple
# import numpy as np

# def calculate_compatibility(user1: Dict, user2: Dict) -> float:
#     score = 0
#     # Common hobbies
#     common_hobbies = set(user1["hobbies"]) & set(user2["hobbies"])
#     score += len(common_hobbies) * 2

#     # Common interests
#     common_interests = set(user1["interests"]) & set(user2["interests"])
#     score += len(common_interests) * 3

#     # Similar location
#     if user1["location"] == user2["location"]:
#         score += 5

#     # Education level match
#     if user1["education_level"] == user2["education_level"]:
#         score += 4

#     # Personality traits similarity 
#     traits1 = set(user1["personality_traits"])
#     traits2 = set(user2["personality_traits"])
#     score += len(traits1 & traits2) / len(traits1 | traits2) * 5

#     return score

# def generate_matches(user_id: str, all_users: List[Dict]) -> List[Tuple[str, float]]:
#     current_user = next(user for user in all_users if user["id"] == user_id)
#     matches = [
#         (user["id"], calculate_compatibility(current_user, user))
#         for user in all_users if user["id"] != user_id
#     ]
#     matches.sort(key=lambda x: x[1], reverse=True)
#     return matches

from typing import List, Dict, Tuple
import numpy as np


def calculate_compatibility(user1: Dict, user2: Dict) -> float:
    score = 0
    weights = {
        "hobbies": 2,
        "interests": 3,
        "location": 5,
        "education_level": 4,
        "traits": 5,
        "age": 3,
        "occupation": 2,
    }

    # Common hobbies
    common_hobbies = set(user1["hobbies"]) & set(user2["hobbies"])
    score += len(common_hobbies) * weights["hobbies"]

    # Common interests
    common_interests = set(user1["interests"]) & set(user2["interests"])
    score += len(common_interests) * weights["interests"]

    # Similar location
    if user1["location"] == user2["location"]:
        score += weights["location"]

    # Education level match
    if user1["education_level"] == user2["education_level"]:
        score += weights["education_level"]

    # Personality traits similarity
    traits1 = set(user1["personality_traits"])
    traits2 = set(user2["personality_traits"])
    if traits1 and traits2:
        score += len(traits1 & traits2) / len(traits1 | traits2) * weights["traits"]

    # Age compatibility
    age_difference = abs(user1["age"] - user2["age"])
    if age_difference <= 5:  # Adjust tolerance range as needed
        score += weights["age"]

    # Occupation compatibility
    if user1["occupation"] == user2["occupation"]:
        score += weights["occupation"]

    # Geographical distance (optional, requires lat/lon)
    if "coordinates" in user1 and "coordinates" in user2:
        lat1, lon1 = user1["coordinates"]
        lat2, lon2 = user2["coordinates"]
        distance = np.sqrt((lat1 - lat2) ** 2 + (lon1 - lon2) ** 2)
        if distance < 50:  # Assume 50 units as "close"
            score += weights["location"] / (1 + distance / 10)

    return score


def generate_matches(user_id: str, all_users: List[Dict]) -> List[Tuple[str, float]]:
    current_user = next((user for user in all_users if user["id"] == user_id), None)
    if not current_user:
        return []

    matches = []
    for user in all_users:
        if user["id"] != user_id:
            compatibility_score = calculate_compatibility(current_user, user)
            matches.append((user["id"], round(compatibility_score, 2)))

    # Sort matches by compatibility score in descending order
    matches.sort(key=lambda x: x[1], reverse=True)
    return matches