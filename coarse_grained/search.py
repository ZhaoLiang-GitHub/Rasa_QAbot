#!/usr/bin/env python

#SENIVERSE_KEY=hjne3bys5ilki7yw python ./webchat.py
import pypher
from pypher.builder import Param, Pypher
from neo4j.v1 import GraphDatabase
import os

def QurryAttribute(intent,gold):
	uri = "bolt://localhost:7687"
	driver = GraphDatabase.driver(uri, auth=("neo4j", "SV-yimei"))

	pypherObject = Pypher()
	pypherObject.Match.node('n', 'A').WHERE.n.property('question') ==  intent
	pypherObject.RETURN.n.property(gold)
	print ('search command:',pypherObject)
	params = pypherObject.bound_params

	with driver.session() as session:
	    result = session.run(str(pypherObject), **dict(params))
	    query_result = result.data()
	return query_result[0]

