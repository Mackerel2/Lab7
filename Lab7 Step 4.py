from guizero import App, Text, Picture
def closeitup():
    if app.yesno("Quit","Do you want to quit???") == True:
        app.destroy()
    else:
        print("Welcome back!")
app = App("Wanted!")
app.bg = "#ABA0AA"
wanted_text = Text(app, "THIS GUY")
wanted_text.text_size = 50
wanted_text.font = "Times New Roman"
cat = Picture(app, image="droid.png")
app.when_closed = closeitup
app.display()