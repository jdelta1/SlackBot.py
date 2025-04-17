# SlackBot.py
Simple Stage1 / Outflank C2 Slack Bot

Currently will just ping you when a new beacon checks in.

Create an incoming [webhook](https://api.slack.com/messaging/webhooks) for a Slack bot and paste it in. Drop this bad boy in `shared/bots/on` on your Teamserver and restart the bot engine `docker container restart <container ID>`. 
