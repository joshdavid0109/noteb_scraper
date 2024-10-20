import requests


def check_site_accessibility(url):
    with requests.Session() as session:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
        }

        try:
            response = session.get(url, headers=headers)
            if response.status_code == 200:
                print(f"The site {url} is accessible.")
            else:
                print(f"The site {url} returned status code: {response.status_code}.")
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")


# Example usage
url_to_check = "https://noteb.com/?search/search.php?prod=HP&browse_by=prod&sort_by=value"
check_site_accessibility(url_to_check)
