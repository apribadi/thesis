all:
	xelatex draft.tex
stuff:
	xelatex draft.tex
	bibtex draft.aux
	makeindex draft.idx
	xelatex draft.tex
	xelatex draft.tex

clean:
	rm -f *.aux *.bbl *.blg *.idx *.ilg *.ind *.log *.toc
