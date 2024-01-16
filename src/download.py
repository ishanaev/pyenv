import os
import yaml
import requests


class InitDist:
    def __init__(self, name: str, url: str | None, file: str | None, path: str):
        """
        :param name: Name of the distro
        :param url: Url of the distro (if exist)
        :param file: Local file of the distro (if exist)
        :param path: Distro extraction path (ex: /home/user/.pyenv/python)
        """
        self.name = name
        self.url = url
        self.file = file
        self.path = path

    def download_dist(self):
        with open(f'{self.name}.zip', 'wb+') as archive:
            requests.get(url=self.url, verify=None, files=archive)
