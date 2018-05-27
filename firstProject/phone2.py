from twilio.rest import Client


account_sid = "ACba28249fddcca9e700ec9f1c49435d22"
auth_token = "8d9d329c1d977162b607afa2ee0506c9"

client = Client(account_sid, auth_token)

call = client.calls.create(
    to="8613771073133",
    from_="(610)467-2496",
    url="https://demo.twilio.com/welcome/voice/"
)

print(call.sid)
