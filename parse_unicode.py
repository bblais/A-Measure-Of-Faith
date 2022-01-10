from glob import glob
fnames=glob("chapters/*.md")

omit=['Misc thoughts and to-dos.md','chapters/Scratch.md']


for fname in fnames:
    flag=False
    for name in omit:
        if name in fname:
            flag=True
            break
    if flag:
        continue


    with open(fname) as fid:
        lines=fid.readlines()

    first_time=False
    for i,line in enumerate(lines):
        if any([ord(x)>127 for x in line]):
            S=f"{fname} [Line {i}]: "
            for x in line:
                if ord(x)<=127:
                    S+=x
                else:
                    S+=" 🥶%d🥶 " % ord(x)
            print(S)

