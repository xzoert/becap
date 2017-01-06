from PySide.QtCore import *
from PySide.QtGui import *

import os, os.path, json, sys, subprocess, datetime, re


class BackupThread(QThread):

	progress=Signal(str,int)
	done=Signal(str)

	def __init__(self,app):
		self.app=app
		QThread.__init__(self)
		self.fileNumberRe=re.compile('Number of files\: \d+ \(reg\: (\d+), dir\: \d+\)')
	
	
	def run(self):
		try:
			s=self.app.getSource()
			if not os.path.isdir(s):
				raise Exception('No such directory: %s'%s)
				
			t=self.app.getTarget()
			if not t:
				raise Exception('No target directory.')
				
			if not os.path.isdir(t):
				os.makedirs(t)
	
			now=datetime.datetime.now()
			backupName=now.strftime('%Y-%m-%d_%H-%M')
			backupPath=t+'/'+backupName
			if os.path.exists(backupPath):
				raise Exception('Backup %s already exists'%backupName)
			allPath=t+'/all'
			lastPath=t+'/last'
			
			if os.path.isdir(lastPath):
				self.progress.emit('Copying last...',0)
				# COPY LAST AS HARD LINKS
				process = subprocess.Popen(['cp','-avl',lastPath+'/.',backupPath], stdout=subprocess.PIPE, universal_newlines=True,bufsize=1)
				for line in iter(process.stdout.readline, ''):
					if line!='':
						#print(line)
						pass
			else:
				os.mkdir(backupPath)

			if not os.path.isdir(allPath):
				os.mkdir(allPath)


			# CREATE THE EXCLUDE FILE
			tempPath=QDir.tempPath()
			excludeFilePath=tempPath+'/'+backupName
			f=open(excludeFilePath,'w')
			if 'exclude' in self.app.prefs:
				for path in self.app.prefs['exclude']:
					if s and len(path)>len(s) and path[:len(s)]==s:
						f.write('/'+path[len(s)+1:]+'\n')
			f.close()
					
			fileNumber=0
					
			# SIMULATION TO GET FILE COUNT
			self.progress.emit('Counting files...',0)
			process = subprocess.Popen(['rsync','-avvn','--exclude-from',excludeFilePath,s+'/',backupPath], stdout=subprocess.PIPE, universal_newlines=True,bufsize=1,cwd=s)
			for line in iter(process.stdout.readline, ''):
				fileNumber+=1
			#print('File number',fileNumber)
			fileCount=0
			# RSYNC 
			process = subprocess.Popen(['rsync','-avv','--delete','--exclude-from',excludeFilePath,s+'/',backupPath], stdout=subprocess.PIPE, universal_newlines=True,bufsize=1,cwd=s)
			for line in iter(process.stdout.readline, ''):
				if line!='':
					fileCount+=1
					if fileCount>=fileNumber:
						perc=90
					else:
						perc=int(fileCount*90/fileNumber)
					self.progress.emit(line,perc)
			
			
			fileCount=0
			# CREATE LINKS IN ALL
			self.progress.emit('Creating links in all...',100)
			process = subprocess.Popen(['cp','-avvl',backupPath+'/.',allPath], stdout=subprocess.PIPE, universal_newlines=True,bufsize=1)
			for line in iter(process.stdout.readline, ''):
				if line!='':
					#print(line)
					#self.progress.emit(line,0)
					fileCount+=1
					if fileCount>=fileNumber:
						perc=100
					else:
						perc=90+int(fileCount*10/fileNumber)
					self.progress.emit(line,perc)
			
			if os.path.exists(lastPath):
				os.remove(lastPath)
				
			os.symlink(backupName,lastPath)
			
			self.done.emit(None)
		
		except Exception as err:
			self.done.emit(str(err))
			raise err
			

