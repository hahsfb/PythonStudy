import sys
from datetime import datetime
from datetime import timedelta
from pycall import CallFile, Call, Application


def call(number, time=None):
    c = Call('SIP/flowroute/%s' % number)
    a = Application('Playback', 'hello-world')
    cf = CallFile(c, a)
    cf.spool(time)

if __name__ == '__main__':
    call('18101519736', datetime.now()+timedelta(hours=1))
