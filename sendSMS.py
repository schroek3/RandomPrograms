#Ken Schroeder
#First Program to send text messages
#Plan is to use this to send stock alerts
from twilio.rest import Client
accountSID = "AC6d2833c666348311d568bb87695495c6"
authToken = "a491e3496753c46e87119bcfba39d4b7"
myNumber = "+14255013016"
twilioNumber = "+12068008601"

def main():
	textMyself("\nHello, Ken")

def textMyself(message):
	client = Client(accountSID,authToken)
	client.messages.create(to=myNumber,from_=twilioNumber,body="AUTOMATED\n"+message)

if __name__ == "__main__":
	main()
