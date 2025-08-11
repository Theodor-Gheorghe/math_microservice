from services import calculate_factorial, calculate_pow, calculate_fibonacci

def lambda_handler(event):
    """
    Simulează o funcție serverless: primește un `event` (JSON) și returnează un rezultat.
    """
    operation = event.get('operation')
    input_data = event.get('input', {})

    try:
        if operation == 'factorial':
            number = int(input_data.get('number', 0))
            result = calculate_factorial(number)

        elif operation == 'power':
            base = float(input_data.get('base', 0))
            exponent = float(input_data.get('exponent', 0))
            result = calculate_pow(base, exponent)

        elif operation == 'fibonacci':
            number = int(input_data.get('number', 0))
            result = calculate_fibonacci(number)

        else:
            return {'error': f'Operatie necunoscuta: {operation}'}

        return {
            'operation': operation,
            'input': input_data,
            'result': result
        }

    except Exception as e:
        return {'error': str(e)}