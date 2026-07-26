from flask import Flask, request, jsonify

app = Flask(__name__)

@app.post('/proration')
def proration():
    data = request.get_json(silent=True) or {}
    try:
        old_price = float(data['old_price'])
        new_price = float(data['new_price'])
        days_remaining = float(data['days_remaining'])
        days_in_actual_month = float(data['days_in_actual_month'])
        spec = data['spec']
    except (KeyError, TypeError, ValueError):
        return jsonify({'error': 'Invalid request body'}), 400

    if spec == 'v1':
        divisor = 30.0
    elif spec == 'v2':
        if days_in_actual_month <= 0:
            return jsonify({'error': 'days_in_actual_month must be positive'}), 400
        divisor = days_in_actual_month
    else:
        return jsonify({'error': 'spec must be v1 or v2'}), 400

    charge = (new_price - old_price) * (days_remaining / divisor)
    return jsonify({'charge': charge})

@app.get('/')
def home():
    return jsonify({'status': 'ok', 'endpoint': '/proration'})