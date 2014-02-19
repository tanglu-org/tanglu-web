from menus.base import Menu, NavigationNode
from menus.menu_pool import menu_pool
from menulinks.models import MenuLink

class TangluNavigationMenu(Menu):
    def __get_menu_links(self):
        """Get a list of links from the MenuLinks app"""
        return MenuLink.objects.all()

    def get_nodes(self, request):
        """This should return a list of NavigationNode instances"""
        nodes = []
        menuLinks = self.__get_menu_links()

        menuLinks = sorted(menuLinks, key=lambda link: link.weight)

        for id, link in enumerate(menuLinks):
            nodes.append(NavigationNode(link.title, link.url, id))

        return nodes

menu_pool.register_menu(TangluNavigationMenu)
