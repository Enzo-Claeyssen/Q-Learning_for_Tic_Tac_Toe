

FILE = src src.DeepRL src.DeepRL.Board src.DeepRL.Cell src.DeepRL.opponent src.DeepRL.opponent.Opponent src.DeepRL.opponent.RandomPlayer




all :
	@make doc
	@make run




doc :
	@echo ------
	@echo Generating doc
	@echo ------
	
	@mkdir doc
	@pydoc3 -w $(FILE)
	@mv *.html doc
	
	@echo ------
	@echo Doc generated
	@echo ------




run :
	@echo ------
	@echo Running programm
	@echo ------
	
	@python3 src
	
	@echo ------
	@echo Program ended
	@echo ------




clean :
	@echo ------
	@echo Cleaning directory
	@echo ------
	
	rm -r doc
	
	@echo ------
	@echo Directory cleaned
	@echo ------
