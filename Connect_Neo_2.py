'''
Created on Dec 27, 2018

@author: afukxs8
'''
from py2neo import Graph
from py2neo.ogm import RelatedTo,Property,Label,GraphObject, RelatedFrom

# connect to authenticated graph database
try:
    sgraph = Graph("bolt://localhost:7687/db/data/",user='neo4j',password="1234")
except:
    print("Couldnot connect to Neo. Please make sure the instance in running")
    exit
 
class Person(GraphObject):
    ___primarykey__ = 'name'
    
    Assoc_ID    =   Property()
    Name        =   Property()
    Desig       =   Property()
    Dob         =   Property()
    Doj         =   Property()
    Loc_City    =   Property()
    Loc_Cntry   =   Property()
    person = Label()
    
    knows = RelatedTo("Tech")
            
class Tech(GraphObject):
    ___primarykey__ = 'name'
    
    Assoc_ID    =   Property()
    Skill_ID    =   Property()
    Skill_Name  =   Property()
    Exp_Level   =   Property()
    tech = Label()
    
    person_knows = RelatedFrom("Person","KNOWS")
    

if __name__ == "__main__":
    
    N = Person()
    N.Name = "Karthik"
    N.Assoc_ID = '210154'
    N.Desig = 'Tech Spec'
    N.Dob = '05-Dec-1983'
    N.Doj = '02-Nov-2009'
    N.Loc_City = 'Charlotte'
    N.Loc_Cntry = 'USA'
    
#     sgraph.push(N)
#     print(alice.__node__)

    x = Person()
    x.Name = "Kumar"
    x.Assoc_ID = '280344'
    x.Desig = 'Architect'
    x.Dob = '02-Aug-1982'
    x.Doj = '02-Jul-2010'
    x.Loc_City = 'Charlotte'
    x.Loc_Cntry = 'USA'
#     sgraph.push(x)    
    
    t = Tech()
    t.Assoc_ID = '210154'
    t.Skill_ID = '1'
    t.Skill_Name = 'Mainframes'
    t.Exp_Level = 8
    N.knows.add(t)
#     sgraph.push(t) 
    
    t = Tech()
    t.Assoc_ID = '280344'
    t.Skill_ID = '1'
    t.Skill_Name = 'Python'
    t.Exp_Level = 9
    x.knows.add(t)

    sgraph.push(N)
    sgraph.push(x)
 
    txt = Person.match(sgraph).where("_.name =~ 'K.*'") 
    
    for z in txt:
        print(z)
        print(z.Assoc_ID)
