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

