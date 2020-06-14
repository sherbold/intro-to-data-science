import re

regex = (r"\{\n"
        r"\\sphinxsetup\{VerbatimColor=\{named\}\{nbsphinx-code-bg\}\}\n"
        r"\\sphinxsetup\{VerbatimBorderColor=\{named\}{nbsphinx-code-border\}\}\n"
        r"\\begin{sphinxVerbatim}\[commandchars=\\\\\\{\\\}\]\n"
        r"\\llap{\\color{nbsphinxin}\[\d+\]:\\,\\hspace{\\fboxrule}\\hspace{\\fboxsep}}\n"
        r"\\end\{sphinxVerbatim\}\n"
        r"\}\n\n"
        r"\\hrule height -\\fboxrule\\relax\n"
        r"\\vspace\{\\nbsphinxcodecellspacing\}")

with open('_pdfbuild/latex/introductiontodatascience.tex', 'r') as tex_file:
    tex = tex_file.read()

tex = re.sub(regex, '', tex, flags=re.MULTILINE)
tex = re.sub(r'\\llap\{\\color\{nbsphinxin\}\[\d+\]:\\,\\hspace\{\\fboxrule}\\hspace\{\\fboxsep\}\}', '', tex)
tex = re.sub(r'\\llap\{\\color\{nbsphinxout\}\[\d+\]:\\,\\hspace\{\\fboxrule}\\hspace\{\\fboxsep\}\}', '', tex)
tex = tex.replace(r'\textasciigrave{} \textless{}\textgreater{}\textasciigrave{}\_\_', '')
tex = tex.replace(r'\chapter{Preface}', r'\chapter*{Preface}')
tex = tex.replace(r'\section{Target audience}', r'\section*{Target audience}')
tex = tex.replace(r'\section{Prerequisites}', r'\section*{Prerequisites}')
tex = tex.replace(r'\section{Installation of Required Software}', r'\section*{Installation of Required Software}')
tex = tex.replace(r'\section{State of the Online Book}', r'\section*{State of the Book}')


with open('_pdfbuild/latex/introductiontodatascience.tex', 'w') as tex_file:
    tex = tex_file.write(tex)