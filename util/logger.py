
import datetime


def info(text):
    print(datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S - {}".format(text)))
