# from flask import Flask, request, jsonify

# app = Flask(__name__)

# # Callback URL to handle the polling response
# @app.route('/callback-endpoint', methods=['POST'])
# def handle_polling_result():
#     data = request.json  # Get the JSON data sent by KopoKopo
#     print("Received data:", data)  # Print or process the data as needed
    
#     # For now, just return a success response
#     return jsonify({"status": "success", "message": "Polling result received!"}), 200

# if __name__ == '__main__':
#     app.run(debug=True, port=5000)


from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import JSONResponse

app = FastAPI()

# Create a Pydantic model for the expected JSON payload
class PollingResult(BaseModel):
    id: str
    type: str
    attributes: dict

# Define the endpoint for receiving polling data
@app.post("/callback-endpoint")
async def handle_polling_result(polling_result: PollingResult):
    # Print the received data
    print("Received polling result:", polling_result)

    # Process or store the data as needed
    # For example, if there are transactions, you can extract them:
    if polling_result.attributes.get('transactions'):
        transactions = polling_result.attributes['transactions']
        print("Transactions received:", transactions)

    # Send a response indicating success
    return JSONResponse(content={"status": "success", "message": "Polling result received!"}, status_code=200)

# To run the server, you can use `uvicorn` from the terminal




