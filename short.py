""" Simple script to short urls by different sites.
Should work with python 3.6+ and does not require any other module to be
installed first.
"""
import json
import urllib.request


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
        print(data)
        if data["status"] == 7:
            return {
                "success": True,
                "short": data["shortLink"],
                "title": data["title"],
            }
    return {"success": False}
