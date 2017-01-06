from PySide.QtCore import *
from PySide.QtGui import *

import os, os.path, json, sys, subprocess, datetime, re


class RestoreThread(QThread):

	progress=Signal(str,int)
	done=Signal(str)

	def __init__(self,app,restoreDir):
		self.app=app
		self.restoreDir=restoreDir
		QThread.__init__(self)
	
	
	def run(self):
		try:
			s=self.restoreDir
			if not os.path.isdir(s):
				raise Exception('No such directory: %s'%s)
				
			t=self.app.getSource()
			if not t:
				raise Exception('No target directory.')
				
			if not os.path.isdir(t):
				os.makedirs(t)
	
			
			while t[-1]=='/':
				t=t[:-1]
			
			fileNumber=0
					
			# SIMULATION TO GET FILE COUNT
			process = subprocess.Popen(['rsync','-avvn',s+'/',t], stdout=subprocess.PIPE, universal_newlines=True,bufsize=1,cwd=s)
			for line in iter(process.stdout.readline, ''):
				if line!='':
					fileNumber+=1
					self.progress.emit('Counting files...'+str(fileNumber),0)
			fileCount=0
			
			# RSYNC 
			process = subprocess.Popen(['rsync','-avv',s+'/',t], stdout=subprocess.PIPE, universal_newlines=True,bufsize=1,cwd=s)
			for line in iter(process.stdout.readline, ''):
				if line!='':
					fileCount+=1
					if fileCount>=fileNumber:
						perc=100
					else:
						perc=int(fileCount*100/fileNumber)
					self.progress.emit(line,perc)
			
			self.done.emit(None)
		
		except Exception as err:
			self.done.emit(str(err))
			raise err
			

