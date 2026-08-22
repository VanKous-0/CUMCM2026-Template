LATEXMK ?= latexmk

.PHONY: pdf clean check

pdf:
	$(LATEXMK) -xelatex -interaction=nonstopmode -halt-on-error main.tex

clean:
	$(LATEXMK) -C main.tex

check: pdf
	@! grep -E "LaTeX Error|Undefined control sequence|undefined references|Citation .* undefined|Reference .* undefined|Overfull \\hbox \\([1-9][0-9]*(\\.[0-9]+)?pt too wide\\)" main.log
