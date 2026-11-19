#!/usr/bin/env python3
"""Evaluator-only exact checks. Standard library; no external services."""
import json
from collections import deque
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path

def boundary(cells):
    return sum((x+dx,y+dy) not in cells for x,y in cells for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)))

def distances(edges):
    d={(1,2,3,4):0}; q=deque(d)
    while q:
        s=q.popleft()
        for i,j in edges:
            t=list(s); t[i],t[j]=t[j],t[i]; t=tuple(t)
            if t not in d: d[t]=d[s]+1; q.append(t)
    return d

def graphs():
    pairs=list(combinations(range(4),2))
    readings={(2,1,3,4):1,(1,3,2,4):1,(1,2,4,3):1,(3,2,1,4):3,(1,4,3,2):3,(4,2,3,1):5}
    matches=[]
    for bits in product((0,1),repeat=6):
        edges=[p for p,b in zip(pairs,bits) if b]; d=distances(edges)
        if all(d.get(s)==v for s,v in readings.items()):
            matches.append({'edges':[[i+1,j+1] for i,j in edges],'target_distance':d[(3,4,1,2)]})
    return matches

def grid_paths():
    cells={(r,c) for r in range(1,4) for c in range(1,5)}
    def walk(p,seen):
        if p==(3,3): return int(len(seen)==12)
        r,c=p
        return sum(walk(n,seen|{n}) for n in ((r+1,c),(r-1,c),(r,c+1),(r,c-1)) if n in cells and n not in seen)
    return walk((1,1),{(1,1)})

def repairs():
    rows=[[2,7,6,1],[4,None,6,9],[8,3,4,8],[6,9,4,1]]; choices=[]
    for row in rows:
        options=[]
        for a,b in product(range(10),repeat=2):
            valid=[a,b,(a+2*b)%10,(2*a+b)%10]
            errors=sum(x is not None and x!=y for x,y in zip(row,valid))
            if errors<=1: options.append((valid,errors))
        choices.append(options)
    return [[x[0] for x in result] for result in product(*choices) if sum(x[1] for x in result)==1]

def compute():
    segments={'0':'abcdef','1':'bc','2':'abdeg','3':'abcdg','4':'bcfg','5':'acdfg','6':'acdefg','7':'abc','8':'abcdefg','9':'abcdfg'}
    flips=[len(set(segments[a])^set(segments[b])) for a,b in zip('23','59')]
    codes=[f'{a}{b}{c}' for a,b,c in product(range(1,7),repeat=3) if a+b==5 and b+c==7 and b%2==0]
    count=sum(any(len(set(bits[i:i+4]))==1 for i in range(9)) for bits in product((0,1),repeat=12))
    partitions=[]
    for left in combinations(range(2,8),3):
        right=tuple(sorted(set(range(2,8))-set(left)))
        if left<right and abs(sum(left)-sum(right))==1: partitions.append([list(left),list(right)])
    return {
      'Q01':{'proposed_mechanism':'total exposed unit side length','conditional_answer':boundary({(0,0),(1,0),(2,0),(0,1),(2,1),(0,2)}),'shared_sides':5,'unrestricted_rule_unique':False},
      'Q02':{'proposed_mechanism':'Hamming distance of fixed-position segment states','conditional_answer':sum(flips),'per_position':flips,'unrestricted_rule_unique':False},
      'Q03':{'symmetry':'reflection across vertical midline','dot':[0.8,0.35],'rotation_suffices':False},
      'Q04':{'compatible_graphs':graphs(),'shortest_witness':['3412','3142','1342','1324','1234']},
      'Q05':{'codes':codes,'unique':False},
      'Q06':{'exists':False,'enumerated_paths':grid_paths(),'proof':'12 cells require opposite-color endpoints; specified endpoints have the same checkerboard color.'},
      'Q07':{'repairs':repairs()},
      'Q08':{'favorable':count,'total':4096,'probability':str(Fraction(count,4096))},
      'Q09':{'optimal_first':['A','B','C'],'worst_case_queries':3,'D_worst_case':4,'no_oracle_reply_received':True},
      'Q10':{'x':7},
      'Q11':{'box':'A','truth_values':[False,True,False]},
      'Q12':{'minimum_difference':1,'optimal_partitions':partitions}
    }

if __name__=='__main__':
    result=compute()
    assert result['Q01']['conditional_answer']==14
    assert result['Q02']['conditional_answer']==5
    assert result['Q04']['compatible_graphs']==[{'edges':[[1,2],[2,3],[3,4]],'target_distance':4}]
    assert result['Q05']['codes']==['143','325']
    assert result['Q06']['enumerated_paths']==0
    assert result['Q07']['repairs']==[[[2,7,6,1],[4,1,6,9],[8,3,4,9],[6,9,4,1]]]
    path=result['Q04']['shortest_witness']
    for a,b in zip(path,path[1:]):
        changed=[i for i,(x,y) in enumerate(zip(a,b)) if x!=y]
        assert len(changed)==2 and changed[1]-changed[0]==1
        i,j=changed
        assert a[i]==b[j] and a[j]==b[i]
    assert len(path)-1==4
    out=Path(__file__).with_name('gold.json')
    out.write_text(json.dumps(result,indent=2)+'\n')
    print('All exact checks passed. Gold saved to evaluation/private/gold.json.')
    print('Q08 exact count:', result['Q08'])
