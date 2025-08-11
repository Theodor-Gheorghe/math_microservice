from handler import lambda_handler

# Test factorial
event1 = {
    'operation': 'factorial',
    'input': {'number': 5}
}

# Test power
event2 = {
    'operation': 'power',
    'input': {'base': 2, 'exponent': 4}
}

# Test fibonacci
event3 = {
    'operation': 'fibonacci',
    'input': {'number': 7}
}

for event in [event1, event2, event3]:
    print(lambda_handler(event))