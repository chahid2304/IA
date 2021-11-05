from queue import Queue
from graphviz import Digraph
import os
import copy
class Node:
    def __init__(self, state, parent, action, depth):
        self.state = state
        self.parent = parent
        self.action = action
        self.depth = depth
        self.id = "".join(str(n) for n in self.state)

    def __repr__(self):
        joined_string = " ".join(str(n) for n in self.state)
        return joined_string[0:5]+"\n"+joined_string[6:11]+"\n"+joined_string[12:17]
def possible_moves(state):
    if(state[0]==0) : 
        return['right','down']
    if(state[1]==0) : 
        return['left','right','down']
    if(state[2]==0) : 
        return['left','down']
    if(state[3]==0) : 
        return['up','right','down']
    if(state[4]==0) : 
        return['left','up','right','down']
    if(state[5]==0) : 
        return['left','up','down']
    if(state[6]==0) : 
        return['up','right']
    if(state[7]==0) : 
        return['left','up','right']
    if(state[8]==0) : 
        return['left','up']
def generate_state(state, m):
    temp = copy.deepcopy(state) 
    for i in range(8):
        if(temp[i]==0) : break
    if(m=='left') :
        t=temp[i]
        temp[i]= temp[i-1]
        temp[i-1] =t
    if(m=='right') : 
        t=temp[i]
        temp[i]= temp[i+1]
        temp[i+1] =t
    if(m=='up') : 
        t=temp[i]
        temp[i]= temp[i-3]
        temp[i-3] =t
    if(m=='down') : 
        t=temp[i]
        temp[i]= temp[i+3]
        temp[i+3] =t
    return temp
    

def create_node(state, parent, action, depth):
    return Node(state, parent, action, depth)

def expand_node(node):
    expanded_nodes = []
    pos_moves = possible_moves(node.state)
    for m in pos_moves :
        expanded_nodes.append(create_node(generate_state(node.state,m),node.id,m,node.depth+1))
    return expanded_nodes

def dfs():
    stack = []
    visited = []
    visited_str = []
    depth_limit = 5
    stack.append(create_node(initial, "283164705", None, 0))
    while len(stack) > 0:
        node = stack.pop(0)
        if node.id in visited_str:
            continue
        else:
            visited.append(node)
            visited_str.append(node.id)
         
        if node.state == goal:
            return visited
        
        if node.depth < depth_limit:
            expanded_nodes = expand_node(node)
            if(expanded_nodes not in visited):
                expanded_nodes.extend(stack)
                stack = expanded_nodes

'''def bfs():
     visited=[]
     queue=[]
     queue.append(create_node(initial, "283164705", None, 0))
     while queue:
         node=queue.pop(0)
         if node.state not in visited :
             visited.append(node.state)
             if node.state == goal:
                   return visited       
             next=expand_node(node)
             for nexts in next :
                 queue.append(nexts)'''
def bfs():
    queue = []
    visited = []
    visited__str = []
    depth__limit = 5
    queue.append(create_node(initial, "283164705", None, 0))
    while(len(queue)>0):
        node = queue.pop()
        if node.id in visited__str:
            continue
        else:
            visited.append(node)
            visited__str.append(node.id)
            if node.state == goal:
                return visited
            if node.depth < depth__limit:
                expanded__nodes = expand_node(node)
                if(expanded__nodes not in visited):
                    expanded__nodes.extend(queue)
                    queue = expanded__nodes
        if(len(queue)==0): return None
            

def display(title, path, file):
    # Start - Graphs init
    graph_dfs = Digraph(comment=title)
    step = 0
    color = "black"
    for node in path:
        node_str = node.__str__()
        if node.state == goal: color = "green"
        graph_dfs.node(str(node.id), node_str, color=color)
        graph_dfs.edge(str(node.parent), str(node.id), str(node.action) + "\n" + str(step))
        step += 1
    # Start - Graphs rendering
    graph_dfs.render(str(os.getcwd() + '/outputs/' + file + '.gv'), view=True)
	# End - Graphs rendering
def cout(node,goal):
    c=0
    for i in range (len(node)):
        if node[i] != goal[i]:
            c=c+1
    return c
'''def bestfirst():
    open=[]
    closed=[]
    open.append(create_node(initial, "283164705", None, 0))
    while len(open)>0:
        n=open.pop(0)
        closed.append(n)
        if n==goal:
            return n
        next=expand_node(n)
        for nexts in next:
            open.append(nexts)
            for i in range (len(open)):
                if cout(open[i],goal)>cout(open[i+1],goal):
                    m=open[i]
                    open[i]=open[i+1]
                    open[i+1]=m'''
def Best_First_Search():
    Open=[]
    Closed=[]
    depth_limit = 800
    visited=[]
    visited_str = []
    Open.append(create_node(initial, "283164705", None, 0))
    while len(Open) > 0:
        m=0
        
        node = Open.pop(0)
        if node.id in visited_str:
            continue
        else:
            visited.append(node)
            visited_str.append(node.id)
        if node.state == goal:
            return visited
        if node.depth < depth_limit:
            expanded_nodes=expand_node(node)
            for node in expanded_nodes:
                if node.id not in visited_str:
                    Open.append(node)
                    for node in Open:
                        list_h=[]
                        h=cout(node.state,goal)
                        if h<m:
                            m=h
                            list_h.append(node)
                            Open=copy.deepcopy(list_h)


 
def plot_graph(x, y, predicted):
    plt.scatter(x, y, c = 'red')
    plt.plot(x, predicted, marker = 'o', color = 'blue')
    plt.show() 
def mean(values):
    return sum(values)/len(values)
def covariance(x, mean_x, y, mean_y):
    c=0
    for i in range (len(x)):
       c+= (x[i]-mean_x)*(y[i]-mean_y)
       return c/(len(x)-1)

def variance(values): 
    s=sum(values)**2-((sum(values)**2)/len(values))
    return s/(len(values)-1)

def coefficients(x, y):
    a=covariance(x,y)/variance(x)
    b=mean(y)-a*mean(x)
    return ()
 

print(mean([1,2,3,4]))

x=[1,2,3,5]
y=[6,7,8,9]
print(variance(x))
print(mean(x))
print(mean(y))
print(covariance(x, mean(x), y, mean(y)))

'''goal = [1, 2, 3, 8, 0, 4, 7, 6, 5]
initial = [2, 8, 3, 1, 6, 4, 7, 0, 5]
#print(possible_moves(initial))
#print(generate_state(initial,"up"))
#print(cout(initial,goal))
print(dfs())
print("hi")
print(bfs())
print("*********************************************")
print(Best_First_Search())
display("DFS graph", dfs(), "dfs")
display("BFS graph", bfs(), "bfs")
display("BFS graph", Best_First_Search(), "best first")'''