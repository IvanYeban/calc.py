from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
import math

Window.size = (400,600)
Window.clearcolor = (0, 0, 0, 1)
Window.title = "Введи вес мяса"

class MyApp(App):

    def __init__(self):
        super().__init__()
        self.label = Label(text="КАЛЬКУЛЯТОР ДЛЯ ПЕЛЬМЕНЕЙ\n      Вес листа теста 160-200гр.")
        self.water = Label(text="Вода")
        self.egg = Label(text="Яйцо")
        self.oil = Label(text="Масло")
        self.dough_salt = Label(text="Соль в тесто")
        self.flour = Label(text="Мука")
        self.onion = Label(text="Лук")
        self.ground_meat_salt = Label(text="Соль для фарша")
        self.pepper = Label(text="Перец")
        self.garlic = Label(text="Чеснок")
        self.input_data = TextInput(hint_text = "Введи вес мяса в граммах", multiline=False)
        self.input_data.bind(text=self.on_text)

    def on_text(self, *args):
        data = self.input_data.text
        if data.isnumeric():
            data = int(data)
            meat = data

            # коэффициенты:

            coefficient = 1.8  # коэффициент умножения для расчета муки
            water = 0.25  # вода для теста
            egg = 0.0925  # яйцо для теста
            oil = 0.025  # масло для теста
            dough_salt = 0.0075  # соль для теста
            onion = 0.15  # лук для фарша
            ground_meat_salt = 0.01  # соль для фарша
            pepper = 0.0025  # перец дял фарша
            garlic = 0.02  # чеснок для фарша

            # расчет ингридиентов:

            calculated_water = round((water * meat)*1.7)
            calculated_egg = round((egg * meat)*1.7)
            calculated_oil = round((oil * meat)*1.7)
            calculated_dough_salt = round((dough_salt * meat)*1.7)
            calculated_onion = round(onion * meat)
            calculated_ground_meat_salt = round(ground_meat_salt * meat)
            calculated_pepper = round(pepper * meat)
            calculated_garlic = round(garlic * meat)
            calculated_flour = round((calculated_water+calculated_egg+calculated_oil+calculated_dough_salt)*coefficient)

            # средний вес 1 шт:

            average_weight_of_egg = 46.25
            average_weight_of_oil = 16.66667
            average_weight_of_dough_salt = 5
            average_weight_of_onion = 100
            average_weight_of_ground_meat_salt = 5
            average_weight_of_pepper = 2.5
            average_weight_of_garlic = 6.666667

            # расчет количества в штуках или в ложках

            quantity_egg = math.ceil(calculated_egg / average_weight_of_egg)
            quantity_oil = math.ceil(calculated_oil / average_weight_of_oil)
            quantity_dough_salt = math.ceil(calculated_dough_salt / average_weight_of_dough_salt)
            quantity_onion = math.ceil(calculated_onion / average_weight_of_onion)
            quantity_ground_meat_salt = math.ceil(calculated_ground_meat_salt / average_weight_of_ground_meat_salt)
            quantity_pepper = math.ceil(calculated_pepper / average_weight_of_pepper)
            quantity_garlic = math.ceil(calculated_garlic / average_weight_of_garlic)
            self.water.text ="Вес воды: "+ str(calculated_water) + "гр. "
            self.egg.text = "Вес яйца: " + str(calculated_egg) + "гр. или " + str(quantity_egg)+ " шт"
            self.oil.text = "Вес масла: " + str(calculated_oil) + "гр. или " + str(quantity_oil)+ " ст.л"
            self.dough_salt.text = "Вес соли для теста: " + str(calculated_dough_salt) + "гр. или " + str(quantity_dough_salt)+ " ч.л"
            self.flour.text = "Вес муки: " + str(calculated_flour) + "гр."
            self.onion.text = "Вес лука: " + str(calculated_onion) + "гр. или " + str(quantity_onion)+ " шт"
            self.ground_meat_salt.text = "Вес соли для фарша: " + str(calculated_ground_meat_salt) + "гр. или " + str(quantity_ground_meat_salt)+ " ч.л"
            self.pepper.text = "Вес перца: " + str(calculated_pepper) + "гр. или " + str(quantity_pepper)+ " ч.л"
            self.garlic.text = "Вес чеснока: " + str(calculated_garlic) + "гр. или " + str(quantity_garlic)+ " зуб"
        else:
            self.input_data.text = ""

    def build(self):
        box = BoxLayout(orientation="vertical")
        box.add_widget(self.label)
        box.add_widget(self.input_data)
        box.add_widget(self.water)
        box.add_widget(self.egg)
        box.add_widget(self.oil)
        box.add_widget(self.dough_salt)
        box.add_widget(self.flour)
        box.add_widget(self.onion)
        box.add_widget(self.ground_meat_salt)
        box.add_widget(self.pepper)
        box.add_widget(self.garlic)

        return box

if __name__=="__main__":
    MyApp().run()