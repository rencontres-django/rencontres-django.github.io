PY?=python3
PELICAN?=pelican
PELICANOPTS=

BASEDIR=$(CURDIR)
INPUTDIR=$(BASEDIR)/content
OUTPUTDIR=$(BASEDIR)/../2019
CONFFILE=$(BASEDIR)/pelicanconf.py
PUBLISHCONF=$(BASEDIR)/publishconf.py

GITHUB_PAGES_BRANCH=master


DEBUG ?= 0
ifeq ($(DEBUG), 1)
	PELICANOPTS += -D
endif

RELATIVE ?= 0
ifeq ($(RELATIVE), 1)
	PELICANOPTS += --relative-urls
endif

.PHONY: help theme/static/css/style.css html

help:
	@echo 'Makefile for a pelican Web site                                           '
	@echo '                                                                          '
	@echo 'Usage:                                                                    '
	@echo '   make html                           (re)generate the web site          '
	@echo '   make clean                          remove the generated files         '
	@echo '   make regenerate                     regenerate files upon modification '
	@echo '   make publish                        generate using production settings '
	@echo '   make serve [PORT=8000]              serve site at http://localhost:8000'
	@echo '   make serve-global [SERVER=0.0.0.0]  serve (as root) to $(SERVER):80    '
	@echo '   make devserver [PORT=8000]          serve and regenerate together      '
	@echo '   make ssh_upload                     upload the web site via SSH        '
	@echo '   make rsync_upload                   upload the web site via rsync+ssh  '
	@echo '   make github                         upload the web site via gh-pages   '
	@echo '                                                                          '
	@echo 'Set the DEBUG variable to 1 to enable debugging, e.g. make DEBUG=1 html   '
	@echo 'Set the RELATIVE variable to 1 to enable relative urls                    '
	@echo '                                                                          '

theme/static/css/style.css: 
	node_modules/sass/sass.js scss/style.scss theme/static/css/style.css

theme/static/js/jquery.js:
	cp node_modules/jquery/dist/jquery.min.js theme/static/js

theme/static/js/leaflet.js:
	cp node_modules/leaflet/dist/leaflet.js* theme/static/js

theme/static/js/slick.min.js:
	cp node_modules/slick-carousel/slick/slick.min.js theme/static/js

theme/static/js/materialize.min.js:
	cp node_modules/materialize-css/dist/js/materialize.min.js theme/static/js

theme/static/fonts/material-icons:
	mkdir theme/static/fonts/material-icons/
	cp node_modules/material-icons/iconfont/*.woff* theme/static/fonts/material-icons/

html: clean theme/static/css/style.css theme/static/js/leaflet.js theme/static/js/slick.min.js theme/static/js/materialize.min.js theme/static/fonts/material-icons
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

clean:
	[ ! -d $(OUTPUTDIR) ] || rm -rf $(OUTPUTDIR)

regenerate:
	$(PELICAN) -r $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

serve:
ifdef PORT
	$(PELICAN) -l $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS) -p $(PORT)
else
	$(PELICAN) -l $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)
endif

serve-global:
ifdef SERVER
	$(PELICAN) -l $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS) -p $(PORT) -b $(SERVER)
else
	$(PELICAN) -l $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS) -p $(PORT) -b 0.0.0.0
endif


devserver:
ifdef PORT
	$(PELICAN) -lr $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS) -p $(PORT)
else
	$(PELICAN) -lr $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)
endif

publish:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(PUBLISHCONF) $(PELICANOPTS)

install:
	pip install -r requirements.txt
	npm install

.PHONY: html help clean regenerate serve serve-global devserver stopserver publish github