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

for name in files:

    fname='chapters/%s' % name
    print(fname)

    with open(fname) as fid:
        text=fid.read()

    newlines=[]
    for line in text.split('\n'):
        newline=line
        if '<img ' in line:
            print(line)
            imgfname=line.split('"')[1].split('"')[0]
            if 'width=' in line:
                width=line.split('width=')[1].split('>')[0]
            else:
                width=None

            newline="![](%s)" % imgfname
            if width:
                newline+=" {width=%s}" % width
            print (newline)
            print()
        newlines.append(newline)


    newtext='\n'.join(newlines)

    if newtext!=text:
        print("text changed")  
        with open(fname,'w') as fid:
            fid.write(newtext)
    else:
        print("text unchanged")

