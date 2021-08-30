#!/usr/bin/env python
"""
Convert equations to pngs for html, epub, etc....
"""

import panflute as pf
from hashlib import md5
import tempfile
import os

dpi=170
def action(elem, doc):

    if isinstance(elem,pf.Math):
        eqn=pf.stringify(elem)
        eqnhash=md5(str(eqn).encode('ascii')).hexdigest()
        eqnim='_equation_images/eq%s.png' % eqnhash
        if not os.path.exists(eqnim):
            if not os.path.exists('_equation_images'):
                os.mkdir('_equation_images')

            tfname=tempfile.mktemp()
            base,_=os.path.split(tfname)
            with open(tfname+".tex",'w') as fid:
                if elem.format=='DisplayMath':
                    fid.write(r"""
\documentclass{article}
\usepackage{amsmath}
\thispagestyle{empty}
\begin{document}
\begin{displaymath}
 %s
\end{displaymath}
\end{document}
                    """ % eqn.strip())
                elif elem.format=='InlineMath':
                    fid.write(r"""
\documentclass{article}
\usepackage{amsmath}
\thispagestyle{empty}
\begin{document}
$%s$
\end{document}
                    """ % eqn.strip())

            # need to get rid of stdout for these because the filter uses it
            ret1=os.system('latex -output-directory=%s %s > /dev/null' % (base,tfname))
            ret2=os.system('dvipng -o %s -bg transparent -T tight -D %d %s.dvi  > /dev/null' % (eqnim,dpi,tfname))

        return pf.Image(elem,url=eqnim)


def main(doc=None):
    return pf.run_filter(action, doc=doc) 


if __name__ == '__main__':

    main()
