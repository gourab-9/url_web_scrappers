import streamlit as st
import urllib.request
from bs4 import BeautifulSoup


class Scrapper:
    def __init__(self, site):
        self.site = site

    def scrape(self):
        try:
            r = urllib.request.urlopen(self.site)
            html = r.read()
            parser = "html.parser"
            sp = BeautifulSoup(html, parser)

            urls = []
            for tag in sp.find_all("a"):
                url = tag.get("href")
                if url is not None:
                    urls.append(url)
            return urls
        except Exception as e:
            print("Error:", e)
            return []


# Streamlit app title
st.title("URL Scraper")

# Get website name from user input
site = st.text_input("Enter the website name:")

# Button to trigger scraping
if st.button("Get URLs"):
    if site:
        # Instantiate Scrapper class
        scrapper = Scrapper(site)

        # Call scrape method
        urls = scrapper.scrape()

        if urls:
            # Display scraped URLs
            st.write("Found URLs:")
            for url in urls:
                st.write(url)
        else:
            st.write("No URLs found.")
    else:
        st.write("Please enter a website name.")
