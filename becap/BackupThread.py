from PySide.QtCore import *
from PySide.QtGui import *

import os, os.path, json, sys, subprocess, datetime, re, shutil


class BackupThread(QThread):

	progress=Signal(str,int)
	done=Signal(str)

	def __init__(self,app):
		self.app=app
		QThread.__init__(self)
		self.aborted=False
	
	def abort(self):
		self.aborted=True
	
	def run(self):
		backupPath=None
		process=None
		fileCount=0
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
			
			if os.path.exists(lastPath):
				self.progress.emit('Copying last...',0)
				# COPY LAST AS HARD LINKS
				process = subprocess.Popen(['cp','-avl',lastPath+'/.',backupPath], stdout=subprocess.PIPE, universal_newlines=True,bufsize=1)
				for line in iter(process.stdout.readline, ''):
					if line!='':
						#print(line)
						pass
			else:
				os.mkdir(backupPath)



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
			process = subprocess.Popen(['rsync','-avvn','--exclude-from',excludeFilePath,s+'/',backupPath], stdout=subprocess.PIPE, universal_newlines=True,bufsize=1,cwd=s)
			for line in iter(process.stdout.readline, ''):
				if self.aborted:
					raise Exception('Aborted!')
				if line!='':
					fileNumber+=1
					self.progress.emit('Counting files...'+str(fileNumber),0)
			#print('File number',fileNumber)
			fileCount=0
			# RSYNC 
			process = subprocess.Popen(['rsync','-avv','--delete','--exclude-from',excludeFilePath,s+'/',backupPath], stdout=subprocess.PIPE, universal_newlines=True,bufsize=1,cwd=s)
			for line in iter(process.stdout.readline, ''):
				if self.aborted:
					raise Exception('Aborted!')
				if line!='':
					fileCount+=1
					if fileCount>=fileNumber:
						perc=90
					else:
						perc=int(fileCount*90/fileNumber)
					self.progress.emit(line,perc)
			
			
			fileCount=0
			# CREATE LINKS IN ALL
			if not os.path.isdir(allPath):
				os.mkdir(allPath)
			self.progress.emit('Creating links in all...',100)
			process = subprocess.Popen(['cp','-avvl',backupPath+'/.',allPath], stdout=subprocess.PIPE, universal_newlines=True,bufsize=1)
			for line in iter(process.stdout.readline, ''):
				if self.aborted:
					raise Exception('Aborted!')
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
			self.progress.emit('Aborting...',0)
			if process:
				try:
					print('Termninating process',process)
					process.terminate()
				except:
					pass
			if backupPath:
				try:
					removeCount=0
					process = subprocess.Popen(['rm','-rvf',backupPath], stdout=subprocess.PIPE, universal_newlines=True,bufsize=1)
					for line in iter(process.stdout.readline, ''):
						if line!='':
							removeCount+=1
							if removeCount>=fileCount:
								perc=100
							else:
								perc=int(removeCount*100/fileCount)
							self.progress.emit('Aborting...',perc)
					#print('Removing',backupPath)
					#shutil.rmtree(backupPath)
				except:
					pass
			self.done.emit(str(err))
			raise err
			

