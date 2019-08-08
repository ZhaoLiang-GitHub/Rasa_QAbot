#!/usr/bin/env python

#SENIVERSE_KEY=hjne3bys5ilki7yw python ./webchat.py
import os
import pypher
import json
import warnings
import ruamel.yaml as yaml
from pypher.builder import Param, Pypher
from neo4j.v1 import GraphDatabase
from rasa_core.interpreter import RasaNLUInterpreter
import sys 
import argparse

interpret = RasaNLUInterpreter('./models/nlu/longbi')
extracted_intents = None
extracted_values = None # entities values
prediction = None
#a = input("input:")
a_list=['过度依赖父母怎么办','总咬指甲会怎么样','为什么爱说谎']
# ,'过度胆小怎么办','害怕分离怎么办','孩子经常夹腿怎么办','5岁了还尿床怎么办','多动不专心怎么办','不自主的挤眉弄眼怎么办','走路说话晚怎么办','不看人不理人怎么办','孩子易冲动、爱攻击别人怎么办','家长如何帮助孩子对应压力','家长如何帮助孩子理解和表达自己的感受'
#a_list=['孩子总是不理人是怎么样的']
#a=a_list[11]
#a='孩子总是压力大怎么办'
for a in a_list:

	extracted_entities = None
	extracted_intents = None

	prediction = interpret.parse(a)
	print(a,':',prediction['intent'])
	if len(prediction.get("entities")) > 0:
	    # extracted_entities = None
	    extracted_entities = prediction.get("entities")[0]['entity']
	    #extracted_values = prediction.get("entities")[0]['value']
	    extracted_values = ''.join(prediction.get("entities")[0]['value'].split())

	if len(prediction.get("entities")) > 1:
	    print('sss')
	    extracted_entities = dict()
	    extracted_entities = \
		{prediction.get("entities")[entity]['entity']: prediction.get("entities")[entity]['value'] 
			for entity in range(len(prediction.get("entities")))}

	print(extracted_entities, extracted_values )
