import time

import schedule

def api_requests():
    def get_current_volumes():
        print('wwww')


    #schedule.every().day.at("20:28", "Europe/Moscow").do(get_current_volumes)
    schedule.every(10).seconds.do(get_current_volumes)
    while True:
        schedule.run_pending()
        print('for loop')
        time.sleep(10)