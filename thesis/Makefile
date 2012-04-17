all:
	xelatex thesis.tex
stuff:
	xelatex thesis.tex
	bibtex thesis.aux
	makeindex thesis.idx
	xelatex thesis.tex
	xelatex thesis.tex

clean:
	rm -f *.aux *.bbl *.blg *.idx *.ilg *.ind *.log *.toc
