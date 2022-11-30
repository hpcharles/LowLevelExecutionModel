
all:
	pdflatex main
	pdflatex main
	cp main.pdf ModeleExecutionAndHybrogen.pdf
nup:
	pdfnup --nup 1x4 --offset "-4cm 0cm" --no-landscape main.pdf

clean:
	cleantex -a main.tex
