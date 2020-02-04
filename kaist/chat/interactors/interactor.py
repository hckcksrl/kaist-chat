from kaist.chat.repositories.respository import MenuRepository
import datetime


day_list = ['월', '화', '수', '목', '금', '토', '일']


class MenuInteractor:
    def __init__(self):
        self.repository = MenuRepository()
        self.result = {
            "version": "2.0",
            "data": {
                "location": "",
                "menu": ""
            }
        }

    def location_func(self, location: str, day: str):
        if location == '학부식당':
            return self.repository.get_fclt_menu(day=day)

        if location == '서맛골':
            return self.repository.get_west_menu(day=day)

        if location == '동맛골':
            return self.repository.get_east1_menu(day=day)

        if location == '동맛골교직원':
            return self.repository.get_east2_menu(day=day)

        if location == '교직원식당':
            return self.repository.get_emp_menu(day=day)

        if location == '문지캠퍼스':
            return self.repository.get_icc_menu(day=day)

        if location == '화암기숙사':
            return self.repository.get_hawam_menu(day=day)


class GetMenuInteracor(MenuInteractor):
    def execute(self, data: dict):
        result = self.result
        day = data['userRequest']['utterance']
        location = data['userRequest']['block']['name']
        result['data']['location'] = location

        if day in day_list:
            menus = self.location_func(location=location, day=day)

            for menu in menus:

                if menu.menu:
                    result['data']['menu'] = result['data']['menu'] + f'{menu.time}\n{menu.menu}\n\n'

            return result

        today_id = datetime.datetime.today().weekday()
        today = day_list[today_id]
        menus = self.location_func(location=location, day=today)

        for menu in menus:
            result['data']['menu'] = result['data']['menu'] + f'{menu.time}\n{menu.menu}\n\n'

        return result

