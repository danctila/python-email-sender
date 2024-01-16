 # Python Email Sender

python-email-sender is a tool for sending data pulled from an API to emails.

## Installation

Use python3 from https://www.python.org/ to run .


## Usage
1. Import all three files to development environment.

2. In emailSender.py replace myEmail@gmail.com with your own email and myEmailPassword with the password to that email. The more secure version of this would be through [google app passwords](https://support.google.com/accounts/answer/185833?hl=en "google app passwords").

3. The from_email can be left as youremail@gmail.com


```python
import smtplib

def Send(adresses, subject, body):
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_username = 'myEmail@gmail.com'
    smtp_password = 'myEmailPassword'

    from_email = 'youremail@gmail.com'

```
4. In factSender.py replace the adresses with any valid emails you want to recieve the message

```python
import emailSender
import factAPI
import datetime

# find current year, month, and day and format to year and month shorthand
now = datetime.datetime.now()
curYear = str(now.strftime("%y")) # year, short version-w/o century
curMonth = str(now.strftime("%m")) # month, as number
curDayText = str(now.strftime("%A")) # weekday, full version
curDayNum = str(now.strftime("%d")) # weekday, as number

# Day month-dayNum-yearAbrev
today = (curDayText + " " + curMonth + "-" + curDayNum + "-" + curYear).replace(u'\xa0', u' ')

adresses = ['emailOne@gmail.com', 'emailTwo@gmail.com', 'emailThree@gmail.com']
subject = 'Daily Fact Digest | ' + today
body = factAPI.randomFact()

emailSender.Send(adresses, subject, body)
```
4. Run factSender.py to send API data to email adresses assigned from the email adress inputed in emailSender.py

## Acknowledgements

- python-email-sender uses the [uselessfacts API](https://uselessfacts.jsph.pl/ "uselessfacts API") to pull data from the /today endpoint for a daily useless fact.
- python's dateTime library is also used to pull exact time when emails are sent to include in the subject of the given message

## In Action

The fact senders message appears as below when a message is sent.

<img src="https://github.com/danctila/python-email-sender/assets/134968796/8baa1b15-f9c0-4443-aa8a-c50f5d2f43b6" alt="email" width="500"/>
