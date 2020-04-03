""" Simple script to short urls by different sites.
Should work with python 3.6+ and does not require any other module to be
installed first.
"""
import json
import string
import random
import urllib.request

import config


def cutt_ly(url, alias, api_key):
    """ Short provided url by cutt.ly website

    :param url: Url that should be short
    :type url: str
    :param alias: Alias for the url that should be short
    :type alias: str
    :return: Dictionary containing information about short url
    :rtype: dict
    """
    get_url = f"https://cutt.ly/api/api.php?key={api_key}&short={url}&name={alias}"
    with urllib.request.urlopen(get_url) as response:
        data = json.loads(response.read().decode("utf-8"))["url"]
        if data["status"] == 7:
            return {
                "success": True,
                "short": data["shortLink"],
                "title": data["title"],
            }
    return {"success": False}


def main():
    """ Main function
    """
    url = input("Enter url:")
    alias = input("Enter alias: (Leave empty for random 6 character)")
    if alias == '':
        alias = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
    response = cutt_ly(url, alias, config.CUTT_LY_API_KEY)
    if response['success']:
        print(response['title'] + ':')
        print(response['short'])
    else:
        print("Something went wrong ...")


if __name__ == '__main__':
    main()
