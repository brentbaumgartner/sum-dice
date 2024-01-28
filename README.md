# sum-dice
Discord dice bot written in Python that shows individual rolls and the sum.

## Python depends:
- `pip install discord.py`
- `pip install Flask`

## Self hosting requires:
- WSGI server like Gunicorn or uWSGI
- reverse proxy like nginx

## Edit sum-dice.py:
- search and replace `serveridhere` with your server ID
- search and replace `secrettokenhere` with your secret token (2 entries)

## Channel commands:
- `!roll` Roll one die
- `!roll 6` Roll [1-6] dice
