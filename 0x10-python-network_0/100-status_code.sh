#!/bin/bash
#script sends a request to a URL passed as an argument, and displays only the status code
curl -o /dev/null -w "%{http_code}" -sLI "$1"
