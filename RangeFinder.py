import tkinter as tk
import math

root = tk.Tk()
root.geometry("600x400")

root.attributes('-alpha', 0.35)
root.title("manuroger112's range calculator")
root.config(bg = "green")

canvas = tk.Canvas(root, width=500, height=500, bg= "black")
canvas.place(x=0, y= 0)

class gls:
    pxLabelOffset = 5
    Distance = 200.0
    NormUnit = 250.0
    
    BaseNorms = [150, 200, 225, 250, 325, 400, 500, 550]
    NormSelection = 3
    
    Range = (Distance/NormUnit) * 250
    
Globals = gls()

def BeginDrag(event):
    #get the specific widget of the event that we are dealing with
    widget = event.widget
    
    widget.beginX = event.x
    widget.beginY = event.y

def MouseDrag(event):
    widget = event.widget
    
    x = widget.winfo_x() - widget.beginX + event.x
    y = widget.winfo_y() - widget.beginY + event.y
    widget.place(x=x, y=y)

    canvas.coords(RangeLine, Point1.winfo_x()+Globals.pxLabelOffset, Point1.winfo_y()+Globals.pxLabelOffset, Point2.winfo_x()+Globals.pxLabelOffset, Point2.winfo_y() + Globals.pxLabelOffset)
    Globals.Distance = round(math.sqrt(math.pow((Point2.winfo_x() - Point1.winfo_x()), 2)+math.pow((Point2.winfo_y() - Point1.winfo_y()), 2)))
    Globals.Range = round(((Globals.Distance/Globals.NormUnit) * Globals.BaseNorms[Globals.NormSelection])) #times 0.9 as 0.9 is coefficient found through studies in wt of how much the calculated range is in comparison to actual range over different resolutions
    TextDistance.config(text=f"Distance: {Globals.Distance} pixels | Range = {Globals.Range} Meters")

def SetNormalizer():
    Globals.NormUnit = abs(Point2.winfo_x() - Point1.winfo_x())
    NormalizedUnit.config(text=f"Normalized Unit = {Globals.NormUnit} pixels for {Globals.BaseNorms[Globals.NormSelection]} Meters")

def SetBaseNorm():
    Globals.NormSelection = (Globals.NormSelection+1)%len(Globals.BaseNorms)
    Globals.Distance = round(math.sqrt(math.pow((Point2.winfo_x() - Point1.winfo_x()), 2)+math.pow((Point2.winfo_y() - Point1.winfo_y()), 2)))
    Globals.Range = round(((Globals.Distance/Globals.NormUnit) * Globals.BaseNorms[Globals.NormSelection]))
    NormalizedUnit.config(text=f"Normalized Unit = {Globals.NormUnit} pixels for {Globals.BaseNorms[Globals.NormSelection]} Meters")
    TextDistance.config(text=f"Distance: {Globals.Distance} pixels | Range = {Globals.Range} Meters")

image = tk.PhotoImage(file="crossaim.png")

Point1 = tk.Label(canvas, image=image)
Point2 = tk.Label(canvas, image=image)

TextDistance = tk.Label(canvas, text=f"Distance:{Globals.Distance} pixels | Range = {Globals.Range} Meters", relief=tk.RAISED, font=("Impact", 12, "italic"), width = 40, height = 1);
TextDistance.place(x=0, y=0)

SetUnitNormalizer = tk.Button(root, text="Set Unit Norm", width = 11, font=("Impact", 9, ""), height = 2, command=SetNormalizer)
SetUnitNormalizer.place(x=510, y=30)

SetBaseNormalizator = tk.Button(root, text="BASE GRID SIZE", width = 11, font=("Impact", 9, ""), height = 2, command=SetBaseNorm)
SetBaseNormalizator.place(x=510, y=90)

NormalizedUnit = tk.Label(root, text=f"Normalized Unit = {Globals.NormUnit} pixels for {Globals.BaseNorms[Globals.NormSelection]} Meters", font=("Impact", 8, "italic"))
NormalizedUnit.place(x=0, y= 25)

Point1.place(x=0, y=200)
Point2.place(x=200, y=200)

Point1.bind("<Button-1>", BeginDrag)
Point1.bind("<B1-Motion>", MouseDrag)

Point2.bind("<Button-1>", BeginDrag)
Point2.bind("<B1-Motion>", MouseDrag)


RangeLine = canvas.create_line(0+Globals.pxLabelOffset, 200+Globals.pxLabelOffset, 200, 200+Globals.pxLabelOffset, fill="green", width=1)
root.mainloop()
