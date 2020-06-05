import time
from plyer import notification


if __name__ == '__main__':
    while True:
        notification.notify(
            title="Covid-19 Remainder",
            app_name="Health & Safety",
            message="During Covid-19 Pandamic Wash Your Hands in Every 10 Mins. Go Wash Your Hands",
            app_icon="C:/Users/noman/PycharmProjects/CovidNotiCentre/handwash.ICO",
            timeout=7,
            )
        time.sleep(10)
