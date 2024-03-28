#!/bin/bash
sends a DELETE request to the URL passed as the 1st arg and displays the body of response
curl -sX DELETE "$1"
