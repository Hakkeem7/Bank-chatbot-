from flask import Flask, render_template, request
import requests

app = Flask(__name__)

BANK_PROMPT = """
You are an AI Banking Assistant.

Rules:
- Answer ONLY banking and finance related questions.
- Topics include:
    * Bank accounts
    * Debit cards
    * Credit cards
    * UPI
    * NEFT
    * RTGS
    * IMPS
    * Loans
    * Fixed Deposits
    * Savings Accounts
    * Current Accounts
    * Internet Banking
    * Mobile Banking
    * Cheque
    * Interest Rates
    * Banking Security
    * KYC
    * ATM
    * Digital Payments

If the question is NOT related to banking, reply:

"I am a Banking Assistant. Please ask only banking-related questions."

Keep answers:
- Short
- Simple
- Professional
- Easy to understand

Never ask for:
- Password
- OTP
- ATM PIN
- CVV
- Aadhaar Number
- Full Account Number

Never pretend to access customer accounts.
"""

@app.route("/", methods=["GET", "POST"])
def home():
    output = ""

    if request.method == "POST":
        user_query = request.form.get("user")

        prompt = f"""
{BANK_PROMPT}

Customer Question:
{user_query}

Answer:
"""

        url = "http://localhost:11434/api/generate"

        response = requests.post(
            url,
            json={
                "model": "tinyllama",
                "prompt": prompt,
                "stream": False
            }
        )

        if response.status_code == 200:
            output = response.json()["response"]
        else:
            output = "Unable to connect to the AI model."

    return render_template("index.html", output=output)

if __name__ == "__main__":
    app.run(debug=True)