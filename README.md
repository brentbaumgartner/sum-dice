# sum-dice
Discord dice bot written in Python that shows individual rolls and the sum.

## Python depends:
- `pip install discord.py`
- `pip install Flask`

## Also requires:
- WSGI server like Gunicorn or uWSGI
- reverse proxy like nginx

## Adjust sum-dice.py:
- Search and replace `serveridhere` with your server ID
- Search and replace `secrettokenhere` with your secret token (2 entries)

## Channel commands:
- `!roll` Roll one die
- `!roll 6` Roll [1-6] dice
