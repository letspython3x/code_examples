# how to work with Threads to simultaneously make several requests to different website links to extract data.Here is my code, which is working but its takes same amount of time to complete 100 urls with Threads and without them
import requests
from bs4 import BeautifulSoup
import threading
import pandas as pd

def parse_line(line, result_dict):
    r = requests.get(line)
    soup = BeautifulSoup(r.content.decode('utf-8', 'ignore'), 'lxml')
    try:
        title = soup.find('h1', id='itemTitle').text.encode('utf-8')
        price = soup.find('span', itemprop='price').text.encode('utf-8')
        result_dict[title] = price
    except:
        result_dict['No Title'] = "No price"

        my_dict = {}
        threads = []

        file_lines = []
        with open("ProductLinks.txt", 'r') as f:
            for line in f:
                file_lines.append(line)

                for input_line in file_lines:
                    parse_line(input_line, my_dict)

                    for input_line in file_lines:
                        t = threading.Thread(target=parse_line, args=(input_line, my_dict))
                        threads.append(t)
                        t.start()
                        df = pd.DataFrame.from_dict(my_dict, orient="index")
                        df.to_csv("Data.csv")

