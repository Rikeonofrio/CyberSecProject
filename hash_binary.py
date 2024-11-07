import hashlib

import requests
from bs4 import BeautifulSoup
import time
import sys

sys.set_int_max_str_digits(100000)


def binary_to_string(binary_str):
    n = 8
    binary_values = [binary_str[i:i + n] for i in range(0, len(binary_str), n)]

    decimal_values = [int(bv, 2) for bv in binary_values]

    ascii_characteres = [chr(dv) for dv in decimal_values]

    final_string = "".join(ascii_characteres)

    return final_string


def main():
    url = "http://challenges.ringzer0ctf.com:10014/"
    start_time = time.time()

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    message_tag = soup.find('div', class_='message')
    message = message_tag.text.strip()

    message = message.replace("----- BEGIN MESSAGE -----", "").replace("----- END MESSAGE -----", "").strip()

    ###--------------------------------------------

    n = 8
    binary_values = [message[i:i + n] for i in range(0, len(message), n)]

    decimal_values = [int(bv, 2) for bv in binary_values]

    ascii_characteres = [chr(dv) for dv in decimal_values]

    final_string = "".join(ascii_characteres)



    ###-------------------------------------------

    hash_object = hashlib.sha512(final_string.encode())
    hash_hex = hash_object.hexdigest()

    response_url = f"{url}?r={hash_hex}"

    response = requests.get(response_url)

    end_time = time.time()

    print(f"Response: {response.text}")
    print(f"Time elapsed: {end_time - start_time} seconds")


if __name__ == "__main__":
    main()
