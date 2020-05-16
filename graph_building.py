# -*- coding: utf-8 -*-
"""
Created on Fri May 08 23:00:01 2020

@author: Shouzeb
"""

def graph_building():
    #here key:(X, BOOL). X is city and bool is for coloured or uncoloured
    #
    graph={}
    country=['SA:[WA,NT,Q,NSW,V]', 'NT:[WA,Q,SA]', 'NSW:[Q,V,SA]', 'WA:[NT,SA]', 'Q:[NT,SA,NSW]', 'V:[SA,NSW]', 'T:[]']
    for city_neighbor in country:
        city, neighbors=city_neighbor.split(":")
        neighbors=neighbors.replace("[","").replace("]","").replace("\n","").split(",")
        neighbors=[(neighbor,'') for neighbor in neighbors if neighbor != '']
        '''for neighbor in neighbors:
            if neighbor != '':
                neighbors.append(tuple((neighbor,'')))'''
        graph[(city, False)]=neighbors
    return graph

