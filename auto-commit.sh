#!/bin/bash
# Get git status in short format
git_status=$(git status --short)

read -p "Which branch to push? " branch
echo "Pushing to branch $branch"
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
git push origin $branch

echo "Committed with message:"
echo "$commit_message"

