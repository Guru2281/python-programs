def get_res(branch,**sub):
    total=0
    for k,v in sub.items():
        if branch=='CSE' and k in ['C','java']:
            total+=v
    return total

sub={"C":20,"java":10,"math":30}
total= get_res("CSE",C=20,java=10,math=30)
print(total)
