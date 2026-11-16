#!/bin/bash
# Prompt for an OpenRouter key without echoing it and save it to ~/.openrouter_key (mode 600).
# The waiting run tabs start as soon as the file exists.
umask 077
printf 'Paste your OpenRouter API key (input hidden), then press Enter: '
IFS= read -rs k
echo
if [ -z "$k" ]; then echo "Nothing entered; no file written."; exit 1; fi
printf '%s' "$k" > "$HOME/.openrouter_key.tmp" && mv "$HOME/.openrouter_key.tmp" "$HOME/.openrouter_key"
chmod 600 "$HOME/.openrouter_key"
unset k
echo "Saved to ~/.openrouter_key. The four run tabs will start within a few seconds. You can close this tab."
