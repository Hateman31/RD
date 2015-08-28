from kivy.app import App
from kivy.uix.boxlayout	import BoxLayout
import json
import os
import tools

from kivy.config import Config
pairs = {
		'fullscreen': '0',
		'resizable': '0'
		}
Config.setall('graphics',pairs)
with open('data1') as f:
	data = json.loads(f.read())

class Root(BoxLayout):
	keys = ('tank','map','battle_type')
	tanks,maps,battles = map(sorted,(data[x] for x in keys))
	path = ''
	if os.path.exists('data.txt'):
		with open('data.txt') as f:
			path = f.read()
	def attack(self):
		'''Main function. It start searching and loading goods'''
		self.stuff['path'] = self.path
		tools.action(self.stuff)
		#...
	def folder(self,path):
		'''записывает в конфиг папку для сохранений'''
		cwd = os.path.join(os.getcwd(),'data.txt')
		if not os.path.exists(cwd):
			with open(cwd,'w') as f:
				f.write(path)
		self.path = path

class SummApp(App):
		config = self.config
		self.title = 'Replays Downloader'
		print(self.config)
		return Root()
if __name__ == '__main__':
	SummApp().run()
