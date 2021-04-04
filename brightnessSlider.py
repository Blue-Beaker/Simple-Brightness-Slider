import tkinter
filePath="/sys/class/backlight/intel_backlight/" #Modify this path for your device if this doesn't work
brightnessFile=open(f"{filePath}/brightness",mode="w+")
minBrightness=1
maxBrightness=open(f"{filePath}/max_brightness").read()
brightness=int(brightnessFile.read())
brightnessFile.close()
def setBrightness(value):
    brightnessFile=open(f"{filePath}/brightness",mode="w+")
    brightnessFile.write(str(value))
    brightnessFile.close()
root=tkinter.Tk()
root.title("Brightness")
root.geometry("300x100-100-100")
slider=tkinter.Scale(root,orient="horizontal",length=300,width=50,from_=minBrightness,to=maxBrightness,command=setBrightness)
slider.set(brightness)
slider.pack()
root.bind("<FocusOut>",exit) #Exit on FocusOut by default. Comment if you don't need this
root.bind("<Escape>",exit) #Exit on Esc Pressed
root.mainloop()
