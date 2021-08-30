fname='chapters/Chapter 02 - Probability.md'
with open(fname) as fid:
    text=fid.read()

text=text.replace('\u200b','')

for line in text.split('\n'):
    if line.startswith('The following are our intuitions'):
        print(line)
        break

with open(fname,'w') as fid:
    fid.write(text)
