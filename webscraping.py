import sys
import requests
from bs4 import BeautifulSoup

# System (command line arguments)
print('Number of arguments:', len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv))



def main():
    # loops through arguments from command line
    for x in range(1, len(sys.argv)):
        # requests (Gets website url content)
        request = requests.get("https://en.wikipedia.org/wiki/" + str(sys.argv[x]) + "_(disambiguation)").content

        # BeautifulSoup
        soup = BeautifulSoup(request, "lxml")

        # loops through all text in the website
        for text in soup.find_all():
            if str(sys.argv[x]) in text.get_text():
                print(text.get_text())

    return 0


if __name__ == '__main__':
    main()