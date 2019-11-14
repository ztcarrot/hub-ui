#!/usr/bin/env python
# coding:UTF-8

import os ,logging ,sys ,time

def log_call(func):
    def proxy(*args, **kwargs):
        func_name = func.__module__+"-->"+func.__name__
        time_start = time.time()
        Logger().logger.debug('\n>>>>>>begin call: {}'.format(func_name))
        result = func(*args, **kwargs)
        time_end = time.time()
        Logger().logger.info('end call %s, cost: %.2f seconds.\n<<<<<<' % (func_name, (time_end - time_start)))
        return result
    return proxy


def singleton(cls):
    instances = {}
    def _singleton(*args ,**kwargs):
        if cls not in instances:
            instances[cls] = cls(*args ,**kwargs)
        return instances[cls]
    return _singleton

@singleton
class Logger():
    def __init__(self ,logfile=None):
        self.logger = logging.getLogger()
        formater = logging.Formatter('%(asctime)s - %(levelname)s <%(thread)s> [%(filename)s %(lineno)d]:: %(message)s')
        if logfile == None:
            cur_path = os.path.split(os.path.realpath(__file__))[0]
            stime = time.strftime("%Y-%m-%d" ,time.localtime())
            logfile = cur_path + os.sep + "log_" + stime + ".log"
        else:
            logfile = logfile
        self.sh = logging.StreamHandler(sys.stdout)
        self.sh.setFormatter(formater)
        self.fh = logging.FileHandler(logfile)
        self.fh.setFormatter(formater)
        self.logger.addHandler(self.sh)
        self.logger.addHandler(self.fh)
        self.logger.setLevel(logging.INFO)

if __name__ == "__main__":
    lg = Logger()
    lg2 = Logger()
    print(lg)
    print(lg2)
    Logger().logger.info("test")
