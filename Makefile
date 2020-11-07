# Versao python
PYTHON = python3.7

.DEFAULT_GOAL = help

help:
	@echo "---------------HELP-----------------"
	@echo "Para rodar escreva make run"
	@echo "------------------------------------"
	
run:
	${PYTHON} grafos2.py
