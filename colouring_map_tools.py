# -*- coding: utf-8 -*-
"""
Created on Fri May 15 23:41:19 2020

@author: Shouzeb
"""
from operator import itemgetter
import operator
# return index of city or cities with max neighbours.
def find_max_neighbors(graph):
    index_len_neighbors=[(index,len(n[1])) for index, n in enumerate(graph.items()) if n[0][1] is False]
    max_neighbors=max(index_len_neighbors, key=itemgetter(1))[1]
    max_index_len_neighbors=[x[0] for x in index_len_neighbors if x[1] == max_neighbors]
    cities=[list(graph)[index][0] for index in max_index_len_neighbors]
    print(cities)
    
    return cities


def mrv(graph,colors):
    cities_without_color = [(city[0]) for city, colored in graph.items() if city[1] is False]
    allowed_color_each_city={}
    print(cities_without_color)
    for city in cities_without_color:
        print("hi")
        allowed_color_each_city[city]=get_allowed_colors(graph,city,colors)
    print(allowed_color_each_city.items())
    min_available_color_len=min([len(allowed_color) for city, allowed_color in allowed_color_each_city.items()])
    cities=[city for city, colors in allowed_color_each_city.items() if len(colors) is min_available_color_len]
                       
    return cities

def get_allowed_colors(graph,city,colors):
    not_allowed_colors=[city[1] for city in graph[(city, False)] if city[1] is not '']
    print("hi ",not_allowed_colors)
    allowed_colors=diff(colors,not_allowed_colors)
    return allowed_colors

def diff(colors,not_allowed_colors):
    difference=[i for i in colors+not_allowed_colors if i not in colors or i not in not_allowed_colors]
    return difference

def lcv(graph,colors):
    color_number = {}
    city_color = []
    for neighbours in graph.values():
        [city_color.append(c) for c in neighbours if c[1] != '']
    
    all_used_colors_dict=list(dict.fromkeys(city_color))
    
    if not all_used_colors_dict:
        return colors
    
    for cc in all_used_colors_dict:
        if cc[1] not in color_number:
            color_number[cc[1]] = 1
        else:
            color_number[cc[1]] += 1
    
    number_of_max_color_used=max(color_number.items(),key=operator.itemgetter(1))[1]
    colors=[key for key, value in color_number.items() if value is number_of_max_color_used]
    return colors

def coloring(graph,city,color):
    neighbours=graph[(city,False)]
    del graph[(city,False)]
    graph[(city,True)]=neighbours
    for neighbours_list in graph.values():
        for n in neighbours_list:
            if n[0] == city:
                l=list(n)
                l[1]=color
                t=tuple(l)
                neighbours_list.remove(n)
                neighbours_list.append(t)
                
            
        
