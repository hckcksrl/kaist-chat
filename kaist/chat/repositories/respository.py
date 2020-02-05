import abc
from typing import List
from kaist.chat.models.models import \
    FCLT, WEST, EAST1, EAST2, EMP, ICC, HAWAM, DAY

from kaist.chat.entities.entity import MenuEntity


class MenuABCRepository:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_fclt_menu(self, day: str) -> List[MenuEntity]:
        pass

    @abc.abstractmethod
    def get_west_menu(self, day: str) -> List[MenuEntity]:
        pass

    @abc.abstractmethod
    def get_east1_menu(self, day: str) -> List[MenuEntity]:
        pass

    @abc.abstractmethod
    def get_east2_menu(self, day: str) -> List[MenuEntity]:
        pass

    @abc.abstractmethod
    def get_emp_menu(self, day: str) -> List[MenuEntity]:
        pass

    @abc.abstractmethod
    def get_icc_menu(self, day: str) -> List[MenuEntity]:
        pass

    @abc.abstractmethod
    def get_hawam_menu(self, day: str) -> List[MenuEntity]:
        pass


class MenuRepository(MenuEntity):
    def get_fclt_menu(self, day: str) -> List[MenuEntity]:
        day = DAY.objects.get(day=day)
        menus = FCLT.objects.filter(day=day.id)
        menu_entities = [menu.to_entity() for menu in menus]

        return menu_entities

    def get_west_menu(self, day: str) -> List[MenuEntity]:
        day = DAY.objects.get(day=day)
        menus = WEST.objects.filter(day=day.id)
        menu_entities = [menu.to_entity() for menu in menus]

        return menu_entities

    def get_east1_menu(self, day: str) -> List[MenuEntity]:
        day = DAY.objects.get(day=day)
        menus = EAST1.objects.filter(day=day.id)
        menu_entities = [menu.to_entity() for menu in menus]

        return menu_entities

    def get_east2_menu(self, day: str) -> List[MenuEntity]:
        day = DAY.objects.get(day=day)
        menus = EAST2.objects.filter(day=day.id)
        menu_entities = [menu.to_entity() for menu in menus]

        return menu_entities

    def get_emp_menu(self, day: str) -> List[MenuEntity]:
        day = DAY.objects.get(day=day)
        menus = EMP.objects.filter(day=day.id)
        menu_entities = [menu.to_entity() for menu in menus]

        return menu_entities

    def get_icc_menu(self, day: str) -> List[MenuEntity]:
        day = DAY.objects.get(day=day)
        menus = ICC.objects.filter(day=day.id)
        menu_entities = [menu.to_entity() for menu in menus]

        return menu_entities

    def get_hawam_menu(self, day: str) -> List[MenuEntity]:
        day = DAY.objects.get(day=day)
        menus = HAWAM.objects.filter(day=day.id)
        menu_entities = [menu.to_entity() for menu in menus]

        return menu_entities
