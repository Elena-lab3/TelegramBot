import requests


def get_schedule(url):
    r = requests.get(url)
    print(r.json())
    return r.json()


class ScheduleDAO:

    def get_todays_schedule(self, url):
        return self.get_schedule(url)['todaySchedules']

    def get_tomorrows_schedule(self, url):
        return self.get_schedule(url)['tomorrowSchedules']

    def get_week(self, url):
        return self.get_schedule(url)['schedules']

    def get_exam(self, url):
        return self.get_schedule(url)['examSchedules']

    def get_schedule(self, url):
        r = requests.get(url)
        print(r.json())
        return r.json()