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
    'Chapter 08 - Conclusions.md',
]

def task_epub_azw3():
    return {
        'file_dep': ['build/measure_of_faith.epub'],
        'targets': ['build/measure_of_faith.azw3'],
        'actions': ['/Applications/calibre.app/Contents/MacOS/ebook-convert build/measure_of_faith.epub build/measure_of_faith.azw3', 
        'cp build/measure_of_faith.azw3  "./A Measure of Faith - Brian Blais.azw3"'],
        'clean':True,
    }


def task_html_epub():
    import os

    return {
        'file_dep': ['build/measure_of_faith.html'],
        'targets': ['build/measure_of_faith.epub'],
        'actions': ['/Applications/calibre.app/Contents/MacOS/ebook-convert build/measure_of_faith.html build/measure_of_faith.epub --authors "Brian Blais" --language en --title "A Measure of Faith" --no-default-epub-cover --cover=images/cover.png', 
        'cp build/measure_of_faith.epub "./A Measure of Faith - Brian Blais.epub"'],
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

# def task_last_compile():
#     import datetime

#     today=datetime.datetime.now()
#     with open("chapters/Chapter 00x - Last Compiled.md","w") as fid:
#         fid.write("""
# ### Last Compiled

# %s

# """ % today.strftime("%c"))

#     return {'actions':['echo "last compiled"']}



def task_md_html_individual():
    import os

    for name in files:
        base,ext=os.path.splitext(name)
        mdfile="chapters/%s" % name
        fix_mdfile(mdfile)

        htmlfile='build/%s.html' % base

        s= 'pandoc  -M date="`date`" --filter eqn2png.py --filter pandoc-citeproc  --filter replace_metavars.py -s --toc --toc-depth=2 --top-level-division=chapter --self-contained -o "%s" "%s" config/config_6x9.yaml' % (htmlfile,mdfile)
    
        yield {
            'name':base,
            'file_dep': [mdfile,'config/config_6x9.yaml'],
            'targets': [htmlfile],
            'actions': [s],
#            'task_dep':['last_compile'],
            'clean':True,
        }

def task_md_html():
    import os

    fnames=[]
    for name in files:
        base,ext=os.path.splitext(name)
        mdfile="chapters/%s" % name
        fix_mdfile(mdfile)

        fnames.append(mdfile)


    s= 'pandoc  -M date="`date`" --filter eqn2png.py --filter pandoc-citeproc  --filter replace_metavars.py -s --toc --toc-depth=2 --top-level-division=chapter --self-contained -o build/measure_of_faith.html %s config/config_6x9.yaml' % (' '.join(q(fnames)))
    
    
    return {
        'file_dep': fnames,
        'targets': ['build/measure_of_faith.html'],
        'actions': [s],
        #'task_dep':['last_compile'],
        'clean':True,
    }

def task_md_tex():
    import os

    for name in files:
        base,ext=os.path.splitext(name)
        mdfile="chapters/%s" % name
        texfile='build/%s_6x9.tex' % base

        yield {
            'name': base,
            'file_dep': [mdfile,'config/config_6x9.yaml'],
            'targets': [texfile],
            'actions': ['pandoc -M date="`date`" --filter replace_metavars.py --natbib --top-level-division=chapter  -o "%s" "%s"' % (texfile,mdfile)],
            #'task_dep':['last_compile'],
            'clean':True,
        }

def task_tex_tex():
    import os

    fnames=[]
    for name in files:
        base,ext=os.path.splitext(name)
        mdfile="chapters/%s" % name
        texfile='build/%s_6x9.tex' % base

        fnames.append(texfile)

    return {
        'file_dep': fnames+ ['config/config_6x9.yaml','config/config_6x9.latex'],
        'targets': ['build/measure_of_faith_6x9.tex'],
        'actions': ['pandoc -s --template=config/config_6x9.latex -M fontsize=12pt -M documentclass=book --top-level-division=chapter --toc --natbib --bibliography=chapters/main.bib  -o build/measure_of_faith_6x9.tex  --include-before=%s %s' % (q([fnames[0]])[0],' '.join(q(fnames[1:])))],
        'clean':True,
    }



from doit.task import clean_targets    
def task_tex_pdf():
    return {
        'file_dep': ['build/measure_of_faith_6x9.tex',],
        'targets': ['build/measure_of_faith_6x9.pdf'],
        'actions': ['pdflatex -halt-on-error -output-directory build build/measure_of_faith_6x9.tex', 
                    'bibtex "build/measure_of_faith_6x9"',
                    'pdflatex -halt-on-error -output-directory build build/measure_of_faith_6x9.tex', 
                    'pdflatex -halt-on-error -output-directory build build/measure_of_faith_6x9.tex', 
                    'gs -dNOPAUSE -dBATCH -sDEVICE=pdfwrite -dEmbedAllFonts=true -sOutputFile=build/measure_of_faith_6x9_embeded.pdf -f build/measure_of_faith_6x9.pdf',
                    'cp build/measure_of_faith_6x9_embeded.pdf "./A Measure of Faith - Brian Blais 6x9.pdf"'],
        'clean':[clean_targets,'rm -f build/*.log build/*.toc build/*.aux build/*.out build/*.bbl build/*.blg build/*.synctex.gz'],
        'verbosity': 2,
    }

