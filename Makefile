

FILE = src src.DeepRL src.DeepRL.opponent src.DeepRL.opponent.Opponent src.DeepRL.opponent.RandomPlayer


all :
	make doc


doc :
	mkdir doc
	pydoc3 -w $(FILE)
	mv *.html doc


clean :
	rm -r doc
