import hashlib
import requests
from bs4 import BeautifulSoup
import time

def main():
    url = "http://challenges.ringzer0team.com:10013/"
    start_time = time.time()

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    message_tag = soup.find('div', class_='message')
    message = message_tag.text.strip()

    message = message.replace("----- BEGIN MESSAGE -----", "").replace("----- END MESSAGE -----", "").strip()

    hash_object = hashlib.sha512(message.encode())
    hash_hex = hash_object.hexdigest()

    response_url = f"{url}?r={hash_hex}"

    response = requests.get(response_url)

    end_time = time.time()

    print(f"Response: {response.text}")
    print(f"Time elapsed: {end_time - start_time} seconds")

if __name__ == "__main__":
    main()




