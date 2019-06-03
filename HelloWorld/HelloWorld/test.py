#!/usr/bin/python

import os

MailCode="123"


def sendmail():
    Mail = "1628575993@qq.com"
    TITLE="VPN _verification_code"
    sendmail="echo " + MailCode + "| mail -s "  + TITLE + " "+ Mail
    os.system(sendmail)

def writefile():
    Mail = "1628575993@qq.com"
    TITLE="VPN _verification_code"
    sendmail="echo " + MailCode + "| mail -s "  + TITLE + " "+ Mail
    fo=open("/tmp/test.txt","w")
    fo.write(sendmail)
    fo.close()

if __name__ == "__main__":
    writefile()