default: all

RST = $(wildcard *.rst)
HTML = $(RST:.rst=.html)

DOTS = $(wildcard *.dot)
PNGS = $(DOTS:.dot=.png)

.PHONY: all clean

all: $(HTML) $(PNGS)

%.html: %.rst
	landslide config.cfg

%.png: %.dot
	dot -Tpng -o $@ $<
	convert -resize '80%' $@ $@

clean:
	-rm -f $(HTML) $(PNGS)
