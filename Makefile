PYTHON ?= python3
.PHONY: preview official test check clean
preview:
	$(PYTHON) scripts/build.py preview
official:
	$(PYTHON) scripts/build.py official
test:
	$(PYTHON) -m unittest discover -s tests -v
check:
	$(PYTHON) scripts/build.py check
clean:
	$(PYTHON) scripts/build.py clean
