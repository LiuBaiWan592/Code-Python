import requests
 
 
def check_website(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"{url} is up and running!")
        else:
            print(f"{url} returned status code {response.status_code}")
    except Exception as e:
        print(f"Error: {e}")
 
 
check_website('https://example.com')
check_website('http://localhost:9008')