# restart (new session taking over)

1. Read CLAUDE.md and README.md. START.md is not in this repo; if it appears, follow it.
2. Run `bash tools/setup-signing.sh <your-name>@SovereignWebsite.dinis <session-url>`, commit your public key, sign commits.
3. Read now.md here. Do not add images until Dinis supplies photos and the bio.
4. Pages are generated: `python3 docs/tools/make-pages.py`, then `bash tools/check.sh`.
5. Push to dev only.
