import json
from datetime import datetime
from khayyam import JalaliDatetime

from config import rules
from sendmail import send_smtp_email
from sendsms import send_sms
from fixer import get_rate



def archive(filename, rates):
    with open(f'archive/{filename}.json', 'w') as f:
        f.write(json.dumps(rates))


def send_mail(timestamp, rates):

    now_time = JalaliDatetime(datetime.now()).strftime('%y-%B-%d %A %H:%M')
    subject = f' نرخ ارز{now_time} '

    if rules['preferred'] is not None:
        tmp = dict()
        for exc in rules['preferred']:
            tmp[exc] = rates[exc]
        rates = tmp
    text = json.dumps(rates)
    send_smtp_email(subject, text)


def check_notify_rules(rates):
    preferred = rules['notification']['preferred']
    msg = ''
    for exc in preferred.keys():
        if rates[exc] <= preferred[exc]['min']:
            msg += f'{exc} reached min: {rates[exc]}'
        if rates[exc] >= preferred[exc]['max']:
            msg += f'{exc} reached max: {rates[exc]}'

        return msg




if __name__ == "__main__":
    res = get_rate()

    if rules['archive']:
        archive(res['timestamp'], res['rates'])

    if rules['send_mail']:
        send_mail(res['date'], res['rates'])

    if rules['notification']['enable']:
        notification_msg = check_notify_rules(res['rates'])
        if notification_msg:
            now = JalaliDatetime(datetime.now()).strftime('%y-%B-%d %A %H:%M')
            notification_msg += now
            send_sms(notification_msg)
