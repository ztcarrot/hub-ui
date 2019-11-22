# coding:UTF-8
from configparser import ConfigParser
import os


def singleton(cls):
    instances = {}

    def _singleton(*args ,**kwargs):
        if cls not in instances:
            instances[cls] = cls(*args ,**kwargs)
        return instances[cls]
    return _singleton


@singleton
class Configger():
    config = ConfigParser()

    def __init__(self):
        self.config.read("configs/default.config")
        if os.environ["test_env"] is not None:
            # overwrite the default config with specified one
            self.config.read("configs/%s.config" % os.environ["test_env"])
        print({section: dict(self.config[section]) for section in self.config.sections()})


if __name__ == "__main__":
    __configs1 = Configger()
    __configs2 = Configger()
    print(Configger())
    print(__configs1)
    print(__configs2)

    print(Configger().config["pytest"]["browser_list"])
