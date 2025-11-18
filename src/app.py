from fastapi import FastAPI, HTTPException

app = FastAPI()

activities = {
   "Chess Club": {
      "description": "Learn strategies and compete in chess tournaments",
      "schedule": "Fridays, 3:30 PM - 5:00 PM",
      "max_participants": 12,
      "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
   },
   "Programming Class": {
      "description": "Learn programming fundamentals and build software projects",
      "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
      "max_participants": 20,
      "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
   },
   "Gym Class": {
      "description": "Physical education and sports activities",
      "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
      "max_participants": 30,
      "participants": ["john@mergington.edu", "olivia@mergington.edu"]
   },
   "Basketball Team": {
      "description": "Competitive basketball training and games",
      "schedule": "Tuesdays and Thursdays, 4:00 PM - 6:00 PM",
      "max_participants": 15,
      "participants": []
   },
   "Swimming Club": {
      "description": "Swimming training and water sports",
      "schedule": "Mondays and Wednesdays, 3:30 PM - 5:00 PM",
      "max_participants": 20,
      "participants": []
   },
   "Art Studio": {
      "description": "Express creativity through painting and drawing",
      "schedule": "Wednesdays, 3:30 PM - 5:00 PM",
      "max_participants": 15,
      "participants": []
   },
   "Drama Club": {
      "description": "Theater arts and performance training",
      "schedule": "Tuesdays, 4:00 PM - 6:00 PM",
      "max_participants": 25,
      "participants": []
   },
   "Debate Team": {
      "description": "Learn public speaking and argumentation skills",
      "schedule": "Thursdays, 3:30 PM - 5:00 PM",
      "max_participants": 16,
      "participants": []
   },
   "Science Club": {
      "description": "Hands-on experiments and scientific exploration",
      "schedule": "Fridays, 3:30 PM - 5:00 PM",
      "max_participants": 20,
      "participants": []
   },
   # Sports related
   "Soccer Team": {
      "description": "Team soccer practice and inter-school matches",
      "schedule": "Mondays and Thursdays, 4:00 PM - 6:00 PM",
      "max_participants": 18,
      "participants": []
   },
   "Tennis Club": {
      "description": "Tennis lessons and friendly competitions",
      "schedule": "Wednesdays, 3:30 PM - 5:00 PM",
      "max_participants": 10,
      "participants": []
   },
   # Artistic
   "Photography Club": {
      "description": "Explore photography techniques and photo editing",
      "schedule": "Fridays, 3:30 PM - 5:00 PM",
      "max_participants": 12,
      "participants": []
   },
   "Dance Crew": {
      "description": "Learn and perform various dance styles",
      "schedule": "Tuesdays, 3:30 PM - 5:00 PM",
      "max_participants": 20,
      "participants": []
   },
   # Intellectual
   "Mathletes": {
      "description": "Participate in math competitions and problem-solving sessions",
      "schedule": "Mondays, 3:30 PM - 5:00 PM",
      "max_participants": 15,
      "participants": []
   },
   "Book Club": {
      "description": "Read and discuss literature from various genres",
      "schedule": "Thursdays, 4:00 PM - 5:00 PM",
      "max_participants": 20,
      "participants": []
   }
}

@app.post("/activities/{activity_name}/signup")
def signup_for_activity(activity_name: str, email: str):
   """Sign up a student for an activity"""
   # Validate activity exists
   if activity_name not in activities:
      raise HTTPException(status_code=404, detail="Activity not found")

   # Get the activity
   activity = activities[activity_name]

   # Validate student is not already signed up (case-insensitive, trimmed)
   normalized_email = email.strip().lower()
   normalized_participants = [e.strip().lower() for e in activity["participants"]]
   if normalized_email in normalized_participants:
     raise HTTPException(status_code=400, detail="Student is already signed up")

   # Add student
   activity["participants"].append(email)
   return {"message": f"Signed up {email} for {activity_name}"}