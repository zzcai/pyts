from kivy.app import App

from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button


from kivy.app import App
from kivy.core.audio import SoundLoader
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.carousel import Carousel
from kivy.uix.switch import Switch
from kivy.uix.slider import Slider
import sys


class CustomLayout(FloatLayout):
    def __init__(self, **kwargs):
        # suprascrierea initului vechi din modul
        super(CustomLayout, self).__init__(**kwargs)
        # var muzica_activa este o definita in acest namespace pt a avea efect in dezactivarea_volumului
        self.muzica_activa =0
        # obiectul layout0 este de tipul FloatLayout()
        self.layout0 = FloatLayout()
        # setam atributul source al obiect imag1
        self.imag1 = Image(source="logga.png")
        # adaugam fundalul ca si widget
        self.add_widget(self.imag1)
        # setam atributele layout0
        self.layout0.size = (600, 500)
        self.layout0.size_hint = (None, None)
        self.layout0.padding = 200
        self.imag1.add_widget(self.layout0)

        # Main function
        self.Menu(None)

    def Menu(self, Buton):
        # clear layout
        self.layout0.clear_widgets()
        # create button 1
        self.but1 = Button(text="TSP_imageview", bold=True, background_color=(0, 0, 1, 1))
        self.but1.pos = (300, 800)
        self.but1.size_hint = (0.3, 0.1)
        self.but1.opacity = 0.7
        # adaugarea ca si widget a but1 pe layout0
        self.layout0.add_widget(self.but1)

        # create button 2
        self.but2 = Button(text="TSP_GUI", bold=True, background_color=(0, 0, 1, 1))
        self.but2.pos = (300, 300)
        self.but2.size_hint = (0.3, 0.1)
        self.but2.opacity = 0.7
        self.layout0.add_widget(self.but2)

        # create button 3
        self.but3 = Button(text="TSP_settings", bold=True, background_color=(0, 0, 1, 1))
        self.but3.pos = (300, 220)
        self.but3.size_hint = (0.3, 0.1)
        self.but3.opacity = 0.7
        self.layout0.add_widget(self.but3)

        # create button 4
        self.but4 = Button(text="TSF_process", bold=True, background_color=(0, 0, 1, 1))
        self.but4.pos = (300, 140)
        self.but4.size_hint = (0.3, 0.1)
        self.but4.opacity = 0.7
        self.layout0.add_widget(self.but4)

        # create button 5
        self.but5 = Button(text="TSF_process parallel", bold=True, background_color=(0, 0, 1, 1))
        self.but5.pos = (300, 140)
        self.but5.size_hint = (0.3, 0.1)
        self.but5.opacity = 0.7
        self.layout0.add_widget(self.but5)

        # create button 6
        self.but6 = Button(text="TSP_fileinfo", bold=True, background_color=(0, 0, 1, 1))
        self.but6.pos = (300, 140)
        self.but6.size_hint = (0.3, 0.1)
        self.but6.opacity = 0.7
        self.layout0.add_widget(self.but6)

        # create button 7
        self.but7 = Button(text="TSP_printseasons", bold=True, background_color=(0, 0, 1, 1))
        self.but7.pos = (300, 140)
        self.but7.size_hint = (0.3, 0.1)
        self.but7.opacity = 0.7
        self.layout0.add_widget(self.but7)

        # create button 8
        self.but8 = Button(text="TSP_viewfits", bold=True, background_color=(0, 0, 1, 1))
        self.but8.pos = (300, 140)
        self.but8.size_hint = (0.3, 0.1)
        self.but8.opacity = 0.7
        self.layout0.add_widget(self.but8)

        # create button 9
        self.but9 = Button(text="TSF_fit2time", bold=True, background_color=(0, 0, 1, 1))
        self.but9.pos = (300, 140)
        self.but9.size_hint = (0.3, 0.1)
        self.but9.opacity = 0.7
        self.layout0.add_widget(self.but9)

        # create button 10
        self.but10 = Button(text="TSF_fit2img", bold=True, background_color=(0, 0, 1, 1))
        self.but10.pos = (300, 140)
        self.but10.size_hint = (0.3, 0.1)
        self.but10.opacity = 0.7
        self.layout0.add_widget(self.but10)

        # create button 11
        self.but11 = Button(text="TSF_seas2img", bold=True, background_color=(0, 0, 1, 1))
        self.but11.pos = (300, 140)
        self.but11.size_hint = (0.3, 0.1)
        self.but11.opacity = 0.7
        self.layout0.add_widget(self.but11)

        # create button 12
        self.but12 = Button(text="TSF_merge", bold=True, background_color=(0, 0, 1, 1))
        self.but12.pos = (300, 140)
        self.but12.size_hint = (0.3, 0.1)
        self.but12.opacity = 0.7
        self.layout0.add_widget(self.but12)

        # se leaga evenimentele de apasare a butoanelor de metodele de mai jos
        self.but1.bind(on_press=self.TSP_imageview)
        self.but2.bind(on_press=self.TSP_GUI)
        self.but3.bind(on_press=self.TSP_settings)
        self.but4.bind(on_press=self.TSF_process)
        self.but5.bind(on_press=self.TSF_process_parallel)
        self.but6.bind(on_press=self.TSP_fileinfo)
        self.but7.bind(on_press=self.TSP_printseasons)
        self.but8.bind(on_press=self.TSP_viewfits)
        self.but9.bind(on_press=self.TSF_fit2time)
        self.but10.bind(on_press=self.TSF_fit2img)
        self.but11.bind(on_press=self.TSF_seas2img)
        self.but12.bind(on_press=self.TSF_merge)

    def TSP_imageview(self, Buton):
        # am curatat layoutul
        self.layout0.clear_widgets()

        # am adaptat programul din clasa folosind obiecte dar nu merge
        # setam directia in care vom misca cu mouse-ul imaginile
        self.carousel = Carousel(direction='right')
        # setam viteza de miscare
        self.carousel.anim_move_duration = 1
        self.carousel.loop = True
        self.carousel.size_hint = (0.7, 0.7)
        self.carousel.pos = (200, 120)
        self.carousel.add_widget(self.layout0)
        self.image1 = Image(source="nature1.jpg")
        self.carousel.add_widget(self.image1)
        self.image2 = Image(source="nature2.jpg")
        self.carousel.add_widget(self.image2)
        self.image3 = Image(source="nature3.jpg")
        self.carousel.add_widget(self.image3)
        self.image1 = Image(source="nature4.jpg")
        self.carousel.add_widget(self.image4)
        self.eticheta_final = Label(text="Am ajuns la finalul listei!", font_size=30)
        self.carousel.add_widget(self.eticheta_final)

        # cream widgetul inapoiButon
        self.inapoiButon = Button(text="Inapoi", bold=True, background_color=(0, 0, 1, 1))
        self.inapoiButon.pos = (200, 100)
        self.inapoiButon.size_hint = (0.7, 0.1)
        self.inapoiButon.opacity = 0.7
        self.layout0.add_widget(self.inapoiButon)
        # legam apasarea butonului de intoarcerea la meniul principal
        self.inapoiButon.bind(on_press=self.Menu)

    def TSP_GUI(self, Buton):
        self.layout0.clear_widgets()

        # Cream un widget Switch si atributele sale
        self.switch1 = Switch(text="muzica")
        self.switch1.active = True
        self.switch1.size_hint = (0.3, 0.2)
        self.switch1.pos = (300, 360)
        self.layout0.add_widget(self.switch1)
        # leaga Switch-ul de metoda dezactiveaza_volum
        self.switch1.bind(active=self.dezactiveaza_volum)

        # cream un widget Label si atributele sale
        # textul de pe acesta urmand sa se schimbe odata cu volumul
        self.arata_volum = Label(text="volum: 50")
        self.arata_volum.size_hint = (0.3, 0.1)
        self.arata_volum.pos = (300, 260)
        self.layout0.add_widget(self.arata_volum)

        # cream un widget Slider si atributele sale
        # nu am urmat exact indicatiile din cerinta pt. a crea atributele
        # am incercercat sa fac fereastra sa semene cu poza
        self.slide_muzica = Slider(min=0, max=100, value=50)
        self.slide_muzica.step = 5
        self.slide_muzica.pos = (300, 100)
        self.slide_muzica.size_hint = (0.3, 0.5)
        self.slide_muzica.orientation = "horizontal"
        self.layout0.add_widget(self.slide_muzica)
        # leaga Slider-ul de metoda valoare_volum
        self.slide_muzica.bind(value=self.valoare_volum)

        # crearea widgetu-lui inapoiButon si atributelor sale
        self.inapoiButon = Button(text="Inapoi", bold=True, background_color=(0, 0, 1, 1))
        self.inapoiButon.pos = (300, 120)
        self.inapoiButon.size_hint = (0.3, 0.1)
        self.inapoiButon.opacity = 0.7
        self.layout0.add_widget(self.inapoiButon)
        # legam apasarea butonului de intoarcerea la meniul principal
        self.inapoiButon.bind(on_press=self.Menu)

    def TSP_settings(self, Buton):
        # Apelam sys.exit()
        sys.exit()

    def valoare_volum(self, x, y):
        # modificam Labelul arata_volum aratand valoarea integer a slide-ului
        self.arata_volum.text = "volum: " + str(int(self.slide_muzica.value))
        self.sound.volume = self.slide_muzica.value / 100

    def dezactiveaza_volum(self, x, y):
        if (self.muzica_activa % 2 == 0):
            # slide-ul este dezactivat
            self.slide_muzica.disabled = True
            # stocam valoarea slidu-lui intr-o var temporara
            self.slide_muzica.value_temp = int(self.slide_muzica.value)
            # setam valorea volumului la 0
            self.slide_muzica.value = 0
        else:
            # facem slide-ul iar available
            self.slide_muzica.disabled = False
            # reluam volumul melodiei din variabila temporara
            self.slide_muzica.value = int(self.slide_muzica.value_temp)
            self.sound.play()
        # folosim aceasta variabila pt. a contoriza switch-ul
        self.muzica_activa += 1

    def TSF_process(self, Buton):
        # crearea widgetu-lui inchide si atributelor sale
        self.inchide = Button(text="Inapoi", background_color=(0, 0, 1, 1))
        self.inchide.pos = (300, 120)
        self.inchide.size_hint = (1, 0.1)
        # legam apasarea butonului de intoarcerea la meniul principal
        self.inchide.bind(on_press=self.inchide_popup)

        # cream Label
        self.eticheta = Label(text="Multumiri InfoAcademy", bold=True, font_size=24)

        self.layout1 = BoxLayout()
        self.layout1.orientation = "vertical"
        self.layout1.padding = 40
        self.layout1.add_widget(self.eticheta)
        self.layout1.add_widget(self.inchide)
        self.popup = Popup()
        self.popup.background = "fundal4_tema.jpg"
        self.popup.size_hint = (None, None)
        self.popup.size = (400, 400)
        self.popup.title = 'Cine a creat aplicatia?'
        self.popup.content = self.layout1
        self.popup.open()

    def inchide_popup(self, Buton):
        self.popup.dismiss()

    def TSF_process_parallel(self, Buton):
        sys.exit()

    def TSF_process_parallel(self, Buton):
        sys.exit()

    def TSP_fileinfo(self, Buton):
        sys.exit()
    def TSP_printseasons(self, Buton):
        sys.exit()
    def TSP_viewfits(self, Buton):
        sys.exit()
    def TSF_fit2time(self, Buton):
        sys.exit()
    def TSF_fit2img(self, Buton):
        sys.exit()
    def TSF_seas2img(self, Buton):
        sys.exit()
    def TSF_merge(self, Buton):
        sys.exit()

class MainApp(App):
    def build(self):
        #self.icon ="python1.ico"
        return CustomLayout()


if __name__ == "__main__":
    MainApp().run()