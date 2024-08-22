

FILE = src src.DeepRL src.DeepRL.Game src.DeepRL.Board src.DeepRL.Cell src.DeepRL.opponent src.DeepRL.opponent.Opponent src.DeepRL.opponent.RandomPlayer src.DeepRL.opponent.Player src.DeepRL.opponent.QLearningTTT

TEST_FILE = src.DeepRL.test_Game src.DeepRL.test_Cell src.DeepRL.test_Board src.DeepRL.opponent.test_RandomPlayer


all :
	@make doc
	@make test
	@make run


doc :
	@echo ------
	@echo Generating doc
	@echo ------
	
	@mkdir doc
	@python3 -m pydoc -w $(FILE)
	@mv *.html doc
	
	@echo ------
	@echo Doc generated
	@echo ------


test :
	@echo ------
	@echo Running Tests
	@echo ------
	
	@python3 -m unittest $(TEST_FILE)
	
	@echo ------
	@echo Tests finished
	@echo ------



run :
	@echo ------
	@echo Running programm
	@echo ------
	
	@python3 -m venv env
	@. env/bin/activate; pip install tqdm; pip install numpy; python3 src
	
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
