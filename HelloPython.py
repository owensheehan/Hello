import datetime

def main():
	helloWorld()
	dateTime()

def helloWorld():#Text
	print("Hello world!")
    print("Version 2")
	
def dateTime():#date and time
	now = datetime.datetime.now()
	print ("Current date and time is ")
	print (now.strftime("%A, %d-%m-%Y : %H:%M"))
    print("Goodbye ")	
	
main()