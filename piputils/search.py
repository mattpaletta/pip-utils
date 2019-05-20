import urllib.request as url
from bs4 import BeautifulSoup
import json


def search(package: str):
    response = url.urlopen("https://pypi.python.org/pypi?%3Aaction=search&term={0}&submit=search".format(package))
    soup = BeautifulSoup(response.read(), "html.parser")
    for section in soup.find_all(class_ = "package-snippet"):
        name = section.find_all(class_ = "package-snippet__name")[0].get_text()
        version = section.find_all(class_ = "package-snippet__version")[0].get_text()
        description = section.find_all(class_ = "package-snippet__description")[0].get_text()

        yield name, version, description


def _get_release_data(package_name):
    response = url.urlopen("https://pypi.org/pypi/{0}/json".format(package_name))
    data = json.loads(str(response)).get("releases")
    return data


def get_releases(package_name):
    data = _get_release_data(package_name).keys()
    return list(data)


def get_latest_release(package_name):
    release_versions = _get_release_data(package_name)

    def extract_release_date(dict_item):
        version = dict_item[0]
        upload_data = dict_item[1]

        if len(upload_data) == 0:
            return version, ""
        else:
            return version, upload_data[0].get("upload_time", None)

    release_date = list(map(extract_release_date, release_versions.items()))
    sorted(release_date, key = lambda x: x[1])
    return release_date[-1][0]
