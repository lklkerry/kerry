import logging
import time
import os

cur_path=os.path.dirname(os.path.realpath(__file__))
log_path=os.path.join(os.path.dirname(cur_path),'logs')

if not os.path.exists(log_path):os.mkdir(log_path)

class Log():
    def __init__(self):
        # self.logname=os.path.join(log_path,'%s.log'%time.strftime('%Y_%m_%d_%H_%M_%S'))
        self.logger=logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        self.formatter=logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')
        # formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')
    def __console(self,level,message):
        # fh=logging.FileHandler(self.logname,'a',encoding='utf-8')
        fh = logging.FileHandler('a', encoding='utf-8')
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)

        ch=logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)

        if level=='info':
            self.logger.info(message)
        elif level=='debug':
            self.logger.debug(message)
        elif level=='warning':
            self.logger.warning(message)
        elif level=='error':
            self.logger.error(message)

        self.logger.removeHandler(fh)
        self.logger.removeHandler(ch)
        fh.close()

    def info(self,message):
        self.__console('info',message)

    def warning(self,message):
        self.__console('warning',message)


if __name__=="__main__":
    log=Log()
    log.info('---测试开始---')
    log.info('操作步骤1,2,3')
    log.warning('---测试结束---')

