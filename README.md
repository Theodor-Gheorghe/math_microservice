Math Microservice

This is a Python project that lets you do some basic math operations (factorial, power, Fibonacci) using a web API. 
It also saves every request in a database and logs messages to a file. You can run it locally or with Docker.

# What does it do?

- You can ask for factorial, power, or Fibonacci numbers using HTTP requests.
- Every request is saved in a SQLite database so you can check what was calculated.
- Each request also gets logged as a message in a `.jsonl` file (like a simple messaging system).
- There’s a function that acts like a serverless handler, so you can test how it would work in a cloud function.
- You can run everything in Docker if you want.

# How to run it

1. Install dependencies
   ```
   pip install -r requirements.txt
   ```

2. Start the app
   ```
   python app.py
   ```
   The API will be at `http://localhost:5000`.

3. Try the API
   - Open your browser or use Postman/curl:
     - `/api/factorial?number=5`
     - `/api/pow?base=2&exponent=4`
     - `/api/fibonacci?number=7`
     - `/api/logs` (shows all requests from the database)
     - `/api/messages` (shows all messages from the log file)
     - `/serverless` (POST with JSON to test the serverless handler)

4. Test the handler directly
   ```
   python test_handler.py
   ```
   This runs some sample events and prints the results.

!!! How to use Docker

1. **Build the image**
   ```sh
   docker build -t math-microservice .
   ```

2. **Run the container**
   ```sh
   docker run -p 5000:5000 math-microservice
   ```
   Now the app is running in Docker at `http://localhost:5000`.

# How does it save stuff?

- Requests go into `database/requests.db` (SQLite). You can see them with `/api/logs`.
- Messages go into `messages/messages.jsonl`. You can see them with `/api/messages`.

# Messaging

Every time you make a request, a message is saved in the `.jsonl` file. This is just a simple way to show how you could send events to a messaging system.

# Serverless simulation

The `lambda_handler` function lets you send a JSON event and get a result, just like you would in AWS Lambda or another cloud function. Try it with a POST to `/serverless`.

