import requests
from bs4 import BeautifulSoup

# Function to scrape links and text from a given URL


def web_scrapper(url):
    response = requests.get(url)  # Send an HTTP GET request to the URL
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        web_page = response.text  # Get the HTML content of the web page

        # Create a BeautifulSoup object to parse the HTML content
        soup = BeautifulSoup(web_page, 'html.parser')

        # Scrape and print links (href attributes) from anchor tags
        for link in soup.find_all('a'):
            print('link: ', link.get('href'))

        # Scrape and print text content from paragraph tags
        for text in soup.find_all('p'):
            print('text: ', text.get_text())

    else:
        print('failed to retrieve web page.')


# Call the web_scrapper function with a URL
web_scrapper('https://www.____.com/')
