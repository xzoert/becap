UIS  		= MainWindowUi.py 
UIC   		= pyside-uic --from-imports 


.PHONY: all
all: $(UIS)

MainWindowUi.py: MainWindowUi.ui
	$(UIC) MainWindowUi.ui -o $@


clean:
	rm $(UIS)

