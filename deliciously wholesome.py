import requests

def send_simple_message(subject, message_content):
    return requests.post(
        "https://api.mailgun.net/v3/sandbox2874d9171c6b4039a0e164712846e14d.mailgun.org/messages",
        auth=("api", "c8a19079958323587b6805439a42d026-3b1f59cf-71e4abe2"),
        data={"from": "Excited User <mailgun@sandbox2874d9171c6b4039a0e164712846e14d.mailgun.org>",
              "to" : ["letinag3@gmail.com"], #, "bar@example.com", "YOU@sandbox2874d9171c6b4039a0e164712846e14d.mailgun.org"],
              "subject": subject,
              "html": message_content})



response = send_simple_message("Test email", open("/Users/retina/Desktop/Deliciously Wholesome/Deliciously wholesome.html"))
for item in response:
    print item
