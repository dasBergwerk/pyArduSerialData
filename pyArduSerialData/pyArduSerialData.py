from tkinter import *

class App:
	def __init__(self, master):
		# master.minsize(width = 1200, height = 800)
		frame = Frame(master)
		frame.grid()
		self.label = Label(frame, text = "Serielle Schnittstelle")
		self.label.grid(row = 0, column = 0, columnspan = 2, padx = 20, pady = 10)
		self.button = Button(frame, text = "Start", command = self.startdata)
		self.button.grid(row = 1, column = 0, sticky = E, pady = 10)
		self.button = Button(frame, text = "Stop", command = self.stopdata)
		self.button.grid(row = 1, column = 1, sticky = W)
		self.label = Label(frame, text = "Steuerung Aggregat")
		self.label.grid(row = 0, column = 3, columnspan = 3, padx = 40)
		self.button = Button(frame, text = "Kühlen", command = self.cool)
		self.button.grid(row = 1, column = 3, sticky = E)
		self.button = Button(frame, text = "Heizen", command = self.hot)
		self.button.grid(row = 1, column = 4)
		self.button = Button(frame, text = "Aus", command = self.aus)
		self.button.grid(row = 1, column = 5, sticky = W)
		self.label = Label(frame, text = "Steuerung Temperatur")
		self.label.grid(row = 0, column = 6, columnspan = 2)
		self.scale = Scale(frame, from_=10, to=42, orient = HORIZONTAL)
		self.scale.grid(row = 1, column = 6)
		self.button = Button(frame, text = "Senden", command = self.senden)
		self.button.grid(row = 1, column = 7)
		self.button = Button(frame, text = "Beenden", fg = "red", command = frame.quit)
		self.button.grid(row = 1, column = 8, padx = 40, sticky = W)
	
	def startdata(self):
		print ("Start")
	def stopdata(self):
		print ("Stop")
	def cool(self):
		print ("Kühlen")
	def hot(self):
		print ("Heizen")
	def aus(self):
		print ("Aggregat aus")
	def senden(self):
		print(self.scale.get())

root = Tk()
root.wm_title("Kühlaggregat")
app = App(root)
root. mainloop()
