from doit.tools import run_once

def task_prelim():
    return {
            'targets': ['build'], # files produced
            'actions': ['mkdir build'],
            'uptodate': [run_once],
            'clean':True,
    }    

files=[
    'Chapter 00 - Front Matter.md',
    'Chapter 01 - Introduction.md',
    'Chapter 02 - Probability.md',
    #'chap-simple-applications.md'
]


def task_html_epub():
    import os

    return {
        'file_dep': ['build/measure_of_faith.html'],
        'targets': ['build/measure_of_faith.epub'],
        'actions': ['/Applications/calibre.app/Contents/MacOS/ebook-convert build/measure_of_faith.html build/measure_of_faith.epub --authors "Brian Blais" --language en --title "A Measure of Faith" --no-default-epub-cover --cover=images/cover.png'],
        'clean':True,
    }

def q(f):
    return ['"%s"' % _ for _ in f]

def task_md_html():
    import os

    fnames=[]
    for name in files:
        base,ext=os.path.splitext(name)
        mdfile="chapters/%s" % name
        fnames.append(mdfile)

    # this will make a self-contained version but takes a long time.  good for final

    standalone=False

    if standalone:
        return {
            'file_dep': fnames,
            'targets': ['build/measure_of_faith.html'],
            'actions': ['pandoc  --filter pandoc-citeproc  -s --toc --toc-depth=2 --top-level-division=chapter --self-contained --webtex  -o build/measure_of_faith.html %s' % (' '.join(q(fnames)))],
            'clean':True,
        }
    else:
        return {
            'file_dep': fnames,
            'targets': ['build/measure_of_faith.html'],
            'actions': ['pandoc  --filter pandoc-citeproc  -s --toc --toc-depth=2 --top-level-division=chapter --webtex https://latex.codecogs.com/svg.latex? -o build/measure_of_faith.html %s' % (' '.join(q(fnames)))],
            'clean':True,
        }



def task_md_tex():
    import os

    for name in files:
        base,ext=os.path.splitext(name)
        mdfile="chapters/%s" % name
        texfile='build/%s.tex' % base

        yield {
            'name': base,
            'file_dep': [mdfile,'config/config.yaml'],
            'targets': [texfile],
            'actions': ['pandoc --toc --filter pandoc-citeproc -o "%s" "%s"' % (texfile,mdfile)],
            'clean':True,
        }

def task_tex_tex():
    import os

    fnames=[]
    for name in files:
        base,ext=os.path.splitext(name)
        mdfile="chapters/%s" % name
        texfile='build/%s.tex' % base

        fnames.append(texfile)

    return {
        'file_dep': fnames,
        'targets': ['build/measure_of_faith.tex'],
        'actions': ['pandoc --toc -s --template=config/config.latex --top-level-division=chapter --filter pandoc-citeproc -o build/measure_of_faith.tex config/config.yaml %s' % (' '.join(q(fnames)))],
        'clean':True,
    }

from doit.task import clean_targets    
def task_tex_pdf():
    return {
        'file_dep': ['build/measure_of_faith.tex',],
        'targets': ['build/measure_of_faith.pdf'],
        'actions': ['pdflatex -halt-on-error -output-directory build build/measure_of_faith.tex', 
                    'pdflatex -halt-on-error -output-directory build build/measure_of_faith.tex', 
                    'cp build/measure_of_faith.pdf .'],
        'clean':[clean_targets,'rm -f build/*.log build/*.aux build/*.out build/*.synctex.gz'],
        'verbosity': 2,
    }



        