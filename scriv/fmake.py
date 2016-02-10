#!/usr/bin/env python
from fabricate import *
import os

name='Measure Of Faith'
TOC = ('--toc','--toc-depth=2')

def build():
    tex()
    pdf()
    

def tex():
    run('mkdir','-p','build/tex')
    run('pandoc',TOC,
            '--template=book_template.tex',
            '-o','build/tex/%s.tex' % (name),
            '%s.md' % name)   

def pdf():
    # args=('-draftmode','-output-directory=build/pdf',
    #     '"build/tex/%s.tex"' % name,
    #     )

    # cmd='pdflatex ' + ' '.join(args)
    # os.system(cmd)

    run('mkdir','-p','build/pdf')

    run('pdflatex','-output-directory=build/pdf',
            'build/tex/%s.tex' % (name))

def pdf2():
    run('mkdir','-p','build/pdf')
    run('pdflatex','-draftmode','-output-directory=build/pdf',
            'build/tex/%s.tex' % (name))
    run('pdflatex','-output-directory=build/pdf',
            'build/tex/%s.tex' % (name))



def clean():
    autoclean()

main()
