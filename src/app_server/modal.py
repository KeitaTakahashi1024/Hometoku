# カスタマイズされたモーダルを返す
def view_modal(clap:str):
    return {
        "callback_id": "modal_homeru",
        "title": {
            "type": "plain_text",
            "text": "Hometoku",
            "emoji": True
        },
        "submit": {
            "type": "plain_text",
            "text": "Submit",
            "emoji": True
        },
        "type": "modal",
        "close": {
            "type": "plain_text",
            "text": "Cancel",
            "emoji": True
        },
        "blocks": [
            {
                "type": "divider"
            },
            {
                "block_id": "homepeople",
                "type": "input",
                "element": {
                    "type": "multi_users_select",
                    "placeholder": {
                        "type": "plain_text",
                        "text": "Select users",
                        "emoji": True
                    },
                    "action_id": "select_homepeople"
                },
                "label": {
                    "type": "plain_text",
                    "text": "褒めたい人",
                    "emoji": True
                }
            },
            {
                "block_id": "homemove",
                "type": "input",
                "element": {
                    "type": "plain_text_input",
                    "multiline": True,
                    "action_id": "input_homemove"
                },
                "label": {
                    "type": "plain_text",
                    "text": "褒めたいこと",
                    "emoji": True
                }
            },
            {
                "type": "actions",
                "elements": [
                    {
                        "type": "button",
                        "action_id": "prise_countup",
                        "text": {
                            "type": "plain_text",
                            "text": "褒めたい度",
                            "emoji": True
                        }
                    }
                ]
            },
            {
                "type": "context",
			    "block_id": "prise_counter",
			    "elements": [
				    {
                        "type": "mrkdwn",
                        "text": clap
                    }
                ]
            }
        ]
        }

# ショートカットが押された時に表示するモーダルを生成する関数
def view_modal_from_shortcut(client, shortcut):
    # モーダル表示のリクエスト
    _clap = ":clap:"
    client.views_open(
        trigger_id = shortcut["trigger_id"],
        view = view_modal(_clap)
    )

# 褒めたい度が上がった時にモーダルを更新する関数
def update_modal_from_countup(body, client):
    # _clap = view["state"]["values"]["prise_counter"]
    # _clap = body["view"]["state"]["values"]["prise_counter"]
    _clap = body["view"]["blocks"][4]["elements"][0]["text"]
    _clap += ":clap:"
    client.views_update(
        view_id = body["view"]["id"],
        hash = body["view"]["hash"],
        view = view_modal(_clap)
    )
