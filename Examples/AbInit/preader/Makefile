preader-test:	
	@echo "Testing preader for Abinit...."
	@bash command.sh ${PYTHON_EXE} ${PREADER_OPTIONS} > command.csv
	@../../../checkcsv command.ref.csv command.csv

preader-regenerate:
	@echo "Regenerating reference files from Abinit...."
	@bash command.sh ${PYTHON_EXE} ${PREADER_OPTIONS} > command.ref.csv
