import json

class Settings:
	settings = None
	file = "settings.json"
	def __init__(self):
		self.load_file()

	def load_file(self):
		if not self.settings:
			f = open(self.file, "r", encoding="utf-8")
			try:
				decoder = json.loads(str(f.read()))
				self.settings = decoder
				f.close()
			except json.JSONDecodeError as e:
				print("The settings.josn file is malformat, please check the file.")
		return self.settings

	def save_settings(self):
		f = open(self.file, "w", encoding="utf-8")
		f.write(json.dumps(self.settings, ensure_ascii=False, indent=4))
		f.close()

	def get_settings(self):
		return self.load_file()