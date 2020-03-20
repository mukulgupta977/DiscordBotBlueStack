# Discord Bot Setup

Custom Discord bot which has capability to search on google and reply with search results.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements for this project.

Before pip we need to create a virtualenv and activate it in the project folder

```bash
virtualenv env --python=python3

Now go to the env path and activate it

source env/bin/activate

After activating go the path of requirement.txt file and run the below pip_command.
```

```bash
pip install -r requirements.txt
```

## Database

Databse used Mongo Db

1. install mongo db and create database "Bot"
2. Make sure mongo service is running on default port 27017
3. If you wish to change the port please put the new port in ```
__init__.py ```file

## Bot Name and URL
Bot Name - BlueStacksDiscordBot

```html
https://discordapp.com/api/oauth2/authorize?client_id=690152447729074178&permissions=8&scope=bot
```


## License
[MIT](https://choosealicense.com/licenses/mit/)