from guizero import App, Text
from gpiozero import Button, LED
from time import sleep

button = Button(2)
led17 = LED(17)

def scanInput():
    if button.is_pressed:
        text.value = 1 #"GPIO2 ON "
        led17.on()
    else:
        text.value = 0 #"GPIO2 OFF"
        led17.off()
        
def exitGUI():
    
    text.destroy()
    if app.yesno("Close", "Do you want to Quit?"):
        app.destroy()
        print("adios")
              
if __name__ == '__main__':
    
    app = App("Reading GPIO")
    text = Text(app, text="1")
    text.repeat(10, scanInput)
#input(every)
    app.when_closed = exitGUI
    app.display()