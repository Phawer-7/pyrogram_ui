from pyrogram import Client, filters

from PyQt5 import QtWidgets, QtCore
import ui

class Telegram(QtWidgets.QMainWindow, ui.Ui_MainWindow):
	def __init__(self):
		super().__init__()

		self.setupUi(self)

		self.pushButton_2.pressed.connect(self.sebd_message)
		self.pushButton.pressed.connect(self.auto_answer)

	def auto_answer(self):
		auto = self.lineEdit_3.text()
		app = Client("my_account")
		@app.on_message(filters.private)

		async def hello(client, message):
			await message.reply_text(auto)

		app.run()	

	def sebd_message(self):
		app = Client("my_account")
		msg = self.lineEdit.text()
		who = self.lineEdit_2.text()

		with app:
			app.send_message(who, msg)


app_run = QtWidgets.QApplication([])		
window = Telegram()
window.show()
app_run.exec_()