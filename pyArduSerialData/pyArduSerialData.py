from Tkinter import *
import serial
import sysconfig
import time
import datetime
import serial.tools.list_ports
from ScrolledText import ScrolledText


class App(Frame):
	def __init__(self, master = None):
			Frame.__init__(self, master)
			self.grid()
			self.master.title("Kuehlaggregat")
			self.stat = False
			
			#Frame Kopfzeilen
			FrameKopf = Frame(master)
			FrameKopf.grid(row = 0, column = 0, rowspan = 2, columnspan = 10, pady = 2)
        	
        	#Frame Links
			FrameLinks = Frame(master)
			FrameLinks.grid(row = 2, column = 0, rowspan = 5, columnspan = 2, pady = 10)
        	
        	#Frame Rechts
			FrameRechts = Frame(master)
			FrameRechts.grid(row = 2, column = 2, rowspan = 5, columnspan = 8, pady = 2, sticky = W+N)
        	
        	#Frame Unten
			FrameUnten = Frame(master)
			FrameUnten.grid(row = 8, column = 0, columnspan = 10, pady = 10, sticky = W, padx = 13)
        

				
			# Widgets Serielle Schnittstelle			
			self.labelSer = Label(FrameKopf, text = "Serielle Schnittstelle")
			self.buttonStart = Button(FrameKopf, text = "Start", fg = "green", height = 2, width = 6, command = self.startdata)
			self.buttonStop = Button(FrameKopf, text = "Stop", fg = "red", height = 2, width = 6, command = self.stopdata)
			
			#Widgets Steuerung Aggregat
			self.labelAgg = Label(FrameKopf, text = "Steuerung Aggregat")
			self.buttonKuehlen = Button(FrameKopf, text = "Kuehlen", height = 2, width = 6, command = self.cool)
			self.buttonHeizen = Button(FrameKopf, text = "Heizen", height = 2, width = 6,command = self.hot)
			self.buttonAus = Button(FrameKopf, text = "Aus", height = 2, width = 6, command = self.aus)
			
			#Widgets Steuerung Temperatur
			self.labelSTTemp = Label(FrameKopf, text = "Steuerung Temperatur")
			self.scaleTemp = Scale(FrameKopf, from_=10, to=42, orient = HORIZONTAL)
			self.buttonTemp = Button(FrameKopf, text = "Senden", height = 2, width = 6, command = self.senden)
			
			#Widgets Programm
			self.labelProg = Label(FrameKopf, text = "Programm")
			self.labelStat = Label(FrameKopf, relief = SUNKEN, text = "Status:")
			self.textStat = Text(FrameKopf, height = 1, width = 10)
			self.buttonBeenden = Button(FrameKopf, text = "Beenden", fg = "red", height = 2, width = 6, command = master.quit)
			
			#Widgets Aktuelle Temperatur
			self.labelAktuelleTemp = Label(FrameLinks, text = "Aktuelle Temperatur")
			self.labelRaum = Label(FrameLinks, relief = SUNKEN, height = 1, width = 12, text = "Raum:")
			self.textRaum = Text(FrameLinks, height = 1, width = 4)
			self.labelTank = Label(FrameLinks, relief = SUNKEN, height = 1, width = 12, text = "Tank:")
			self.textTank = Text(FrameLinks, height = 1, width = 4)
			self.labelPelIn = Label(FrameLinks, relief = SUNKEN, height = 1, width = 12, text = "Pelitier Innen:")
			self.textPelIn = Text(FrameLinks, height = 1, width = 4)
			self.labelPelAu = Label(FrameLinks, relief = SUNKEN, height = 1, width = 12, text = "Pelitier Aussen:")
			self.textPelAu = Text(FrameLinks, height = 1, width = 4)
			
			#Widgets Plotting
			self.labelPlot = Label(FrameRechts, text = "Plot")
			
			#Widgets Konsole
			self.labelKonsole = Label(FrameUnten, relief = SUNKEN, width = 12, text = "Konsole:")
			self.textKonsole = ScrolledText(FrameUnten, height = 3, width = 80)	
			
			#Setzen der einzelen Widgets
			self.labelSer.grid(row = 0, column = 0, columnspan = 2, pady = 5, padx = 20)
			self.labelAgg.grid(row = 0, column = 2, columnspan = 3, padx = 25)
			self.labelSTTemp.grid(row = 0, column = 5, columnspan = 2, padx = 30)
			self.labelProg.grid(row = 0, column = 7, columnspan = 3, padx = 20)
			self.buttonStart.grid(row = 1, column = 0, sticky = E)
			self.buttonStop.grid(row = 1, column = 1, sticky = W)
			self.buttonKuehlen.grid(row = 1, column = 2, sticky = E)
			self.buttonHeizen.grid(row = 1, column = 3)
			self.buttonAus.grid(row = 1, column = 4, sticky = W)
			self.scaleTemp.grid(row = 1, column = 5, sticky = E)
			self.buttonTemp.grid(row = 1, column = 6, sticky = W)
			self.labelStat.grid(row = 1, column = 7, sticky = E, padx = 5)
			self.textStat.grid(row = 1, column = 8, sticky = W)
			self.buttonBeenden.grid(row = 1, column = 9, padx = 5)
			self.labelAktuelleTemp.grid(row = 0, column = 0, pady = 5)
			self.labelRaum.grid(row = 1, column = 0)
			self.labelTank.grid(row = 2, column = 0)
			self.labelPelIn.grid(row = 3, column = 0)
			self.labelPelAu.grid(row = 4, column = 0)
			self.textRaum.grid(row = 1, column = 1)
			self.textTank.grid(row = 2, column = 1)
			self.textPelIn.grid(row = 3, column = 1)
			self.textPelAu.grid(row = 4, column = 1)
			self.labelPlot.grid(row = 0, column = 0, sticky = E)
			self.labelKonsole.grid(row = 0, column = 0, sticky = W)
			self.textKonsole.grid(row = 0, column = 1, padx = 13, sticky = S)
		
	# Function: Starting Connection to Arduino and start Datalogging
	def startdata(self):
		self.textKonsole.delete('1.0', END)
		self.textKonsole.insert(END, "Starting...\n")
		self.textKonsole.insert(END, "Scanning for Ports: \n")
		self.arduinoPort = self.findArduinoPort()
		if not self.arduinoPort:
			self.textKonsole.insert(END,"No Arduino found\n")
		else:	
			self.textKonsole.insert(END,"Arduino found: ")
			self.textKonsole.insert(END, self.arduinoPort)
			self.textKonsole.insert(END, "\nTry connecting to arduino...\n")
			self.serialArduino = serial.Serial(str(self.arduinoPort), 9600, timeout = 2)
			self.stat = (str(self.serialArduino.isOpen()))
			if not self.stat:
				self.textKonsole.insert(END, "Connection failed!")
			else:
				self.textKonsole.insert(END, "Connection establish!\n")
				self.textKonsole.insert(END, "Starting Datalogging..\n")
				self.datalog()
				return self.stat
	
	def datalog(self):
		self.datei = open('data.log','w+',0)

				
				
	
	def findArduinoPort(self):
		self.ports = list(serial.tools.list_ports.comports())
		for port in self.ports:
			if "VID:PID=0403:6001" in port[0]\
				or "VID:PID=0403:6001" in port[1]\
				or "VID:PID=0403:6001" in port[2]:
				return port[0] 		
			
	def stopdata(self):
		self.textKonsole.delete('1.0', END)
		self.textKonsole.insert(END, "Stopping...\n")
		if not self.stat:
			self.textKonsole.insert(END, "Nothing to do\n")
		else:
			self.textKonsole.insert(END,"Closing Serial...\n")
			self.serialArduino.close()
			self.stat = False
			self.textKonsole.insert(END,"Close Serial!\n")
			
					
	def cool(self):
		print ("Kuehlen")
	def hot(self):
		print ("Heizen")
	def aus(self):
		print ("Aggregat aus")
	def senden(self):
		print(self.scale.get())
	

root = Tk()
app = App(master = root)
root. mainloop()
