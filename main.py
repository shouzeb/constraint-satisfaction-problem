# -*- coding: utf-8 -*-
"""
Created on Tue May 12 08:36:20 2020

@author: Shouzeb
"""
from csp import CSP
from UniversalDict import UniversalDict
from DefaultDict import DefaultDict

class CSP:
    
    def __init__(self, vars, domains, constraints,neighbors):
        #print "initialize the CSP problem" 
        vars=vars
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
    
    def different_values_constraint(A,a,B,b): 
        return a!=b
    
    def update(x, **entries):
        if isinstance(x,dict): 
            x.update(entries)
        else:
            x.__dict__.update(entries)
        return x
    def backtracking(csp):
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
    
    def count_if(fun,seq):
        f=lambda count,x:count +(fun(x)) 
        return reduce(f,seq,0)
    






vars=['a','b','c'] 
domains=[1,2,3] 
neighbors={'a':['b'],'b':['a','c'],'c':['b']}

backtracking(CSP(vars,UniversalDict(domains),different_values_constraint,neighbors))



