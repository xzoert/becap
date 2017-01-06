from PySide.QtCore import *
from PySide.QtGui import *

import os, os.path, json, sys, subprocess, datetime

from .MainWindow import MainWindow
from .BackupThread import BackupThread
from .RestoreThread import RestoreThread

class Application(QApplication):
	
	
	backupDone=Signal(str)
	backupProgress=Signal(str,int)
	
	def __init__(self,confData=None):
		QApplication.__init__(self,*sys.argv)
		
		if not confData:
			confData={'dataDir':'~/.becap'}
			
		if 'dataDir' in confData:
			dataDir=confData['dataDir']
		else:
			dataDir='~/.becap'

		self.dataDir=os.path.abspath(dataDir)
		
		if not os.path.exists(self.dataDir):
			os.makedirs(self.dataDir)
		
		self.prefs={}
		self.prefFile=self.dataDir+'/prefs.json'
		if os.path.exists(self.prefFile):
			with open(self.prefFile,'r') as infile:
				self.prefs=json.load(infile)
		
		
		self.mainWindow=MainWindow(self)
		self.mainWindow.show()
		
		self.backupThread=None
		self.restoreThread=None
		
		self.exec_()


	def savePrefs(self):
		with open(self.prefFile,'w') as outfile:
			json.dump(self.prefs,outfile)
		

	def getSource(self):
		if 'source' in self.prefs:
			return self.prefs['source']
		
	def setSource(self,source):
		self.prefs['source']=source
		self.savePrefs()
		
	def getTarget(self):
		if 'target' in self.prefs:
			return self.prefs['target']
		
	def setTarget(self,target):
		self.prefs['target']=target
		self.savePrefs()

	def getExcludeList(self):
		if 'exclude' in self.prefs:
			return self.prefs['exclude']
		return {}
		
	def addExclude(self,path):
		if not 'exclude' in self.prefs:
			self.prefs['exclude']={}
		self.prefs['exclude'][path]=1
		self.savePrefs()
		
	def removeExclude(self,path):
		if 'exclude' in self.prefs and path in self.prefs['exclude']:
			del self.prefs['exclude'][path]
			self.savePrefs()
			
	def resetExclude(self,pathList):
		self.prefs['exclude']={}
		for path in pathList:
			self.prefs['exclude'][path]=1
		self.savePrefs()
		
	def relPath(self,path):
		s=self.getSource()
		if s and len(path)>len(s) and path[:len(s)]==s:
			return path[len(s)+1:]
		return path
		
	def getExcludeList(self):
		res=[]
		if 'exclude' in self.prefs:
			for path in self.prefs['exclude']:
				res.append(path)
				
		return res

	def doBackup(self):
		while self.backupThread and self.backupThread.isRunning():
			time.sleep(0.5)
		self.backupThread=BackupThread(self)
		self.backupThread.done.connect(self.emitBackupDone)
		self.backupThread.progress.connect(self.emitBackupProgress)
		self.backupThread.start()

	def doRestore(self,restoreDir):
		while self.restoreThread and self.restoreThread.isRunning():
			time.sleep(0.5)
		self.restoreThread=RestoreThread(self,restoreDir)
		self.restoreThread.done.connect(self.emitBackupDone)
		self.restoreThread.progress.connect(self.emitBackupProgress)
		self.restoreThread.start()


	def emitBackupDone(self,err):
		self.backupDone.emit(err)
		
	def emitBackupProgress(self,msg,perc):
		self.backupProgress.emit(msg,perc)
	
if __name__ == "__main__":
	app=Application()


