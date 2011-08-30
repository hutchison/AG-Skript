AxiomatischeGeometrie.pdf: AxiomatischeGeometrie.tex Desargues.tex Descartes.tex Euklid.tex GeometrieLatexMacros.tex Hilbert.tex
	pdflatex AxiomatischeGeometrie.tex

clean:
	rm *.log
