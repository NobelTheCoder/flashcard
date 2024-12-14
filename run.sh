#!/bin/bash

# Stage all changes
git add .

# Ask for commit message
echo "Enter commit message: "
read commit_message

# Commit with the provided message
git commit -m "$commit_message"

# Push changes to the main branch
git push -u origin main
