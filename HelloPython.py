import datetime

def main():
	helloWorld()
	dateTime()

def helloWorld():
    print("Hello world!")
    print("Version 2")
	
def dateTime():
    now = datetime.datetime.now()
    print ("Current date and time is ")
    print (now.strftime("%A, %d-%m-%Y : %H:%M"))
    print("Goodbye")	
	#azure2

def multiplication(x, y):
    return x*y


main()


