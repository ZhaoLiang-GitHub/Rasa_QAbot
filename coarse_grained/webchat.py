#!/usr/bin/env python

#SENIVERSE_KEY=hjne3bys5ilki7yw python ./webchat.py
import os

from rasa_addons.webchat import WebChatInput, SocketInputChannel
from rasa_core.agent import Agent

#current_path = os.path.dirname(os.path.realpath(__file__))


current_path = os.getcwd()
agent = Agent.load("models/dialogue","models/nlu/longbi")
input_channel = WebChatInput(static_assets_path=os.path.join(current_path, 'static'),index='mychat.html')
agent.handle_channel(SocketInputChannel(5500, "/", input_channel))


