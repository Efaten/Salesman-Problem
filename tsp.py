import math
from itertools import permutations
from random import randint, random, seed, shuffle
from tkinter import Tk, Canvas, Button


CANVAS_W, CANVAS_H = 800, 800
NODE_R = CANVAS_H * 0.005


class GUI:
    def __init__(self, root):
        self.canvas = Canvas(root, width=CANVAS_W, height=CANVAS_H, bg="white")
        self.canvas.pack()
        self.nodes = None

    def draw(self):
        self.canvas.delete("all")
        for i in range(len(self.nodes)):
            x1, y1 = self.nodes[i]
            x2, y2 = self.nodes[(i + 1) % len(self.nodes)]
            self.canvas.create_line(x1, y1, x2, y2)
            r = NODE_R
            self.canvas.create_oval(x1 - r, y1 - r, x1 + r, y1 + r, fill="red")


def make_random_graph(size):
    nodes = []
    for i in range(size):
        nodes.append((
            randint(NODE_R, CANVAS_W - NODE_R),
            randint(NODE_R, CANVAS_H - NODE_R)
        ))
    return nodes


def distance(n1, n2):
    x1, y1 = n1
    x2, y2 = n2
    dx = x1 - x2
    dy = y1 - y2
    return math.sqrt(dx * dx + dy * dy)


def cost(s):
    tour = distance(s[-1], s[0])
    for i in range(len(s) - 1):
        tour += distance(s[i], s[i + 1])
    return tour


def random_transform(s):
    s = s[:]
    shuffle(s)
    return s


def swap_transform(s):
    s = s[:]
    temp1 = randint(0, len(s)-1)
    temp2 = randint(0, len(s)-1)
    s[temp1], s[temp2] = s[temp2], s[temp1]
    return s


def rot_transform(s):
    # TODO
    pass


def random_search(s, steps):
    best = s
    print(cost(s))
    ss = s.copy()
    for step in steps:
        ss = random_transform(ss)
        if cost(ss) < cost(best):
            best = ss
    print(cost(best))
    return best 


def local_search(s, steps):
    # TODO
    pass


def P(delta, T):
    temp = math.exp((-1*delta)/T)
    if random() < temp:
        return True
    return False



def anneal(s, steps):
    T = 100
    alpha = 0.95
    delta = 0
    while T > 0.1:
        next_s = swap_transform(s)
        T *= alpha
        delta = cost(next_s) - cost(s)
        if delta < 0:
            s = next_s
        else:
            if P(delta, T):
                s = next_s
    return s


seed(42)
g = make_random_graph(10)
print(cost(g))
# g = anneal(g, None)
g = random_search(g, range(100000))
print(cost(g))
root = Tk()
w = GUI(root)
w.nodes = g
w.draw()
root.mainloop()
