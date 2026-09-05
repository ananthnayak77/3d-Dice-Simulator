from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# paste this exact block here to fix CORS without any installation:
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

def roll_dice(sides=6):
    return random.randint(1, sides)

@app.route('/play', methods=['POST'])
def play():
    data = request.get_json()
    rounds = int(data['rounds'])
    target_score = int(data['target_score'])
    total = 0
    history = []
    roundnum = 0

    while total < target_score and roundnum < rounds:
        roundnum += 1
        roll = roll_dice()
        total += roll
        history.append(roll)

    if total >= target_score:
        message = f"🎉 Congratulations! You reached {target_score} in {roundnum} rounds."
    else:
        message = f"😢 Sorry, you didn’t reach {target_score} in {roundnum} rounds."

    return jsonify({"history": history, "message": message})

if __name__ == '__main__':
    app.run(debug=True)
