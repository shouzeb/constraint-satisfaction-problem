# -*- coding: utf-8 -*-
"""
Created on Mon May 11 15:54:15 2020

@author: Waqas
"""
from functools import reduce 

class CSP:
    def __init__(self, vars, domains, constraints,neighbors):
        #print "initialize the CSP problem"
        vars=vars
        #print(neighbors)
        update(self,vars=vars,domains=domains,constraints=constraints,neighbors=neighbors)
    def assign(self, var, val, assignment):
        #print "assign the val to variable and place in assignment"
        assignment[var]=val
    def unassign(self,var,assignment):
        #print "unassign the var"
        if var in assignment:
            del assignment[var]
    def nconflicts(self, var, val, assignment):
        #print "return number of conflicts"
        def conflict(var2):
            val2=assignment.get(var2,None)
            return val2!=None and not self.constraints(var,val,var2,val2)
        return count_if(conflict,self.neighbors[var])
def count_if(fun,seq):  
    f=lambda count,x:count +(fun(x))
    return reduce(f,seq,0)
def different_values_constraint(A,a,B,b):
    #print(a,b)
    return a!=b
def update(x, **entries):
    #print(entries)
    if isinstance(x,dict):
        x.update(entries)
    else:
        x.__dict__.update(entries)
    return x
def backtracking(csp):
    print(csp)
    update(csp)
    return recursive_backtracking({},csp)
def recursive_backtracking(assignment,csp):
    #print "perform backtracking"
    if len(assignment)==len(csp.vars):
        return assignment
    var = select_unassigned_variable(assignment,csp)
    for val in order_domain_values(var,assignment,csp):
        if csp.nconflicts(var,val,assignment)==0:
            csp.assign(var,val,assignment)
            result=recursive_backtracking(assignment,csp)
            if result is not None:
                return result
            csp.unassign(var,assignment)
    return None
def select_unassigned_variable(assignment,csp):
    #print "return any one unassigned variable"
    for v in csp.vars:
        if v not in assignment:
            return v
def order_domain_values(var,assignment,csp):
    #print "return any value from the domain"
    domain=csp.domains[var][:]
    while domain:
        yield domain.pop()
class UniversalDict:
    def __init__(self,value):
        self.value=value
        print(self.value)
    def __getitem__(self,key):
        return self.value
import copy
class DefaultDict(dict):
    def __init__(self,default):
        self.default=default
    def __getitem__(self,key):
        if key in self:
            return self.get(key)
        return self.setdefault(key,copy.deepcopy(self.default))
    def __copy__(self):
        copy= DefaultDict(self.default)
        copy.update(self)
        return copy
def neighbors_parse(neighbors,vars=[]):
    dict = DefaultDict([])
    for var in vars:
        dict[var]=[]
    specs = [ spec.split(":")  for spec in neighbors.split(";")]
    for (A, Aneighbors) in specs:
        A=A.strip()
        dict.setdefault(A,[])
        for B in Aneighbors.split():
            dict[A].append(B)
            dict[B].append(A)
    return dict

def MapColoringCSP(colors,neighbors):
    if isinstance(neighbors, str):
        neighbors=neighbors_parse(neighbors)
        #print(neighbors)
        return CSP(neighbors.keys(),UniversalDict(colors),different_values_constraint,neighbors)
'''   
#testing
vars=['a','b','c']
domains=[1,2,3]
neighbors={'a':['b'],'b':['a','c'],'c':['b','c']}
print(backtracking(CSP(vars,UniversalDict(domains),different_values_constraint,neighbors)))
'''
#print(neighbors_parse("x: y z; y: z", list("xyz")))
australia=MapColoringCSP(list("RGB"),"SA:WA NT Q NSW V; NT:WA Q; NSW: Q V; T: ") 
print("Solution: ",backtracking(australia))




