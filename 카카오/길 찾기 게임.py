import sys
sys.setrecursionlimit(10**6) #재귀깊이를 늘려주기 위한 목적

def preorder(arrY, arrX, answer):
    node = arrY[0] # root node 찾음
    idx = arrX.index(node) # root가 좌측으로 몇번째에 있는지
    arrY1 = []
    arrY2 = []

    for i in range(1, len(arrY)):
        if node[0] > arrY[i][0]: # root 왼쪽에 있으면
            arrY1.append(arrY[i])
        else: # root보다 높으면
            arrY2.append(arrY[i])
    
    answer.append(node[2])
    if len(arrY1) > 0:
        preorder(arrY1, arrX[:idx], answer) #node 명명하기 위한 목적.
    if len(arrY2) > 0:
        preorder(arrY2, arrX[idx + 1:], answer) #좌우로 나누는 역할
    return

def postorder(arrY, arrX, answer):
    node = arrY[0]
    idx = arrX.index(node)
    arrY1 = []
    arrY2 = []

    for i in range(1, len(arrY)):
        if node[0] > arrY[i][0]:
            arrY1.append(arrY[i])
        else:
            arrY2.append(arrY[i])
    
    if len(arrY1) > 0:
        postorder(arrY1, arrX[:idx], answer)
    if len(arrY2) > 0:
        postorder(arrY2, arrX[idx + 1:], answer)
    answer.append(node[2])
    return

def solution(nodeinfo):
    # 전위순회, 후위순회할 값을 담을 배열들
    preanswer = [] 
    postanswer = []

    # 이차원 배열 좌표안에 노드번호 작성(방문해아할 순서라기보다는 번호)
    for i in range(len(nodeinfo)):
        nodeinfo[i].append(i+1)

    arrY = sorted(nodeinfo, key = lambda x : (-x[1], x[0])) # 맨 위부터 아래까지
    arrX = sorted(nodeinfo) # 왼쪽부터 오른쪽까지

    preorder(arrY, arrX, preanswer) # preanswer append할 배열
    postorder(arrY, arrX, postanswer) # postanswer append할 배열

    return [preanswer, postanswer]