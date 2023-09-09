import requests
from bs4 import BeautifulSoup
from newspaper import Article

def web_scrapper(url):
    try:
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')

            contribution = Article(url)
            contribution.download()
            contribution.parse()

            file_name = "text.txt"
            authors_text = ", ".join(contribution.authors)

            with open(file_name, "a", encoding="utf-8") as file:
                file.write("Title: " + contribution.title + "\n")
                file.write("--------------------------------------------------------------\n")
                file.write("Publish Date: " + str(contribution.publish_date) + "\n")
                file.write("--------------------------------------------------------------\n")
                file.write("Authors: " + authors_text + "\n")
                file.write("--------------------------------------------------------------\n")
                file.write("Content: " + contribution.text + "\n")

            print(f"{file_name} write to file is successful.")
        else:
            print("Page Not Found", response.status_code)

    except Exception as e:
        print("Something went wrong", str(e))

if __name__ == "__main__":
    contribution_url = "https://www.reuters.com/article/us-health-coronavirus-global-deaths/global-coronavirus-deaths-pass-agonizing-milestone-of-1-million-idUSKBN26K08Y"
    web_scrapper(contribution_url)
