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

# +
tex = tex.replace(r'\usepackage{sphinx}', '\\usepackage{sphinx}\n\\usepackage{booktabs}')
tex = re.sub(regex, '', tex, flags=re.MULTILINE)
tex = re.sub(r'\\llap\{\\color\{nbsphinxin\}\[\d+\]:\\,\\hspace\{\\fboxrule}\\hspace\{\\fboxsep\}\}', '', tex)
tex = re.sub(r'\\llap\{\\color\{nbsphinxout\}\[\d+\]:\\,\\hspace\{\\fboxrule}\\hspace\{\\fboxsep\}\}', '', tex)
tex = re.sub(r'\\savebox\\nbsphinxpromptbox\[0pt\]\[r\]\{\\color\{nbsphinxout\}\\Verb\|\\strut{\[\d+\]:\}\\,\|\}', '', tex)
tex = tex.replace(r'\textasciigrave{} \textless{}\textgreater{}\textasciigrave{}\_\_', '')
tex = tex.replace(r'\chapter{Preface}', r'\chapter*{Preface}')
tex = tex.replace(r'\section{Target audience}', r'\section*{Target audience}')
tex = tex.replace(r'\section{Prerequisites}', r'\section*{Prerequisites}')
tex = tex.replace(r'\section{Installation of Required Software}', r'\section*{Installation of Required Software}')
tex = tex.replace(r'\section{State of the Online Book}', r'\section*{State of the Book}')
tex = tex.replace(r'\chapter{Appendix}', '\\appendix\n\\chapter{Appendix}')
tex = tex.replace(r'\section{Mathematical Notations}', r'\section*{Mathematical Notations}')

confMatReplace = r'''
\begin{savenotes}\sphinxattablestart
\centering
\begin{tabular}{l|l|c|c|c|}
\multicolumn{2}{c}{} & \multicolumn{3}{c}{actual class} \\ \cline{3-5}
\multicolumn{2}{c|}{} & whale & bear & other \\ \cline{2-5}
& whale & 29 & 1 & 3 \\ \cline{2-5}
Predicted class & bear & 2 & 22 & 13 \\ \cline{2-5}
& other & 4 & 11 & 51 \\ \cline{2-5}
\end{tabular}
\par
\sphinxattableend\end{savenotes}'''

confMat = r'''
\begin{sphinxVerbatim}[commandchars=\\\{\}]
\PYG{o}{\PYGZlt{}}\PYG{n}{tr}\PYG{o}{\PYGZgt{}}\PYG{o}{\PYGZlt{}}\PYG{n}{td}\PYG{o}{\PYGZgt{}}\PYG{o}{\PYGZlt{}}\PYG{o}{/}\PYG{n}{td}\PYG{o}{\PYGZgt{}}\PYG{o}{\PYGZlt{}}\PYG{n}{td} \PYG{n}{colspan}\PYG{o}{=}\PYG{l+m+mi}{4}\PYG{o}{\PYGZgt{}}\PYG{o}{\PYGZlt{}}\PYG{n}{b}\PYG{o}{\PYGZgt{}}\PYG{n}{Actual} \PYG{n}{class}\PYG{o}{\PYGZlt{}}\PYG{o}{/}\PYG{n}{b}\PYG{o}{\PYGZgt{}}\PYG{o}{\PYGZlt{}}\PYG{o}{/}\PYG{n}{td}\PYG{o}{\PYGZgt{}}\PYG{o}{\PYGZlt{}}\PYG{o}{/}\PYG{n}{tr}\PYG{o}{\PYGZgt{}}
\PYG{o}{\PYGZlt{}}\PYG{n}{tr}\PYG{o}{\PYGZgt{}}\PYG{o}{\PYGZlt{}}\PYG{n}{td} \PYG{n}{rowspan}\PYG{o}{=}\PYG{l+m+mi}{4}\PYG{o}{\PYGZgt{}}\PYG{o}{\PYGZlt{}}\PYG{n}{br}\PYG{o}{\PYGZgt{}}\PYG{o}{\PYGZlt{}}\PYG{n}{br}\PYG{o}{\PYGZgt{}}\PYG{o}{\PYGZlt{}}\PYG{n}{b}\PYG{o}{\PYGZgt{}}\PYG{n}{Predicted} \PYG{n}{class}\PYG{o}{\PYGZlt{}}\PYG{o}{/}\PYG{n}{b}\PYG{o}{\PYGZgt{}}\PYG{o}{\PYGZlt{}}\PYG{o}{/}\PYG{n}{td}\PYG{o}{\PYGZgt{}}\PYG{o}{\PYGZlt{}}\PYG{n}{td}\PYG{o}{\PYGZgt{}}\PYG{o}{\PYGZlt{}}\PYG{n}{td}\PYG{o}{\PYGZgt{}}\PYG{o}{\PYGZlt{}}\PYG{n}{b}\PYG{o}{\PYGZgt{}}\PYG{n}{whale}\PYG{o}{\PYGZlt{}}\PYG{o}{/}\PYG{n}{b}\PYG{o}{\PYGZgt{}}\PYG{o}{\PYGZlt{}}\PYG{o}{/}\PYG{n}{td}\PYG{o}{\PYGZgt{}}\PYG{o}{\PYGZlt{}}\PYG{n}{td}\PYG{o}{\PYGZgt{}}\PYG{o}{\PYGZlt{}}\PYG{n}{b}\PYG{o}{\PYGZgt{}}\PYG{n}{bear}\PYG{o}{\PYGZlt{}}\PYG{o}{/}\PYG{n}{b}\PYG{o}{\PYGZgt{}}\PYG{o}{\PYGZlt{}}\PYG{o}{/}\PYG{n}{td}\PYG{o}{\PYGZgt{}}\PYG{o}{\PYGZlt{}}\PYG{n}{td}\PYG{o}{\PYGZgt{}}\PYG{o}{\PYGZlt{}}\PYG{n}{b}\PYG{o}{\PYGZgt{}}\PYG{n}{other}\PYG{o}{\PYGZlt{}}\PYG{o}{/}\PYG{n}{b}\PYG{o}{\PYGZgt{}}\PYG{o}{\PYGZlt{}}\PYG{o}{/}\PYG{n}{td}\PYG{o}{\PYGZgt{}}\PYG{o}{\PYGZlt{}}\PYG{o}{/}\PYG{n}{tr}\PYG{o}{\PYGZgt{}}
\PYG{o}{\PYGZlt{}}\PYG{n}{tr}\PYG{o}{\PYGZgt{}}\PYG{o}{\PYGZlt{}}\PYG{n}{td}\PYG{o}{\PYGZgt{}}\PYG{o}{\PYGZlt{}}\PYG{n}{b}\PYG{o}{\PYGZgt{}}\PYG{n}{whale}\PYG{o}{\PYGZlt{}}\PYG{o}{/}\PYG{n}{b}\PYG{o}{\PYGZgt{}}\PYG{o}{\PYGZlt{}}\PYG{o}{/}\PYG{n}{td}\PYG{o}{\PYGZgt{}}\PYG{o}{\PYGZlt{}}\PYG{n}{td}\PYG{o}{\PYGZgt{}}\PYG{l+m+mi}{29}\PYG{o}{\PYGZlt{}}\PYG{o}{/}\PYG{n}{td}\PYG{o}{\PYGZgt{}}\PYG{o}{\PYGZlt{}}\PYG{n}{td}\PYG{o}{\PYGZgt{}}\PYG{l+m+mi}{1}\PYG{o}{\PYGZlt{}}\PYG{o}{/}\PYG{n}{td}\PYG{o}{\PYGZgt{}}\PYG{o}{\PYGZlt{}}\PYG{n}{td}\PYG{o}{\PYGZgt{}}\PYG{l+m+mi}{3}\PYG{o}{\PYGZlt{}}\PYG{o}{/}\PYG{n}{td}\PYG{o}{\PYGZgt{}}\PYG{o}{\PYGZlt{}}\PYG{o}{/}\PYG{n}{tr}\PYG{o}{\PYGZgt{}}
\PYG{o}{\PYGZlt{}}\PYG{n}{tr}\PYG{o}{\PYGZgt{}}\PYG{o}{\PYGZlt{}}\PYG{n}{td}\PYG{o}{\PYGZgt{}}\PYG{o}{\PYGZlt{}}\PYG{n}{b}\PYG{o}{\PYGZgt{}}\PYG{n}{bear}\PYG{o}{\PYGZlt{}}\PYG{o}{/}\PYG{n}{b}\PYG{o}{\PYGZgt{}}\PYG{o}{\PYGZlt{}}\PYG{o}{/}\PYG{n}{td}\PYG{o}{\PYGZgt{}}\PYG{o}{\PYGZlt{}}\PYG{n}{td}\PYG{o}{\PYGZgt{}}\PYG{l+m+mi}{2}\PYG{o}{\PYGZlt{}}\PYG{o}{/}\PYG{n}{td}\PYG{o}{\PYGZgt{}}\PYG{o}{\PYGZlt{}}\PYG{n}{td}\PYG{o}{\PYGZgt{}}\PYG{l+m+mi}{22}\PYG{o}{\PYGZlt{}}\PYG{o}{/}\PYG{n}{td}\PYG{o}{\PYGZgt{}}\PYG{o}{\PYGZlt{}}\PYG{n}{td}\PYG{o}{\PYGZgt{}}\PYG{l+m+mi}{13}\PYG{o}{\PYGZlt{}}\PYG{o}{/}\PYG{n}{td}\PYG{o}{\PYGZgt{}}\PYG{o}{\PYGZlt{}}\PYG{o}{/}\PYG{n}{tr}\PYG{o}{\PYGZgt{}}
\PYG{o}{\PYGZlt{}}\PYG{n}{tr}\PYG{o}{\PYGZgt{}}\PYG{o}{\PYGZlt{}}\PYG{n}{td}\PYG{o}{\PYGZgt{}}\PYG{o}{\PYGZlt{}}\PYG{n}{b}\PYG{o}{\PYGZgt{}}\PYG{n}{other}\PYG{o}{\PYGZlt{}}\PYG{o}{/}\PYG{n}{b}\PYG{o}{\PYGZgt{}}\PYG{o}{\PYGZlt{}}\PYG{o}{/}\PYG{n}{td}\PYG{o}{\PYGZgt{}}\PYG{o}{\PYGZlt{}}\PYG{n}{td}\PYG{o}{\PYGZgt{}}\PYG{l+m+mi}{4}\PYG{o}{\PYGZlt{}}\PYG{o}{/}\PYG{n}{td}\PYG{o}{\PYGZgt{}}\PYG{o}{\PYGZlt{}}\PYG{n}{td}\PYG{o}{\PYGZgt{}}\PYG{l+m+mi}{11}\PYG{o}{\PYGZlt{}}\PYG{o}{/}\PYG{n}{td}\PYG{o}{\PYGZgt{}}\PYG{o}{\PYGZlt{}}\PYG{n}{td}\PYG{o}{\PYGZgt{}}\PYG{l+m+mi}{51}\PYG{o}{\PYGZlt{}}\PYG{o}{/}\PYG{n}{td}\PYG{o}{\PYGZgt{}}\PYG{o}{\PYGZlt{}}\PYG{o}{/}\PYG{n}{tr}\PYG{o}{\PYGZgt{}}
\end{sphinxVerbatim}'''.strip()

tex = tex.replace(confMat, confMatReplace)

confMatReplace = r'''
\begin{savenotes}\sphinxattablestart
\centering
\begin{tabular}{l|l|c|c|}
\multicolumn{2}{c}{} & \multicolumn{2}{c}{actual class} \\ \cline{3-4}
\multicolumn{2}{c|}{} & true & false \\ \cline{2-4}
& true & true positive (TP) & false positive (FP)  \\ \cline{2-4}
Predicted class & false & false negative (FN) & true negative (FN) \\ \cline{2-4}
\end{tabular}
\par
\sphinxattableend\end{savenotes}'''

confMat = r'''
\begin{sphinxVerbatim}[commandchars=\\\{\}]
\PYG{o}{\PYGZlt{}}\PYG{n}{tr}\PYG{o}{\PYGZgt{}}\PYG{o}{\PYGZlt{}}\PYG{n}{td}\PYG{o}{\PYGZgt{}}\PYG{o}{\PYGZlt{}}\PYG{o}{/}\PYG{n}{td}\PYG{o}{\PYGZgt{}}\PYG{o}{\PYGZlt{}}\PYG{n}{td} \PYG{n}{colspan}\PYG{o}{=}\PYG{l+m+mi}{3}\PYG{o}{\PYGZgt{}}\PYG{o}{\PYGZlt{}}\PYG{n}{b}\PYG{o}{\PYGZgt{}}\PYG{n}{Actual} \PYG{n}{class}\PYG{o}{\PYGZlt{}}\PYG{o}{/}\PYG{n}{b}\PYG{o}{\PYGZgt{}}\PYG{o}{\PYGZlt{}}\PYG{o}{/}\PYG{n}{td}\PYG{o}{\PYGZgt{}}\PYG{o}{\PYGZlt{}}\PYG{o}{/}\PYG{n}{tr}\PYG{o}{\PYGZgt{}}
\PYG{o}{\PYGZlt{}}\PYG{n}{tr}\PYG{o}{\PYGZgt{}}\PYG{o}{\PYGZlt{}}\PYG{n}{td} \PYG{n}{rowspan}\PYG{o}{=}\PYG{l+m+mi}{3}\PYG{o}{\PYGZgt{}}\PYG{o}{\PYGZlt{}}\PYG{n}{br}\PYG{o}{\PYGZgt{}}\PYG{o}{\PYGZlt{}}\PYG{n}{br}\PYG{o}{\PYGZgt{}}\PYG{o}{\PYGZlt{}}\PYG{n}{b}\PYG{o}{\PYGZgt{}}\PYG{n}{Predicted} \PYG{n}{class}\PYG{o}{\PYGZlt{}}\PYG{o}{/}\PYG{n}{b}\PYG{o}{\PYGZgt{}}\PYG{o}{\PYGZlt{}}\PYG{o}{/}\PYG{n}{td}\PYG{o}{\PYGZgt{}}\PYG{o}{\PYGZlt{}}\PYG{n}{td}\PYG{o}{\PYGZgt{}}\PYG{o}{\PYGZlt{}}\PYG{n}{td}\PYG{o}{\PYGZgt{}}\PYG{o}{\PYGZlt{}}\PYG{n}{b}\PYG{o}{\PYGZgt{}}\PYG{n}{true}\PYG{o}{\PYGZlt{}}\PYG{o}{/}\PYG{n}{b}\PYG{o}{\PYGZgt{}}\PYG{o}{\PYGZlt{}}\PYG{o}{/}\PYG{n}{td}\PYG{o}{\PYGZgt{}}\PYG{o}{\PYGZlt{}}\PYG{n}{td}\PYG{o}{\PYGZgt{}}\PYG{o}{\PYGZlt{}}\PYG{n}{b}\PYG{o}{\PYGZgt{}}\PYG{n}{false}\PYG{o}{\PYGZlt{}}\PYG{o}{/}\PYG{n}{b}\PYG{o}{\PYGZgt{}}\PYG{o}{\PYGZlt{}}\PYG{o}{/}\PYG{n}{td}\PYG{o}{\PYGZgt{}}\PYG{o}{\PYGZlt{}}\PYG{o}{/}\PYG{n}{tr}\PYG{o}{\PYGZgt{}}
\PYG{o}{\PYGZlt{}}\PYG{n}{tr}\PYG{o}{\PYGZgt{}}\PYG{o}{\PYGZlt{}}\PYG{n}{td}\PYG{o}{\PYGZgt{}}\PYG{o}{\PYGZlt{}}\PYG{n}{b}\PYG{o}{\PYGZgt{}}\PYG{n}{true}\PYG{o}{\PYGZlt{}}\PYG{o}{/}\PYG{n}{b}\PYG{o}{\PYGZgt{}}\PYG{o}{\PYGZlt{}}\PYG{o}{/}\PYG{n}{td}\PYG{o}{\PYGZgt{}}\PYG{o}{\PYGZlt{}}\PYG{n}{td}\PYG{o}{\PYGZgt{}}\PYG{n}{true} \PYG{n}{positive} \PYG{p}{(}\PYG{n}{TP}\PYG{p}{)}\PYG{o}{\PYGZlt{}}\PYG{o}{/}\PYG{n}{td}\PYG{o}{\PYGZgt{}}\PYG{o}{\PYGZlt{}}\PYG{n}{td}\PYG{o}{\PYGZgt{}}\PYG{n}{false} \PYG{n}{positive} \PYG{p}{(}\PYG{n}{FP}\PYG{p}{)}\PYG{o}{\PYGZlt{}}\PYG{o}{/}\PYG{n}{td}\PYG{o}{\PYGZgt{}}\PYG{o}{\PYGZlt{}}\PYG{o}{/}\PYG{n}{tr}\PYG{o}{\PYGZgt{}}
\PYG{o}{\PYGZlt{}}\PYG{n}{tr}\PYG{o}{\PYGZgt{}}\PYG{o}{\PYGZlt{}}\PYG{n}{td}\PYG{o}{\PYGZgt{}}\PYG{o}{\PYGZlt{}}\PYG{n}{b}\PYG{o}{\PYGZgt{}}\PYG{n}{false}\PYG{o}{\PYGZlt{}}\PYG{o}{/}\PYG{n}{b}\PYG{o}{\PYGZgt{}}\PYG{o}{\PYGZlt{}}\PYG{o}{/}\PYG{n}{td}\PYG{o}{\PYGZgt{}}\PYG{o}{\PYGZlt{}}\PYG{n}{td}\PYG{o}{\PYGZgt{}}\PYG{n}{false} \PYG{n}{negative} \PYG{p}{(}\PYG{n}{FN}\PYG{p}{)}\PYG{o}{\PYGZlt{}}\PYG{o}{/}\PYG{n}{td}\PYG{o}{\PYGZgt{}}\PYG{o}{\PYGZlt{}}\PYG{n}{td}\PYG{o}{\PYGZgt{}}\PYG{n}{true} \PYG{n}{negative} \PYG{p}{(}\PYG{n}{TN}\PYG{p}{)}\PYG{o}{\PYGZlt{}}\PYG{o}{/}\PYG{n}{td}\PYG{o}{\PYGZgt{}}\PYG{o}{\PYGZlt{}}\PYG{o}{/}\PYG{n}{tr}\PYG{o}{\PYGZgt{}}
\end{sphinxVerbatim}'''.strip()

tex = tex.replace(confMat, confMatReplace)

mathTable = r'''\begin{savenotes}\sphinxatlongtablestart\begin{longtable}[c]{|l|l|}
\hline
\sphinxstyletheadfamily 
Notation
&\sphinxstyletheadfamily 
Definition
\\
\hline
\endfirsthead'''

mathTableReplace = r'''\begin{savenotes}\sphinxatlongtablestart\begin{longtable}[c]{p{0.28\linewidth}p{0.68\linewidth}}
\hline
\sphinxstyletheadfamily 
Notation
&\sphinxstyletheadfamily 
Definition
\\
\hline
\endfirsthead'''

tex = tex.replace(mathTable, mathTableReplace)

# -


with open('_pdfbuild/latex/introductiontodatascience.tex', 'w') as tex_file:
    tex = tex_file.write(tex)
