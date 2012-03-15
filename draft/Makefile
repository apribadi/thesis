all:
	xelatex *.tex
stuff:
	xelatex *.tex
	bibtex *.aux
	makeindex *.idx
	xelatex *.tex
	xelatex *.tex

clean:
	rm -f *.aux *.bbl *.blg *.idx *.ilg *.ind *.log *.toc
