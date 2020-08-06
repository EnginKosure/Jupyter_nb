# The pagination class will accept 2 parameters:

# items (default: []): A list of contents to paginate.

# pageSize (default: 10): The amount of items to show in each page.


class Pagination:

    def __init__(self, items=[], pageSize=10):
        self.items = items
        self.pageSize = pageSize
        self.totalPages = 0
        self.currentPage = 0

    def getItems(self):
        pass

    def getPageSize(self):
        pass

    def getCurrentPage(self):
        pass
        # Goes to the previous page

    def prevPage():
        pass

    def getVisibleItems(self):
        pass


alphabetList = "abcdefghijklmnopqrstuvwxyz".split('')

p = Pagination(alphabetList, 4)
