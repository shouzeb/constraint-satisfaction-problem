# -*- coding: utf-8 -*-
"""
Created on Fri May 15 23:13:19 2020

@author: Shouzeb
"""
import sys
from graph_building import graph_building
from colouring_map_tools import *

graph=graph_building()
#print(graph)
colors=['RED','BLUE','GREEN']
solution={}
for m in range(len(graph)):
    cities_with_max_neighbors=find_max_neighbors(graph)
    cities_with_min_remaining_colors=mrv(graph,colors)
    more_used_colors=lcv(graph,colors)
    selected_city=set(cities_with_max_neighbors).intersection(set(cities_with_min_remaining_colors)).pop()
    colors_for_selected_city=get_allowed_colors(graph, selected_city, colors)
    final_color=set(more_used_colors).intersection(colors_for_selected_city)
    try:
        if final_color:
            color=final_color.pop()
        else:
            color=colors_for_selected_city.pop()
        coloring(graph,selected_city,color)
        solution[selected_city]=color
    except IndexError:
        sys.exit("Something went wrong. Perhaps there is not enough color for this map")
print("Solution of minimun remaining values: ",solution)
   
#print(graph.items())