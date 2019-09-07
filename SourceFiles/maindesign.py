from designer import Ui_designer
from PyQt5 import QtWidgets
from wolframclient.language import wl
from wolframclient.language import wlexpr
from wolframclient.evaluation import WolframLanguageSession
from PIL import Image
from wolframclient.language import Global
from PyQt5.QtGui import QIcon, QPixmap
import sys

class mywindow(QtWidgets.QMainWindow):
	def __init__(self):
		super(mywindow, self).__init__()
		self.ui = Ui_designer()
		self.ui.setupUi(self)
		self.ui.pushButton_2.clicked.connect(lambda :self.ui.stackedWidget.setCurrentIndex(1))
		self.ui.pushButton_5.clicked.connect(lambda :self.ui.stackedWidget.setCurrentIndex(0))
		topics=session.evaluate('''Keys[questionRepo["Easy"]]''')
		self.ui.comboBox_4.addItems(list(topics))
		self.ui.comboBox.addItems(['Easy','Normal','Hard'])
		self.ui.comboBox_3.addItems(list(topics))
		self.ui.pushButton_3.clicked.connect(self.addTopic)
		self.ui.pushButton_4.clicked.connect(self.deleteTopic)
		self.ui.pushButton.clicked.connect(self.compile)

	def deleteTopic(self):
		print(session.evaluate(wlexpr('''Keys[questionRepo["Easy"]]''')))
		selectedTopic = self.ui.comboBox_3.currentText()
		topicIndex = self.ui.comboBox_3.currentIndex()
		self.ui.comboBox_3.removeItem(topicIndex)
		self.ui.comboBox_4.removeItem(topicIndex)
		session.evaluate(wlexpr('''deleteTopic[ToString['''+str(selectedTopic)+''']]'''))
		session.evaluate(wlexpr('''Export["repo.mx",questionRepo]'''))
		print(session.evaluate(wlexpr('''Keys[questionRepo["Easy"]]''')))


	def addTopic(self):
		print(session.evaluate(wlexpr('''Keys[questionRepo["Easy"]]''')))
		topic = self.ui.lineEdit_5.text()
		session.evaluate(wlexpr('''addNewTopic[ToString['''+str(topic)+''']]'''))
		self.ui.comboBox_4.addItem(topic)
		self.ui.comboBox_3.addItem(topic)
		session.evaluate(wlexpr('''Export["repo.mx",questionRepo]'''))
		print(session.evaluate(wlexpr('''Keys[questionRepo["Easy"]]''')))

	def compile(self):
		print('''Hold[Export["0.png",Rasterize[GraphicsRow[{'''+self.ui.lineEdit_6.text()+'''}]]]]''')
		print('''ToString['''+self.ui.lineEdit_3.text()+''']''')
		print('''Hold['''+self.ui.lineEdit_2.text()+''']''')
		print(self.ui.lineEdit.text())
		print('''Hold['''+self.ui.lineEdit_4.text()+''']''')




if __name__ == '__main__':
	session = WolframLanguageSession()
	commands = [
	'''Get["definitions.mx"];''',
	'''questionRepo=Quiet@Import["repo.mx"];'''
	]
	for i in commands:
		session.evaluate(wlexpr(i))
		
	app = QtWidgets.QApplication([])
	application = mywindow()
	application.show()
	try:
		sys.exit(app.exec())
	except SystemExit:
		session.terminate()		
		print("Wolfram Link has been terminated.")
