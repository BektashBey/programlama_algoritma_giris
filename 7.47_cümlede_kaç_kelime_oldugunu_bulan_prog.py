ni=" ,;-:"; s=0 ; c=imput("cümle: ")
for i in range (len(c)):
    if (c[i] in ni):
        s+=1
print("\nCümlede %d tane kelime vardır."%(s+1))
