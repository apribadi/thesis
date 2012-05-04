all:
	xelatex thesis.tex

complete:
	xelatex thesis.tex
	bibtex thesis.aux
	xelatex thesis.tex
	xelatex thesis.tex

clean:
	rm -f *.aux *.bbl *.blg *.idx *.ilg *.ind *.log *.toc
