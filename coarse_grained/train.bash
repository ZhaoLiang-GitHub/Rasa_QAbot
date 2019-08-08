#!/usr/bin/env bash

python -m rasa_nlu.train -c data/nlu_model_config.yaml -d data/training_dataset.json --project="nlu" --fixed_model_name longbi -o models
python -m rasa_core.train -s data/stories.md -d data/domain.yml -o models/dialogue --epochs 200
