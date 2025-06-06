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

curl http://localhost:11434/api/generate -d '{
  "model": "dolphin3:latest",
  "prompt": "write a git title commit (include emojis)  based on this data  diff --git a/media/plants_image/camera.png b/media/plants_image/camera.png deleted file mode 100644 index 8a884c2..0000000",
  "stream": false
}'