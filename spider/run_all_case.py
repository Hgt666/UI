import HTMLTestRunner
import time
import os
import unittest


def all_case():
    casePath=os.getcwd()+"//case"
    discover=unittest.defaultTestLoader.discover(casePath,pattern="test*.py")
    return discover

if __name__=="__main__":
    now=time.strftime("%Y%m%d%H%M%S")
    reportPath=os.getcwd()+"//report"+"//report"+now+".html"
    ff=open(reportPath,"wb")
    HTMLTestRunner.HTMLTestRunner(ff,title="官网测试",description="详情如下").run(all_case())
    ff.close()