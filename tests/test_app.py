import pytest
from fastapi.testclient import TestClient
import sys
import os

# Ensure src is in sys.path for import
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))


import app as app_module
client = TestClient(app_module.app)

def test_signup_success():
    response = client.post("/activities/Chess%20Club/signup?email=tester@mergington.edu")
    assert response.status_code == 200
    assert "Signed up" in response.json()["message"]
    # Clean up
    app_module.activities["Chess Club"]["participants"].remove("tester@mergington.edu")

def test_signup_duplicate():
    # Add participant first
    app_module.activities["Chess Club"]["participants"].append("dupe@mergington.edu")
    response = client.post("/activities/Chess%20Club/signup?email=dupe@mergington.edu")
    assert response.status_code == 400
    assert response.json()["detail"] == "Student is already signed up"
    # Clean up
    app_module.activities["Chess Club"]["participants"].remove("dupe@mergington.edu")

def test_signup_activity_not_found():
    response = client.post("/activities/Nonexistent/signup?email=ghost@mergington.edu")
    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"
