#!/usr/bin/env bash

python -m rasa_core.train -s data/stories.md -d data/domain.yml -o models/dialogue --epochs 200
