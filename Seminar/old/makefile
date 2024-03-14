FRAMES := frame_hmmd.tex

sframe:	$(myfile).tex
	cat driver.tex | sed s/DRIVEME/$(myfile)/ > $(myfile)-sframe.tex
	pdflatex $(myfile)-sframe && pdflatex $(myfile)-sframe

lecture1:  lecture1.tex  $(FRAMES)
	pdflatex lecture1 && pdflatex lecture1
