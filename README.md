# History Lives

A multi-character historical empathy prototype. Students have conversations
with AI-generated historical figures and composite characters from World War Two.

## Project Structure

```
history_lives/
├── Home.py                  # Landing page / about / mission
├── auth.py                  # Login + usage tracking
├── character_engine.py      # Shared logic for all character pages
├── requirements.txt
├── .gitignore
├── .streamlit/
│   └── secrets.toml.template   # Copy to secrets.toml and fill in
└── pages/
    ├── 0_Persona_Guide.py    # Educator guide with discussion questions
    ├── 1_General_Eisenhower.py
    ├── 2_Field_Marshal_Rommel.py
    ├── 3_Prime_Minister_Churchill.py
    ├── 4_Marianne.py
    ├── 5_Judy.py
    ├── 6_Miguel.py
    └── 7_Aleksei.py
```

## Local Setup (Windows / VS Code)

1. Copy `.streamlit/secrets.toml.template` to `.streamlit/secrets.toml`
2. Fill in your Anthropic API key, ElevenLabs API key, and all 7 voice IDs
3. Set your `ACCESS_CODES` - format is `CODE:limit,CODE2:limit2`
   - Example: `ACCESS_CODES = "TEACHER01:50,WIFE:500,DEMO:30"`
   - Each code gets its own message budget, tracked in `usage_log.json`
4. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
5. Run it:
   ```
   streamlit run Home.py
   ```

The app opens with a login screen. Enter any code from your `ACCESS_CODES`
list to access the characters.

## How Login & Usage Tracking Works

- Each access code has a message limit (e.g., 50 messages)
- Usage is tracked across ALL characters combined per code
  (so one code = one "budget" regardless of which characters are used)
- Usage persists in `usage_log.json` - if you restart the app, usage is remembered
- When a code hits its limit, the user sees a friendly message
- The sidebar shows "messages remaining" for the active session

To give someone a fresh code, just add it to `ACCESS_CODES` in secrets.toml
and restart the app (or redeploy).

## Deploying to Streamlit Community Cloud

1. Push this folder to a GitHub repository
   - Make sure `.streamlit/secrets.toml` is in `.gitignore` (it already is)
     and NOT committed - your API keys should never go to GitHub
2. Go to share.streamlit.io and connect your GitHub repo
3. Set the main file path to `Home.py`
4. In the Streamlit Cloud dashboard, go to your app's Settings → Secrets
   and paste in the contents of your local `secrets.toml` (with real values)
5. Deploy

Your app will be live at a URL like `yourappname.streamlit.app`

## Adding/Changing Access Codes After Deployment

Edit the `ACCESS_CODES` secret in the Streamlit Cloud dashboard
(Settings → Secrets), save, and the app will pick up the new codes
on next restart (Streamlit Cloud restarts automatically after secrets changes).

## Notes

- `usage_log.json` is created automatically on first use and lives in the
  app's filesystem. On Streamlit Community Cloud, this resets if the app
  reboots/redeploys - fine for a demo/pilot phase, but not durable long-term
  storage. If usage tracking needs to survive redeploys reliably, this would
  need to move to a small external database.
- All 7 characters share the same Anthropic and ElevenLabs API keys -
  monitor your usage on both platforms' dashboards during pilots.
