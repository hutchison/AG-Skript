TEX		= $(shell ls *.tex)
TIKZ	= $(shell ls tikz/*.tikz)

AxiomatischeGeometrie.pdf: $(TEX) $(TIKZ)
	pdflatex AxiomatischeGeometrie.tex

clean:
	rm -f *.log *.aux *.out
