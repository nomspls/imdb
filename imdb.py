from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
import pandas as pd

df = pd.read_csv('cleanIMDB.csv')

class AutoGrid(GridLayout):
    def __init__(self, **kwargs):
        super(AutoGrid, self).__init__(**kwargs)
        self.cols = 1 
        self.padding = 50

        self.inside = GridLayout() 
        self.inside.cols = 1

        self.inside.add_widget(Label(text="Enter title: ", font_size=30))
        self.title = TextInput(multiline=False, halign="center", on_text_validate=self.pressed, font_size=30)
        self.inside.add_widget(self.title)
        
        self.outas = Label(font_size=17)
        self.inside.add_widget(self.outas)

        self.add_widget(self.inside) 

        self.submit = Button(text="Search", font_size=40)
        self.submit.bind(on_press=self.pressed)
        self.add_widget(self.submit) 
        
    def pressed(self, instance):
        title = self.title.text
        search = df.loc[df['primaryTitle']== title.title()]
        if search.empty == False:
            outputas = 'Title: '+search.iloc[0]['primaryTitle']+'\n' + 'Rating: '+str(search.iloc[0]['averageRating'])+ '\n' + 'Number of votes: '+str(search.iloc[0]['numVotes'])+ '\n'+'Year: '+ str(search.iloc[0]['startYear'])
            self.title.text = ''
            self.outas.text = outputas
        elif not title:
            self.outas.text = 'No title provided'
        else:
            self.outas.text = 'No such movie'
            self.title.text = ''
            
    def closered(self, instance):
        App.get_running_app().stop()
        Window.close()

class IMDBcheckApp(App):
    def build(self):
        return AutoGrid()

if __name__ == "__main__":
    IMDBcheckApp().run()