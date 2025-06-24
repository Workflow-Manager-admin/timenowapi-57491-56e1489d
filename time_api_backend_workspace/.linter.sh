#!/bin/bash
cd /home/kavia/workspace/code-generation/timenowapi-57491-56e1489d/time_api_backend_workspace/time_api_backend
source venv/bin/activate
flake8 .
LINT_EXIT_CODE=$?
if [ $LINT_EXIT_CODE -ne 0 ]; then
  exit 1
fi

