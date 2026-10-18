"""
Experiment 10: Web Scraping
Course Code: 23A30403 - Data Science Using Python Lab
"""
import requests
from bs4 import BeautifulSoup

def main():
    print("=== Experiment 10: Web Scraping Demonstration ===")
    
    # Educational public testing endpoint
    url = "https://httpbin.org/html"
    print(f"Fetching webpage from: {url}")
    
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        print("Page successfully fetched!")
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract title
        title = soup.title.string if soup.title else "No Title Found"
        print(f"\nPage Title: {title.strip()}")
        
        # Extract headings
        print("\nHeadings Found:")
        headings = soup.find_all(['h1', 'h2', 'h3'])
        for h in headings:
            print(f" - {h.name.upper()}: {h.text.strip()}")
            
        # Extract paragraph sample
        print("\nParagraph Content Sample:")
        p = soup.find('p')
        if p:
            print(p.text.strip()[:150] + "...")
            
    except requests.exceptions.RequestException as e:
        print(f"\n[Network/HTTP Error] Could not fetch page: {e}")
        print("Demonstrating offline mode gracefully.")

if __name__ == "__main__":
    main()
