#!/bin/bash

# diff=$(git diff --cached)
# commit_msg=$(echo "$diff" | ollama run dolphin3:latest | grep -v '^>' | head -n 5)

# echo -e "\nSuggested commit message:\n\n$commit_msg\n"
# read -p "Use this message? (y/n): " choice
# if [[ "$choice" == "y" ]]; then
#     #git commit -m "$commit_msg"
#     echo "this the AI text:"
#     echo $commit_msg
# else
#     echo "Commit aborted."
# fi


# Get git status in short format
git_status=$(git status --short)
#echo $git_status
# Escape newlines and double quotes for JSON
escaped_status=$(printf "%s" "$git_status" | sed ':a;N;$!ba;s/\n/\\n/g' | sed 's/"/\\"/g')

# Create the prompt text
prompt="Write a concise and descriptive Git commit title with emojis based on the following staged changes: $escaped_status"

# Send request to Ollama API
commit_message=$(curl -s http://localhost:11434/api/generate \
  -H "Content-Type: application/json" \
  -d "{
    \"model\": \"dolphin3:latest\",
    \"prompt\": \"$prompt\",
    \"stream\": false
  }" | jq -r '.response')
# Check if commit_message is not empty
if [ -z "$commit_message" ]; then
  echo "No commit message generated. Aborting."
  exit 1
fi

# Commit with the AI-generated message
git commit -m "$commit_message"

echo "Committed with message:"
echo "$commit_message"