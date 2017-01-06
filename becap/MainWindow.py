from PySide.QtCore import *
from PySide.QtGui import *

import os.path

from .MainWindowUi import Ui_MainWindow
from .ExcludeFilterModel import ExcludeFilterModel


class MainWindow(QMainWindow):
	
	def __init__(self,app):
		self.app=app
		QMainWindow.__init__(self)
		self.ui=Ui_MainWindow()
		self.ui.setupUi(self)
		
		self.ui.sourceEdit.setText(app.getSource())
		self.ui.changeSourceButton.clicked.connect(self.openSourceDialog)
		self.ui.sourceEdit.textChanged.connect(self.sourceTextChanged)

		self.ui.targetEdit.setText(app.getTarget())
		self.ui.changeTargetButton.clicked.connect(self.openTargetDialog)
		self.ui.targetEdit.textChanged.connect(self.targetTextChanged)
		
		self.ui.statusLabel.setText('')
		self.ui.statusProgressBar.hide()
		
		self.excludeModel=ExcludeFilterModel(self.ui.excludeTableView,self.app)
		excludeList=self.app.getExcludeList()
		for path in excludeList:
			self.excludeModel.addEntry(path)
		self.excludeModel.changed.connect(self.excludeChanged)
		self.ui.addExcludeButton.clicked.connect(self.openExcludeDialog)
		
		self.ui.backupButton.clicked.connect(self.doBackup)
		
		self.app.backupProgress.connect(self.setBackupProgress)
		self.app.backupDone.connect(self.backupDone)
		
		self.ui.restoreButton.clicked.connect(self.doRestore)
		
	def doRestore(self):
		restoreDir = QFileDialog.getExistingDirectory(self,self.tr('Choose where to export'),self.app.getTarget())
		if restoreDir:
			self.app.doRestore(restoreDir)


	def doBackup(self):
		self.ui.backupButton.setDisabled(True)
		self.ui.restoreButton.setDisabled(True)
		self.ui.statusLabel.setText('')
		self.app.doBackup()
		
	def backupDone(self,err):
		if err:
			QMessageBox.warning(self,'Error during backup',err)
			
		self.ui.backupButton.setDisabled(False)
		self.ui.restoreButton.setDisabled(False)
		self.ui.statusLabel.setText('done.')
		self.ui.statusProgressBar.hide()
		
	def setBackupProgress(self,msg,perc):
		if len(msg)>80:
			msg=msg[:30]+'...'+msg[-47:]
		self.ui.statusLabel.setText(msg)
		if perc is not None:
			self.ui.statusProgressBar.show()
			self.ui.statusProgressBar.setValue(perc)
		


	def openExcludeDialog(self):
		w=QFileDialog()
		w.setDirectory(self.app.getSource())
		w.filesSelected.connect(self.addExcludeFiles)
		w.setFileMode(QFileDialog.DirectoryOnly)
		w.setFilter(QDir.Dirs | QDir.Hidden)
		w.setOption(QFileDialog.DontUseNativeDialog,True)
		l=w.findChild(QListView,"listView")
		if l:
			l.setSelectionMode(QAbstractItemView.MultiSelection)
		t = w.findChild(QTreeView)
		if t:
			t.setSelectionMode(QAbstractItemView.MultiSelection);
		res=w.exec_()

	def addExcludeFiles(self,files):
		for f in files:
			self.excludeModel.addEntry(f)




	def excludeChanged(self):
		self.app.resetExclude(self.excludeModel.getEntries())

	def openSourceDialog(self):
		path = QFileDialog.getExistingDirectory(self,self.tr('Source directory'),self.app.getSource())
		self.ui.sourceEdit.setText(path)
	
	def sourceTextChanged(self):
		path=os.path.abspath(self.ui.sourceEdit.text())
		if os.path.isdir(path):
			self.ui.sourceEdit.setStyleSheet('')
		else:
			self.ui.sourceEdit.setStyleSheet('color: red;')
		self.app.setSource(self.ui.sourceEdit.text())
			

	def openTargetDialog(self):
		path = QFileDialog.getExistingDirectory(self,self.tr('Target directory'),self.app.getTarget())
		self.ui.targetEdit.setText(path)
	
	def targetTextChanged(self):
		path=os.path.abspath(self.ui.targetEdit.text())
		if os.path.isdir(path):
			self.ui.targetEdit.setStyleSheet('')
		else:
			self.ui.targetEdit.setStyleSheet('color: red;')
		self.app.setTarget(self.ui.targetEdit.text())
			
		

