import requests
from bs4 import BeautifulSoup

from content import Content
from grade import Grade


def get_content_list(grade: Grade):
    result = []

    url = "https://www.eiken.or.jp/eiken/exam/grade_" + grade.value + "/solutions.html"
    html = requests.get(url)
    soup = BeautifulSoup(html.content, "html.parser")
    for liElement in soup.find_all(class_="pdf"):
        a_element = list(liElement.children)[0]

        url = "https://www.eiken.or.jp/" + a_element.attrs["href"]
        if a_element.text != "問題と解答のサンプル" and a_element.text != "問題のサンプル":
            split_text = a_element.text.split(" ")
            year = split_text[0]
            time = split_text[1]
            name = split_text[2]
            result.append(Content(grade, year, time, name, url))

    return result
