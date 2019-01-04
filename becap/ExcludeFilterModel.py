from PySide.QtCore import *
from PySide.QtGui import *
#from dedalus import *
#from dedalus.ui import icons


class ExcludeFilterModel(QAbstractTableModel):
	
	COL_DELETE=1
	COL_PATH=0
	
	changed=Signal()
	
	def __init__(self,view,app):
		QAbstractTableModel.__init__(self)
		self.view=view
		self.app=app
		self.entries=[]
		self.view.setModel(self)
		hh=self.view.horizontalHeader()
		hh.setResizeMode(self.COL_PATH,QHeaderView.Stretch)
		hh.setResizeMode(self.COL_DELETE,QHeaderView.Fixed)
		self.view.setColumnWidth(self.COL_DELETE,24)
		self.view.setSelectionMode(QAbstractItemView.NoSelection);
		self.view.clicked.connect(self.itemClicked)
		
		
		
	def itemClicked(self,idx):
		if idx.column()==self.COL_DELETE:
			self.removeEntry(idx.row())
		
	def rowCount(self,parent):
		return len(self.entries)
	
	def columnCount(self,parent):
		return 2
	
	def data(self, index, role):
		if not index.isValid():
			return 
		entry=self.entries[index.row()]
		if index.column()==self.COL_DELETE:
			if role==Qt.DisplayRole:
				return ' x'
		elif index.column()==self.COL_PATH:
			if role==Qt.DisplayRole:
				return self.app.relPath(entry)
					
			
	def refresh(self):
		self.layoutAboutToBeChanged.emit()
		self.layoutChanged.emit()

	def changedEvent(self):
		self.refresh()
		self.changed.emit()

	def removeEntry(self,idx):
		if idx<len(self.entries):
			del self.entries[idx]
			self.changedEvent()
			
	def addEntry(self,path):
		self.entries.append(path)
		self.changedEvent()
		
	def getEntries(self):
		return list(self.entries)
