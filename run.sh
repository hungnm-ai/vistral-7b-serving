#!/bin/bash
gunicorn "api.routers:app" --workers 2 --preload --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8080