import sys
import requests
from bs4 import BeautifulSoup



def main():
    # loops through arguments from command line
    for x in range(1, len(sys.argv)):
        # requests (Gets website url content)
        try:
            # gets website url content
            request = requests.get("https://en.wikipedia.org/wiki/{}".format(sys.argv[x])).content

            # If website is invalid 
            if "Wikipedia does not have an article with this exact name" in str(request):
                print("Wikipedia does not have an article with this exact name")
                exit()

            # BeautifulSoup
            soup = BeautifulSoup(request, "lxml")
            # If the response is valid it should then load beautifulsoup and search the page for the text of the results
            links = []
            words = []

            # narrows to what is displayed in the content div of the page
            content = soup.find("div", {"id": "mw-content-text"})

            for link in content.find_all('a'):
                links.append(link.get('href'))
                words.append(link.text)

            for x in range(0, len(words)):
                print("{} - {}".format(words[x], links[x]))

        except Exception as e:
            print(e)
            print("failed to get website url at https://en.wikipedia.org/wiki/{}".format(sys.argv[x]))
            exit()

    return 0


if __name__ == '__main__':
    main()