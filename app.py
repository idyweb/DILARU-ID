import didkit
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/verify_age/<user_did>', methods=['GET'])
def verify_age(user_did):
    # Resolve the user's DID to get their DID document
    user_did_document = didkit.resolve(user_did)

    # Extract age-related information from the DID document
    age_credential = user_did_document.get("ageCredential")  # Assuming the age information is stored this way

    # Simulated age required to purchase the product
    required_age = 18

    # Check if the user is above the required age
    if age_credential and age_credential >= required_age:
        # Return a JSON response indicating the user is suitable for purchase
        return jsonify({"message": "User is suitable for purchase."})
    else:
        # Return a JSON response indicating the user does not meet age requirements
        return jsonify({"message": "User does not meet age requirements."}), 403

if __name__ == '__main__':
    app.run(debug=True)
