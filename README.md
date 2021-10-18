# IGGUpdateChecker
lol idk why i made this

what this does is send a request to the igg-games game request page and search if a game has been updated lol

# How to use:

## Installation:
```bash
git clone https://github.com/Nameless9000/IGGUpdateChecker.git
cd IGGUpdateChecker
pip install -r requirements.txt
```

## Usage:

1. Edit gamelist.json and put in a game name with the value set to 0 eg.
```json
{
    "Minecraft": 0
}
```

2. Edit the DISCORD_ID value if you want a ping

3. Edit .env and put in your webhook url

4. Run the python script
```bash
python main.py
```
