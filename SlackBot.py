import requests

from outflank_stage1.bot import BaseBot
from outflank_stage1.implant import Implant


class SlackNotification(BaseBot):
    SLACK_WEBHOOK_URL = "<SLACK WEBHOOK HERE>"

    def on_new_implant(self, implant: Implant):
        message = (
            f"*New Beacon!*\n"
            f"*User:* {implant.get_username()}\n"
            f"*Host:* {implant.get_hostname()}\n"
            f"*OS:* {implant.get_os()} ({implant.get_arch()}-bit)\n"
            f"*First Seen:* {implant.get_first_seen().isoformat()}\n"
            f"*PID:* {implant.get_pid()} ({implant.get_proc_name()})"
        )

        payload = {
            "text": message
        }

        response = requests.post(self.SLACK_WEBHOOK_URL, json=payload)
        response.raise_for_status()
