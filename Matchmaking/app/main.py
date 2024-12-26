from fastapi import FastAPI, HTTPException
import json
import os

app = FastAPI()

# Load mock data
base_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(base_dir, "./mock_data/users.json")

# Read the mock data
base_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.abspath(os.path.join(base_dir, "./mock_data/users.json"))

if not os.path.exists(data_path):
    raise FileNotFoundError(f"Mock data file not found at {data_path}")

# Read the mock data
with open(data_path, "r") as f:
    users_data = json.load(f)

@app.get("/")
def health_check():
    """
    Health check endpoint to verify the API is running.
    """
    return {"message": "Welcome to the Dating App Matchmaking API"}

@app.post("/api/v1/match/{user_id}")
def generate_matches(user_id: str):
    """
    Generate matches for a user based on compatibility.
    """
    user = next((u for u in users_data if u["id"] == user_id), None)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    matches = []
    for candidate in users_data:
        if candidate["id"] != user_id and candidate["gender"] == user["interested_in"]:
            # Calculate compatibility score
            common_interests = set(user["interests"]) & set(candidate["interests"])
            common_hobbies = set(user["hobbies"]) & set(candidate["hobbies"])
            score = 0.5 * (len(common_interests) / len(user["interests"]) if user["interests"] else 0) + \
                    0.5 * (len(common_hobbies) / len(user["hobbies"]) if user["hobbies"] else 0)
            
            matches.append({
                "user_id": candidate["id"],
                "name": candidate["name"],
                "compatibility_score": round(score, 2),
                "common_interests": list(common_interests),
                "common_hobbies": list(common_hobbies)
            })
    
    # Sort matches by compatibility score in descending order
    matches = sorted(matches, key=lambda x: x["compatibility_score"], reverse=True)
    return matches

@app.get("/api/v1/compatibility/{user_id1}/{user_id2}")
def check_compatibility(user_id1: str, user_id2: str):
    """
    Check compatibility between two users.
    """
    user1 = next((u for u in users_data if u["id"] == user_id1), None)
    user2 = next((u for u in users_data if u["id"] == user_id2), None)
    if not user1 or not user2:
        raise HTTPException(status_code=404, detail="User not found")

    common_interests = set(user1["interests"]) & set(user2["interests"])
    common_hobbies = set(user1["hobbies"]) & set(user2["hobbies"])
    score = 0.5 * (len(common_interests) / len(user1["interests"]) if user1["interests"] else 0) + \
            0.5 * (len(common_hobbies) / len(user1["hobbies"]) if user1["hobbies"] else 0)

    return {
        "user1_id": user_id1,
        "user2_id": user_id2,
        "compatibility_score": round(score, 2)
    }
