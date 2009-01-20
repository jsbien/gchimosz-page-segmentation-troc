all:
	# nothing to do
	

install:
	install -d "$(DESTDIR)/usr/share/mappage"
	install src/mappage "$(DESTDIR)/usr/bin/mappage"
	install src/segment-page.lua "$(DESTDIR)/usr/share/mappage/segment-page.lua"
	install src/filter-line.py "$(DESTDIR)/usr/share/mappage/filter-line.py"

clean:
