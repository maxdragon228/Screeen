from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class MyApp(App):
    def build(self):
        
        btn = Button(text ="This is cat", markup=True, background_color=(.90, 47,  97, 34))
        txt = Label(text = "This is label") 
        btn.on_press = test
        layout = BoxLayout()
        layout.add_widget(txt)
        layout.add_widget(btn)
        
        return layout
def test():
    print("Hello")
    
app = MyApp()
app.run()