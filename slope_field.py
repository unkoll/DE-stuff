#!/usr/bin/python
# -*- coding: UTF-8 -*-

import numpy as np

def f(t,x):
    if x == t:
        return 1
    if x == 0:
        return np.inf
    return 1.5 * t / x;

min_x = -4
max_x = 4
min_y = -4
max_y = 4

letter_x = "t"
letter_y = "x"

len_line = 0.4

template_begin = """
\\begin{{tikzpicture}}[scale=1.5]
    \draw[step=0.5cm,gray,very thin] ({},{}) grid ({},{});
""".format(min_x + 0.1, min_y + 0.1, max_x - 0.1, max_y - 0.1)

template_end = """
\end{tikzpicture}
"""

def draw_axis():
    ox = "\t\draw[below, thick, ->]\n"
    #ox += "({},{}) node {{${}$}} -- ".format(-plot_len, 0, " ")
    for x in range(min_x, max_x):
        if x != 0:
            ox += "({},{}) node {{${}$}} -- ".format(x, 0, x)
    ox += "({},{}) node {{${}$}};\n".format(max_x, 0, letter_x)

    oy = "\t\draw[right, thick, ->]\n"
    #oy += "({},{}) node {{${}$}} -- ".format(0, -plot_len, " ")
    for y in range(min_y, max_y):
        if y != 0:
            oy += "({},{}) node {{${}$}} -- ".format(0, y, y)
    oy += "({},{}) node {{${}$}};\n".format(0, max_y, letter_y)

    if min_x * max_x <= 0 or min_y * max_y <= 0:
        oy += "\draw[below right] ({},{}) node {{$0$}};\n".format(0,0)
    return ox + oy

def draw_line(x,y):
    coeff = f(x,y)
    if (np.isnan(coeff)):
        return ""   # Not defined, can't draw
    line = "\t\draw[red]"
    line_start = (0,0)
    line_finish = (0,0)
    if np.isinf(coeff):
        line_start = (x, y - len_line/2)
        line_finish = (x, y + len_line/2)
    else:
        dx = np.sqrt(len_line**2/(1 + coeff**2))
        line_start = (x - dx/2, y - coeff * dx/2)
        line_finish = (x + dx/2, y + coeff * dx/2)
    line += """
        {} node {{$ $}} -- {} node {{$ $}};
    """.format(line_start, line_finish)
    return line

def draw_slope_field():
    result = ""
    for x in range(2*min_x + 1, 2*max_y+1):
        for y in range(2*min_y + 1, 2*max_y + 1):
            result += draw_line(x/2,y/2)
    return result

if __name__ == '__main__':
    result = template_begin
    result += draw_axis()
    result += draw_slope_field()
    result += template_end
    print(result)
