import datetime

def main():
	helloWorld()
	dateTime()
	print("The result of the multiplication of 3 with 3 is ", str(multiplication(3,3)))

def helloWorld():
    print("Hello world!")
    print("Version 3")
	
def dateTime():
    now = datetime.datetime.now()
    print ("Current date and time is ")
    print (now.strftime("%A, %d-%m-%Y : %H:%M"))
    print("Goodbye")	
	#azure2
	
def multiplication(x, y):
    return x*y


main()



