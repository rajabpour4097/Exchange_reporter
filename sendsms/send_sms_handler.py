from kavenegar import *


API_KEY = '38435973555755334549722B4465664369723170794C356C2F396453436C415062385357464D56346A4B733D'

number = '09111127685'


def send_sms(text):

    try:
        api = KavenegarAPI(API_KEY)
        params = {
            'sender': '10004346',
            'receptor': number,
            'message': text
        }
        response = api.sms_send(params)
        print(str(response))

    except APIException as e:
            print(str(e))
    except HTTPException as e:
            print(str(e))