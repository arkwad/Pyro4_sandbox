import Pyro4

@Pyro4.expose
class Calculator(object):
    def calculate(self, first_number, second_number, action ):
		
		switcher = {	
			"+":first_number+second_number,
			"-":first_number-second_number,
			"*":first_number*second_number,
			"/":first_number/second_number,
		}
		return switcher.get(action,-1)

daemon = Pyro4.Daemon()                # start Demona pythonowego
ns = Pyro4.locateNS()             
uri = daemon.register(Calculator)
print uri   
ns.register("Calculator", uri)   
print("Ready.")
daemon.requestLoop()   # start the event loop of the server to wait for calls