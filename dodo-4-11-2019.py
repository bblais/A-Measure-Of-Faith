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
    'Chapter 03 - Belief and Evidence.md',
    'Chapter 04 - The Case For God.md',
    'Chapter 05 - The Case for Jesus.md',
    'Chapter 06 - Miracles.md',
    'Chapter 07 - Faith.md',
]

def task_epub_azw3():
    return {
        'file_dep': ['build/measure_of_faith.epub'],
        'targets': ['build/measure_of_faith.azw3'],
        'actions': ['/Applications/calibre.app/Contents/MacOS/ebook-convert build/measure_of_faith.epub build/measure_of_faith.azw3', 
        'cp build/measure_of_faith.azw3 .'],
        'clean':True,
    }


def task_html_epub():
    import os

    return {
        'file_dep': ['build/measure_of_faith.html'],
        'targets': ['build/measure_of_faith.epub'],
        'actions': ['/Applications/calibre.app/Contents/MacOS/ebook-convert build/measure_of_faith.html build/measure_of_faith.epub --authors "Brian Blais" --language en --title "A Measure of Faith" --no-default-epub-cover --cover=images/cover.png', 
        'cp build/measure_of_faith.epub .'],
        'clean':True,
    }

def q(f):
    return ['"%s"' % _ for _ in f]

# ="https://latex.codecogs.com/png.latex?%%5Cdpi{200}"
#webtex=r"'https://latex.codecogs.com/png.latex?%%5Cdpi{170}'"

webtex=r"'https://latex.codecogs.com/svg.latex?'"
standalone=True

def fix_mdfile(fname):
    with open(fname) as fid:
        text=fid.read()

    text2=text.replace('\u200b','')
    if text2!=text:
        with open(fname,'w') as fid:
            fid.write(text2)



def task_md_html_individual():
    import os

    for name in files:
        base,ext=os.path.splitext(name)
        mdfile="chapters/%s" % name
        fix_mdfile(mdfile)

        htmlfile='build/%s.html' % base

        if standalone:  # this will make a self-contained version but takes a long time.  good for final
            s= "pandoc  --filter pandoc-citeproc  -s --toc --toc-depth=2 --top-level-division=chapter --self-contained --webtex=%s -o '%s' '%s' config/config.yaml" % (webtex,htmlfile,mdfile)
        else:
            s= "pandoc  --filter pandoc-citeproc  -s --toc --toc-depth=2 --top-level-division=chapter --webtex=%s -o '%s' '%s' config/config.yaml" % (webtex,htmlfile,mdfile)

        # if standalone:  # this will make a self-contained version but takes a long time.  good for final
        #     s= "pandoc  --filter pandoc-citeproc  -s --toc --toc-depth=2 --top-level-division=chapter --self-contained --mathjax -o '%s' '%s' config/config.yaml" % (htmlfile,mdfile)
        # else:
        #     s= "pandoc  --filter pandoc-citeproc  -s --toc --toc-depth=2 --top-level-division=chapter --mathjax -o '%s' '%s' config/config.yaml" % (htmlfile,mdfile)
   
    
        yield {
            'name':base,
            'file_dep': [mdfile,'config/config.yaml'],
            'targets': [htmlfile],
            'actions': [s],
            'clean':True,
        }


#  pandoc  --filter pandoc-citeproc  -s --toc --toc-depth=2 --top-level-division=chapter --webtex='https://latex.codecogs.com/png.latex?' -o "build/Chapter 00 - Front Matter.html" "chapters/Chapter 00 - Front Matter.md" config/config.yaml

#  pandoc  --filter pandoc-citeproc  -s --toc --toc-depth=2 --top-level-division=chapter --webtex='https://latex.codecogs.com/png.latex?%5Cdpi{150}' -o "build/Chapter 00 - Front Matter.html" "chapters/Chapter 00 - Front Matter.md" config/config.yaml


def task_md_html():
    import os

    fnames=[]
    for name in files:
        base,ext=os.path.splitext(name)
        mdfile="chapters/%s" % name
        fix_mdfile(mdfile)

        fnames.append(mdfile)


    if standalone: # this will make a self-contained version but takes a long time.  good for final
        s= "pandoc  --filter pandoc-citeproc  -s --toc --toc-depth=2 --top-level-division=chapter --self-contained --webtex=%s -o build/measure_of_faith.html %s config/config.yaml" % (webtex,' '.join(q(fnames)))
    else:
        s= 'pandoc  --filter pandoc-citeproc  -s --toc --toc-depth=2 --top-level-division=chapter --webtex=%s -o build/measure_of_faith.html %s config/config.yaml' % (webtex,' '.join(q(fnames)))

    
    
    return {
        'file_dep': fnames,
        'targets': ['build/measure_of_faith.html'],
        'actions': [s],
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
            'actions': ['pandoc --natbib --top-level-division=chapter  -o "%s" "%s"' % (texfile,mdfile)],
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
        'file_dep': fnames+ ['config/config.yaml'],
        'targets': ['build/measure_of_faith.tex'],
        'actions': ['pandoc -s --template=config/config.latex -M fontsize=12pt -M documentclass=book --top-level-division=chapter --toc --natbib --bibliography=chapters/main.bib  -o build/measure_of_faith.tex  --include-before=%s %s' % (q([fnames[0]])[0],' '.join(q(fnames[1:])))],
        'clean':True,
    }



from doit.task import clean_targets    
def task_tex_pdf():
    return {
        'file_dep': ['build/measure_of_faith.tex',],
        'targets': ['build/measure_of_faith.pdf'],
        'actions': ['pdflatex -halt-on-error -output-directory build build/measure_of_faith.tex', 
                    'bibtex "build/measure_of_faith"',
                    'pdflatex -halt-on-error -output-directory build build/measure_of_faith.tex', 
                    'pdflatex -halt-on-error -output-directory build build/measure_of_faith.tex', 
                    'cp build/measure_of_faith.pdf .'],
        'clean':[clean_targets,'rm -f build/*.log build/*.toc build/*.aux build/*.out build/*.bbl build/*.blg build/*.synctex.gz'],
        'verbosity': 2,
    }
