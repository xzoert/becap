SUBDIRS 	= becap

.PHONY: all $(SUBDIRS)
all: $(SUBDIRS)


$(SUBDIRS):
	$(MAKE) -C $@ $(MAKECMDGOALS)

clean: $(SUBDIRS)


