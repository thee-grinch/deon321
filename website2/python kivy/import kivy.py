import kivy
kivy.require('2.1.0')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.animation import Animation
from kivy.graphics import Color, Rectangle

class MyApp(App):

    def build(self):
        # Create a BoxLayout to hold the label and act as the main container
        layout = BoxLayout(orientation='vertical')

        # Create a label
        label = Label(text='DEON & BRYNT', font_size='24sp')

        # Add the label to the layout
        layout.add_widget(label)

        # Create a rectangle for the background
        with layout.canvas.before:
            Color(0, 1, 1, 1)  # Set the initial background color (RGB and alpha)
            self.background = Rectangle(pos=layout.pos, size=layout.size)

        # Schedule the background color animation
        anim = Animation(color=(1, 0, 1, 1), duration=2) + Animation(color=(0, 1, 0, 1), duration=2)
        anim.repeat = True
        anim.start(self.background)

        return layout

if __name__ == '__main__':
    MyApp().run()
