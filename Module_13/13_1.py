from flask import Flask
import json

# Setting constants for the is_prime function
INVALID_INPUT = -2
INVALID_NUM = -1
PRIME = 1
NOT_PRIME = 0

app = Flask(__name__)


# Function is prime
def is_prime(num):
    prime_flag = True
    try:
        num = int(num)
    except:
        return INVALID_INPUT

    if num < 1:
        return INVALID_NUM
    elif num == 1:
        return NOT_PRIME
    else:
        for i in range(2, num - 1):
            if num % i == 0:
                prime_flag = False
                break

        if prime_flag:
            return PRIME
        else:
            return NOT_PRIME


# Route for is prime
@app.route("/<num>")
def route_is_prime(num):
    result = is_prime(num)
    if result == INVALID_INPUT:
        result = {"Number": num, "message": "Invalid input, it needs to be an integer."}
        return json.dumps(result), 400
    elif result == INVALID_NUM:
        result = {"Number": num, "message": "Invalid number, it needs to be greater than 0."}
        return json.dumps(result), 400
    elif result == PRIME:
        result = {"Number": num, "isPrime": True}
        return json.dumps(result)
    elif result == NOT_PRIME:
        result = {"Number": num, "isPrime": False}
        return json.dumps(result)
    else:
        result = {"Number": num, "message": "Something went wrong."}
        return json.dumps(result), 500


if __name__ == '__main__':
    app.run(debug=False)
