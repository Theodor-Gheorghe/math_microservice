from flask import Blueprint, request, jsonify
from services import (
    calculate_factorial,
    calculate_pow,
    calculate_fibonacci
)
from models import log_request, get_all_requests
from messaging import persist_message  # saves message in simulated messaging system
from handler import lambda_handler
import os
import json

api = Blueprint('api', __name__)


@api.route('/api/factorial', methods=['GET'])
def factorial():
    # Handles factorial calculation endpoint
    try:
        number = int(request.args.get('number', ''))
        result = calculate_factorial(number)

        log_request('factorial', {'number': number}, result)
        persist_message('factorial', {'number': number}, result)

        return jsonify({
            'operation': 'factorial',
            'input': number,
            'result': result
        })
    except ValueError as ve:
        return jsonify({'error': str(ve)}), 400
    except Exception:
        return jsonify({'error': 'Internal error'}), 500


@api.route('/api/pow', methods=['GET'])
def power():
    # Handles power calculation endpoint
    try:
        base = float(request.args.get('base', ''))
        exponent = float(request.args.get('exponent', ''))
        result = calculate_pow(base, exponent)

        log_request('power', {'base': base, 'exponent': exponent}, result)
        persist_message('power', {'base': base, 'exponent': exponent}, result)

        return jsonify({
            'operation': 'power',
            'base': base,
            'exponent': exponent,
            'result': result
        })
    except Exception:
        return jsonify({'error': 'Invalid parameters'}), 400


@api.route('/api/fibonacci', methods=['GET'])
def fibonacci():
    # Handles Fibonacci calculation endpoint
    try:
        number = int(request.args.get('number', ''))
        result = calculate_fibonacci(number)

        log_request('fibonacci', {'number': number}, result)
        persist_message('fibonacci', {'number': number}, result)

        return jsonify({
            'operation': 'fibonacci',
            'input': number,
            'result': result
        })
    except ValueError as ve:
        return jsonify({'error': str(ve)}), 400
    except Exception:
        return jsonify({'error': 'Internal error'}), 500


@api.route('/api/logs', methods=['GET'])
def get_logs():
    # Returns all requests from the database
    try:
        logs = get_all_requests()
        return jsonify(logs)
    except Exception:
        return jsonify({'error': 'Could not access database'}), 500


@api.route('/api/messages', methods=['GET'])
def get_messages():
    # Returns all messages from the log file
    try:
        path = 'messages/messages.jsonl'
        if not os.path.exists(path):
            return jsonify([])

        with open(path, 'r') as f:
            lines = f.readlines()
            messages = [json.loads(line) for line in lines]

        return jsonify(messages)
    except Exception:
        return jsonify({'error': 'Could not read messages'}), 500


@api.route('/serverless', methods=['POST'])
def serverless_sim():
    # Simulates a serverless function call
    try:
        event = request.get_json()
        result = lambda_handler(event)
        return jsonify(result)
    except Exception:
        return jsonify({'error': 'Serverless simulation error'}), 500
