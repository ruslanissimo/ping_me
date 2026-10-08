# Ping Me Telegram

`ping-me-telegram` is a lightweight Python utility that allows you to easily send messages from your code directly to your Telegram account. 

Never miss an important event while away from your terminal. It is ideal for:
- **Long-running simulations/training:** Get notified when a heavy computation or training loop finishes.
- **AI Agents:** Track agent progress, milestones, or unexpected behaviors in real-time.
- **Server Alerts:** Instantly catch and report critical exceptions or server errors.

---

## 1. Installation

Install the package via `pip`:

```bash
pip install ping-me-telegram
```

## 2. Registration

Go to the Telegram bot and copy your token
https://t.me/ping_me_when_youre_done_bot

---

## 3. Quick Start

Here is a quick example of how to use the utility in your scripts:

```python
from ping_me_telegram import ping_me

# Send a simple notification
ping_me(token= "place_your_token", message="Hello world")

```

---

## Requirements

- Python >= 3.8
- `requests >= 2.34.2, < 3.0.0`

---

## License

This project is licensed under the terms of the [MIT License](LICENSE).