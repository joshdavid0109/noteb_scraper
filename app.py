import requests
from bs4 import BeautifulSoup

# Step 1: Send a GET request to the webpage
url = 'https://noteb.com/?search/search.php?prod=HP&browse_by=prod&sort_by=value'  # Replace this with your target URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Step 2: Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    print(soup.find_all('div', class_='notificationsModal'))

    # Step 3: Find all the laptop result blocks (based on the 'searchresult' class)
    laptops = soup.find_all('div', class_='searchresult')

    print(laptops)

    # Step 4: Loop through each laptop result and extract relevant information
    for laptop in laptops:
        # Extract the title inside 'searchresulttitlelu'
        title_div = laptop.find('p', class_='searchresulttitlelu')
        title = title_div.get_text(strip=True) if title_div else "No Title"

        # Extract the specs inside 'searchresultdesc'
        specs_div = laptop.find('div', class_='searchresultdesc')
        specs = specs_div.get_text(strip=True) if specs_div else "No Specs Available"

        # Extract the price inside 'fakeBtn' (price is inside a button)
        price_div = laptop.find('div', class_='btn-outline-secondary searchprice fakeBtn')
        price = price_div.get_text(strip=True) if price_div else "Price Not Available"

        # Display the extracted information
        print(f"Title: {title}")
        print(f"Specs: {specs}")
        print(f"Price: {price}")
        print('-' * 40)
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
