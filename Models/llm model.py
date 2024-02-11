import requests

# Replace with your actual API base URL, endpoint, and credentials
API_BASE_URL = ""
API_ENDPOINT = ""
API_KEY = ""

def send_request_to_llm(prompt):
    headers = {"Authorization": f"Bearer {API_KEY}"}
    data = {"prompt": prompt}
    response = requests.post(f"{API_BASE_URL}{API_ENDPOINT}", headers=headers, json=data)

    if response.status_code == 200:
        response_data = response.json()
        # Process the response data (e.g., extract generated text)
        return response_data["text"]
    else:
        # Handle API error, provide feedback to user
        print(f"API error: {response.text}")
        return None

# Example usage in your Flask app
@app.route("/ask", methods=["POST"])
def ask_llm():
    prompt = request.json["prompt"]
    response = send_request_to_llm(prompt)
    # Display response to user
    return jsonify({"response": response})
