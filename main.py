from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
import webbrowser

class WABotApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        self.label = Label(text='WABOT by litzx55\nMasukin nomor & pesan brek!', font_size='18sp')
        self.nomor = TextInput(hint_text='Nomor WA cth: 628123456789', multiline=False)
        self.pesan = TextInput(hint_text='Pesan lu brek...')
        btn = Button(text='KIRIM WA LANGSUNG!', background_color=(0,1,0,1), size_hint_y=None, height=60)
        btn.bind(on_press=self.kirim)
        layout.add_widget(self.label)
        layout.add_widget(self.nomor)
        layout.add_widget(self.pesan)
        layout.add_widget(btn)
        return layout
    def kirim(self, instance):
        no = self.nomor.text
        ps = self.pesan.text
        if no:
            url = f"https://wa.me/{no}?text={ps}"
            webbrowser.open(url)

WABotApp().run()
