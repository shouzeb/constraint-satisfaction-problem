# -*- coding: utf-8 -*-
"""
Created on Fri May 15 23:13:19 2020

@author: Shouzeb
"""
import sys
from graph_building import graph_building
from colouring_map_tools import *
from time import time
#colors
colors=['RED','BLUE','GREEN']


#forward checking
#build graph
print("\t\t\t>>>>>Finding solution by Forward Checking<<<<<")
graph1 = graph_building()
t1=time()
solution={}
selected_city=[]
for m in range(len(graph1)):
    selected_city.append((select_city(graph1,m).pop()))
#print("hi 1",selected_city.pop())
assignment=[]
for m in range(len(graph1)): 
    selected_city1=selected_city.pop()
    #print("hi 2",selected_city1)
    if selected_city1 in assignment:
        continue
    else:
        try:
            colors_of_selected_city = get_allowed_colors(graph1, selected_city1, colors)
            #print(colors_of_selected_city)
            color=colors_of_selected_city.pop()
            coloring(graph1, selected_city1, color)
            assignment.append(selected_city1)
            solution[selected_city1]=color
        except:
            sys.exit("Something went wrong. Perhaps there is not enough color for this map")
t_final=time()-t1
print("Solution of Forward Checking is: ",solution)
print("Time: ",t_final)
print("\n \n")



#Minimun Remaining Values
print("\t\t\t>>>>>Finding solution by Minimun Remaining Values<<<<<")
# Build graph
graph=graph_building()
#print(graph)
t1=time()
solution={}
for m in range(len(graph)):
    cities_with_max_neighbors=find_max_neighbors(graph)
    #print(cities_with_max_neighbors)
    cities_with_min_remaining_colors=mrv(graph,colors)
    #rprint(cities_with_min_remaining_colors)
    more_used_colors=lcv(graph,colors)
    selected_city=set(cities_with_max_neighbors).intersection(set(cities_with_min_remaining_colors)).pop()
    # Get allowed color for selected city
    colors_for_selected_city=get_allowed_colors(graph, selected_city, colors)
    #final color for city
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
t_final=time()-t1
print("Solution of Minimun Remaining Values is: ",solution)
print("Time: ",t_final)
print("\n \n")   
#print(graph.items())
#print(graph.values())