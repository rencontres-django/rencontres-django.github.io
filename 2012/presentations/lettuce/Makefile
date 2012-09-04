RST = djangocong-2012-lettuce.rst
HTML=$(RST:.rst=.html)

.PHONY: all
all: $(HTML)

%.html: %.rst
	landslide config.cfg

clean:
	rm -f $(HTML)
