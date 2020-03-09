
.PHONY: dev-start
dev-start:
	python setup.py develop

.PHONY: dev-stop
dev-stop:
	python setup.py develop --uninstall

.PHONY: coverage
coverage:
	coverage run -m pytest tests
	rm -f *.xlsx
	coverage report -m