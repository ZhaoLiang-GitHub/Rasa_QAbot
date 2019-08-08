
# -*- coding: UTF-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import argparse
import logging
import warnings

from rasa_core.actions import Action
from rasa_core.agent import Agent
from rasa_core.channels.console import ConsoleInputChannel
from rasa_core.events import SlotSet
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy

from rasa_core.events import AllSlotsReset, Restarted
interpret1 = RasaNLUInterpreter('../fine_grained/models/nlu/longbi')



import search

import warnings
warnings.filterwarnings("ignore")

logger = logging.getLogger(__name__)

#from cocoNLP.extractor import extractor


class Performance(Action):
    def name(self):

        return 'action_query_Performance'

    def run(self, dispatcher, tracker, domain):
        
        

        a=tracker.latest_message.text
        print('bb',tracker.latest_message)

        prediction2 = interpret1.parse(a)
        print('cc',prediction2)
        print('s',tracker.current_slot_values())

        if len(prediction2.get("entities")) :
            print('2')
            intent = prediction2.get("entities")[0]['entity']
        else:
            print('1')
            intent = tracker.get_slot("question")
        print(intent)

        result = search.QurryAttribute(intent,'performance')
        result = str(result).split(':')[1][2:-2]
        dispatcher.utter_message("{}".format(result))

        if (prediction2.get("entities")):
            return[SlotSet('question', prediction2.get("entities")[0]['entity'])]

class Reasons(Action):
    def name(self):

        return 'action_query_Reasons'
    def run(self, dispatcher, tracker, domain):
        a=tracker.latest_message.text

        print('bb',tracker.latest_message)
        prediction2 = interpret1.parse(a)
        print('cc',prediction2)
        print('s',tracker.current_slot_values())
        if len(prediction2.get("entities")) :
            print('2')
            intent = prediction2.get("entities")[0]['entity']
        else:
            print('1')
            intent = tracker.get_slot("question")
        print(intent)
        result = search.QurryAttribute(intent,'reasons')
        result = str(result).split(':')[1][2:-2]
        dispatcher.utter_message("{}".format(result))

        if (prediction2.get("entities")):
            return[SlotSet('question', prediction2.get("entities")[0]['entity'])]
        else:
            return[]

class Solution(Action):
    def name(self):
        return 'action_query_Solution'

    def run(self, dispatcher, tracker, domain):
        
        a=tracker.latest_message.text
        print('bb',tracker.latest_message)

        prediction2 = interpret1.parse(a)
        print('cc',prediction2)
        print('s',tracker.current_slot_values())
        if len(prediction2.get("entities")) :
            print('2')
            intent = prediction2.get("entities")[0]['entity']
        else:
            print('1')
            intent = tracker.get_slot("question")
        print(intent)

        result = search.QurryAttribute(intent,'solution')
        result = str(result).split(':')[1][2:-2]
        dispatcher.utter_message("{}".format(result))

        if (prediction2.get("entities")):
            return[SlotSet('question', prediction2.get("entities")[0]['entity'])]
        else:
            return[]

class Introduction(Action):

    def name(self):

        return 'action_query_Introduction'

    def run(self, dispatcher, tracker, domain):
        
        a=tracker.latest_message.text
        print('bb',tracker.latest_message)

        prediction2 = interpret1.parse(a)
        print('cc',prediction2)
        print('s',tracker.current_slot_values())
        
        if len(prediction2.get("entities")) :
            print('2')
            intent = prediction2.get("entities")[0]['entity']
        else:
            print('1')
            intent = tracker.get_slot("question")
        print(intent)

        result = search.QurryAttribute(intent,'introduction')
        result = str(result).split(':')[1][2:-2]
        dispatcher.utter_message("{}".format(result))

        if (prediction2.get("entities")):
            return[SlotSet('question', prediction2.get("entities")[0]['entity'])]
        else:
            return[]


