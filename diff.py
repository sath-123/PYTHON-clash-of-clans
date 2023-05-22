import difflib
from subprocess import run
import argparse
from sys import exit
from os.path import isfile, exists
from os import mkdir

# For 4.in and 4.out is files given by us, 4_rahul.out is your ouput for 4.in file
# Example run = python3 diff.py -i 4.in -a 4.out -o 4_rahul.out -s 10 -p yes 


parser = argparse.ArgumentParser(description="Grade Two Files")
parser.add_argument('-i', '--input', dest='input',
                    default=[None], nargs=1,
                    help='input file name')
parser.add_argument('-a', '--answer', dest='answer',
                    default=[None], nargs=1,
                    help='answer file name')
parser.add_argument('-o', '--output', dest='output',
                    default=[None], nargs=1,
                    help='Output file name')
parser.add_argument('-s', '--score', dest='score',
                    default=[None], nargs=1,
                    help='Score')
parser.add_argument('-p', '--partial', dest='partial',
                    default=['yes'], nargs=1,
                    help='Partial score')

args = parser.parse_args()
input = args.input[0]
answer = args.answer[0]
output = args.output[0]
total = int(args.score[0])
partial = args.partial[0]

def bst_score(tree,root,depth):
    if tree[root][0] == -1 and tree[root][1] == -1:
        # print(root)
        tree[root][2] = root
        tree[root][3] = root
        return tree[root][4]*depth,True
    elif tree[root][0] == -1:
        sub_score,isTree= bst_score(tree,tree[root][1],depth+1)
        if tree[tree[root][1]][3] <= root:
            isTree = False
        tree[root][2] = max(tree[tree[root][1]][2],root)
        tree[root][3] = min(tree[tree[root][1]][3],root)
        return tree[root][4]*depth + sub_score,isTree
    elif tree[root][1] == -1:
        sub_score,isTree= bst_score(tree,tree[root][0],depth+1)
        if tree[tree[root][0]][2] >= root:
            isTree = False
        tree[root][2] = max(tree[tree[root][0]][2],root)
        tree[root][3] = min(tree[tree[root][0]][3],root)
        return tree[root][4]*depth + sub_score,isTree
    else:
        left_score,isTree_l= bst_score(tree,tree[root][0],depth+1)
        right_score,isTree_r = bst_score(tree,tree[root][1],depth+1)
        isTree = isTree_l and isTree_r
        if tree[tree[root][0]][2] >= root or tree[tree[root][1]][3] <= root:
            isTree = False
        tree[root][2] = max(tree[tree[root][0]][2],tree[tree[root][1]][2],root)
        tree[root][3] = min(tree[tree[root][0]][3],tree[tree[root][1]][3],root)
        return tree[root][4]*depth + left_score + right_score,isTree
        
        

lines = 0
match = 0
file1 = open(answer,'r')
content1 = file1.readlines()
file2 = open(output,'r')
content2 = file2.readlines()
if content1[0].strip() == content2[0].strip():
    match = 1
    file3 = open(input,'r')
    content3 = file3.readlines()
    bst = True
    n = int(content3[0].strip())
    tree = []
    for i in range(0,n+1):
        temp = []
        for j in range(0,5):
            temp.append(-1)
        tree.append(temp)
    for i in range(1,n+1):
        index,freq = content3[i].strip().split()
        index = int(index)
        freq = int(freq)
        tree[index][4] = freq
    parent = content2[1].strip().split()
    for i in range(0,n):
        parent[i] = int(parent[i])
    for i in range(0,n):
        if parent[i] == 0:
            root = i+1
            continue
        
        if i+1 < parent[i]:
            if tree[parent[i]][0] == -1:
                tree[parent[i]][0] = i+1
            else:
                bst = False
                break
        elif i+1 > parent[i]:
            if tree[parent[i]][1] == -1:
                tree[parent[i]][1] = i+1
            else:
                bst = False
                break
        else:
            bst = False
            break
    if bst:
        ans_score,isTree = bst_score(tree,root,1)
        if isTree:
            if ans_score == int(content1[0].strip()):
                match = 2

    if partial == 'yes':
        score = (match*total)/2
    else:
        if match == 2:
            score = total
        else:
            score = 0.0
    print(score)
else:
    print("0.0")
    