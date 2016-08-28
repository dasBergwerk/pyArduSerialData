from tkinter import *

class App(Frame):
	def __init__(self, master = None):
			Frame.__init__(self, master)
			self.grid()
			self.master.title("Kühlaggregat")

			FrameKopf = Frame(master, bg = "red")
			FrameKopf.grid(row = 0, column = 0, rowspan = 2, columnspan = 10)
        
			FrameLinks = Frame(master, bg = "blue")
			FrameLinks.grid(row = 2, column = 0, rowspan = 5, columnspan = 2)
        
			FrameRechts = Frame(master, bg = "green")
			FrameRechts.grid(row = 2, column = 2, rowspan = 5, columnspan = 8 )
        
			FrameUnten = Frame(master, bg = "yellow")
			FrameUnten.grid(row = 8, column = 0, columnspan = 10)
        

		
			self.labelSer = Label(FrameKopf, text = "Serielle Schnittstelle")
			self.buttonStart = Button(FrameKopf, text = "Start", fg = "green", height = 2, width = 6, command = self.startdata)
			self.buttonStop = Button(FrameKopf, text = "Stop", fg = "red", height = 2, width = 6, command = self.stopdata)
			self.labelAgg = Label(FrameKopf, text = "Steuerung Aggregat")
			self.buttonKühlen = Button(FrameKopf, text = "Kühlen", height = 2, width = 6, command = self.cool)
			self.buttonHeizen = Button(FrameKopf, text = "Heizen", height = 2, width = 6,command = self.hot)
			self.buttonAus = Button(FrameKopf, text = "Aus", height = 2, width = 6, command = self.aus)
			self.labelSTTemp = Label(FrameKopf, text = "Steuerung Temperatur")
			self.scaleTemp = Scale(FrameKopf, from_=10, to=42, orient = HORIZONTAL)
			self.buttonTemp = Button(FrameKopf, text = "Senden", height = 2, width = 6, command = self.senden)
			self.buttonBeenden = Button(FrameKopf, text = "Beenden", fg = "red", height = 2, width = 6, command = master.quit)
			self.labelAktuelleTemp = Label(FrameLinks, text = "Aktuelle Temperatur")
			self.labelRaum = Label(FrameLinks, relief = SUNKEN, height = 2, width = 12, text = "Raum:")
			self.textRaum = Text(FrameLinks, height = 2, width = 4)
			self.labelTank = Label(FrameLinks, relief = SUNKEN, height = 2, width = 12, text = "Tank:")
			self.textTank = Text(FrameLinks, height = 2, width = 4)
			self.labelPelIn = Label(FrameLinks, relief = SUNKEN, height = 2, width = 12, text = "Pelitier Innen:")
			self.textPelIn = Text(FrameLinks, height = 2, width = 4)
			self.labelPelAu = Label(FrameLinks, relief = SUNKEN, height = 2, width = 12, text = "Pelitier Außen:")
			self.textPelAu = Text(FrameLinks, height = 2, width = 4)
			self.labelKonsole = Label(FrameUnten, text = "Konsole")
			self.textKonsole = Text(FrameUnten, height = 2, width = 20)
	
			self.labelSer.grid(row = 0, column = 0, columnspan = 2)
			self.labelAgg.grid(row = 0, column = 2, columnspan = 3)
			self.labelSTTemp.grid(row = 0, column = 5, columnspan = 2)
			self.buttonStart.grid(row = 1, column = 0)
			self.buttonStop.grid(row = 1, column = 1)
			self.buttonKühlen.grid(row = 1, column = 2)
			self.buttonHeizen.grid(row = 1, column = 3)
			self.buttonAus.grid(row = 1, column = 4)
			self.scaleTemp.grid(row = 1, column = 5)
			self.buttonTemp.grid(row = 1, column = 6)
			self.buttonBeenden.grid(row = 1, column = 7)
			self.labelAktuelleTemp.grid(row = 2, column = 0)
			self.labelRaum.grid(row = 3, column = 0)
			self.labelTank.grid(row = 4, column = 0)
			self.labelPelIn.grid(row = 5, column = 0)
			self.labelPelAu.grid(row = 6, column = 0)
			self.textRaum.grid(row = 3, column = 1)
			self.textTank.grid(row = 4, column = 1)
			self.textPelIn.grid(row = 5, column = 1)
			self.textPelAu.grid(row = 6, column = 1)
			self.labelKonsole.grid(row = 8, column = 0)
			self.textKonsole.grid(row = 8, column = 1)
		

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
app = App(master = root)
root. mainloop()
