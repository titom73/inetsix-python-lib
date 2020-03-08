
.PHONY: dev-start
dev-start:
	python setup.py develop

.PHONY: dev-stop
dev-stop:
	python setup.py develop --uninstall
