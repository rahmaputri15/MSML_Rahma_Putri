import requests
import time
import random

URL = "http://127.0.0.1:5002/invocations"

def hit_model():
    # Menyesuaikan dengan kolom dataset kamu
    payload = {
        "dataframe_split": {
            "columns": ["Age", "Gender_Encoded", "Blood Type_Encoded", "Medical Condition_Encoded"], 
            "data": [[random.randint(20, 80), random.randint(0, 1), random.randint(0, 7), random.randint(0, 5)]] 
        }
    }
    try:
        response = requests.post(URL, json=payload)
        print(f"Status: {response.status_code}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    print("Memulai simulasi request...")
    while True:
        hit_model()
        time.sleep(random.uniform(1, 3))