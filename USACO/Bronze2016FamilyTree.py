###
# this is a tree problem
# i created 2 dictionaries that act as a graph, one going immediatly up (parent) and one going down (child)
# rest was just logic as a certain combination of ups and downs result in specific results (eg. up-up is grandmother and up-down is sibling)
###
import sys
'''
sys.stdin = open("family.in", "r")
sys.stdout = open("family.out", "w")
# uncomment for submission
'''
N, start, target = map(str, input().split())
familyup = {}

familydown = {}
for _ in range(int(N)):
    X, Y = map(str, input().split())
    
    familyup[Y] = X

    if X not in familydown:
        familydown[X] = [Y]
    else:
        familydown[X].append(Y)


great = 0
curr = start
r = 0
cousin = False
did = False
while curr in familyup:
    if familyup[curr] == target:
        did = True
        break
    elif target in familydown[familyup[curr]]:
        did = True
        r = 1
        break
    else:
        q = familydown[familyup[curr]].copy()
        while len(q)!=0:
            newq = []
            for x in q:
                if x not in familydown:
                    continue
                if target in familydown[x]:
                    did = True
                    cousin = True
                    break
                else:
                    for i in familydown[x]:
                        newq.append(i)
            q = newq.copy()

        if cousin:
            break
        
    
    
    curr = familyup[curr]
    great+=1

c = 0
if did:
    if cousin:
        c+=1
    elif great == 0 and r == 0:
        print(target+ " is the mother of "+ start)
    elif great == 0 and r == 1:
        print("SIBLINGS")
    elif great == 1 and r == 1:
        print(target+ " is the aunt of "+ start)
    elif great == 1 and r == 0:
        print(target+ " is the grand-mother of "+ start)

    elif r == 1:
        print(target+ " is the "+"great-"*(great-1)+"aunt of "+ start)

    elif r == 0:
        print(target+ " is the "+"great-"*(great-1)+"grand-mother of "+ start)

if c==1 or not did:
    temp = start
    start = target
    target = temp
    great = 0
    curr = start
    
    r = 0
    cousin = False
    did = False
    while curr in familyup:
        if familyup[curr] == target:
            did = True
            break
        elif target in familydown[familyup[curr]]:
            did = True
            r = 1
            break
        else:
            q = familydown[familyup[curr]].copy()
            while len(q)!=0:
                newq = []
                for x in q:
                    if x not in familydown:
                        continue
                    if target in familydown[x]:
                        did = True
                        cousin = True
                        break
                    else:
                        for i in familydown[x]:
                            newq.append(i)
                q = newq.copy()

            if cousin:
                break
            
        
        
        curr = familyup[curr]
        great+=1
    if not did:
        print("NOT RELATED")
    else:
        if cousin and c == 1:
            
            print("COUSINS")
        elif great == 0 and r == 0:
            print(target+ " is the mother of "+ start)
        elif great == 0 and r == 1:
            print("SIBLINGS")
        elif great == 1 and r == 1:
            print(target+ " is the aunt of "+ start)
        elif great == 1 and r == 0:
            print(target+ " is the grand-mother of "+ start)

        elif r == 1:
            print(target+ " is the "+"great-"*(great-1)+"aunt of "+ start)

        elif r == 0:
            print(target+ " is the "+"great-"*(great-1)+"grand-mother of "+ start)
