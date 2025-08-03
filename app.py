from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import time

app = Flask(__name__)
CORS(app)  # Allow all origins

# 🔐 Replace with your real API token
REPLICATE_API_TOKEN = "your_replicate_api_token"

# Replace with SDXL or any model version you choose
MODEL_VERSION = "a9758cb3b1b20fcf1ec248fd5df8de390a685384f9f5b8e205195de76a8a65d3"  # SDXL v1.0

@app.route("/generate", methods=["POST"])
def generate_image():
    data = request.get_json()
    prompt = data.get("prompt", "")
    if not prompt:
        return jsonify({"error": "Missing prompt"}), 400

    print(f"Received prompt: {prompt}")

    # Step 1: Create Prediction
    headers = {
        "Authorization": f"Token {REPLICATE_API_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "version": MODEL_VERSION,
        "input": {
            "prompt": prompt,
            "width": 768,
            "height": 768
        }
    }
    response = requests.post("https://api.replicate.com/v1/predictions", headers=headers, json=payload)
    if response.status_code != 201:
        print("Error starting prediction:", response.json())
        return jsonify({"error": "Failed to create prediction"}), 500

    prediction = response.json()
    prediction_id = prediction["id"]

    # Step 2: Poll Until Complete
    status_url = f"https://api.replicate.com/v1/predictions/{prediction_id}"
    while True:
        poll_resp = requests.get(status_url, headers=headers)
        result = poll_resp.json()
        if result["status"] == "succeeded":
            image_url = result["output"][0]
            return jsonify({"imageUrl": image_url})
        elif result["status"] == "failed":
            return jsonify({"error": "Prediction failed"}), 500

        time.sleep(2)

if __name__ == "__main__":
    app.run(debug=True)
