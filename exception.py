class MyException(Exception):
    def __init__(self,msg):
        self.msg=msg

    def __str__(self):
	return "exception occured:"+self.msg

try:
    raise MyException("test exception")
except MyException as e:
    print e
