from flask import Flask, make_response

# Setting constants for the is_prime function
INVALID_INPUT = -2
INVALID_NUM = -1
PRIME = 1
NOT_PRIME = 0

app = Flask(__name__)


# Function to determine prime number
def is_prime(num):
    try:
        num = int(num)
    except:
        return INVALID_INPUT

    if num < 1:
        return INVALID_NUM
    elif num == 1:
        return NOT_PRIME
    else:
        for i in range(2, round(num / 2) + 1):
            if num % i == 0:
                return NOT_PRIME
        return PRIME


# Route for is_prime
@app.route("/<num>")
def route_is_prime(num):
    result = is_prime(num)
    if result == INVALID_INPUT:
        response = {"Number": num, "message": "Invalid input, it needs to be an integer."}
        return make_response(response, 400)
    elif result == INVALID_NUM:
        response = {"Number": num, "message": "Invalid number, it needs to be greater than 0."}
        return make_response(response, 400)
    elif result == PRIME:
        response = {"Number": num, "isPrime": True}
        return make_response(response)
    elif result == NOT_PRIME:
        response = {"Number": num, "isPrime": False}
        return make_response(response)
    else:
        response = {"Number": num, "message": "Something went wrong."}
        return make_response(response, 500)


if __name__ == '__main__':
    app.run(debug=False, host="127.0.0.1", port=5000)
