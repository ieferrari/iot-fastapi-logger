#!/bin/bash
working_directory=$(pwd)
cd ..
uvicorn  fastapi-template.main:app --reload
