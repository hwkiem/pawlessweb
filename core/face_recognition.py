import face_recognition
from urllib import request
from bs4 import BeautifulSoup
import re
import os
import urllib


def get_encoding(img):

    return face_recognition.face_encodings(img)


def mock(img):
    print(type(img))
    url = img
    response = request.urlopen(url).read()

    soup= BeautifulSoup(response)
    links = soup.find_all("a")

    url_list = links[0]['href']
    print(url_list)

    request.urlretrieve(url_list, "face.jpg")
    return img
