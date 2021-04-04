import tkinter
filePath="/sys/class/backlight/intel_backlight/"
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
root.bind("<FocusOut>",exit)
root.bind("<Escape>",exit)
root.mainloop()