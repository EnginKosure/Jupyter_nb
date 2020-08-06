# The pagination class will accept 2 parameters:

# items (default: []): A list of contents to paginate.

# pageSize (default: 10): The amount of items to show in each page.


class Pagination:

    def __init__(self, items=[], pageSize=10):
        self.items = items
        self.pageSize = pageSize
        self.totalPages = len(items)//pageSize+1
        self.currentPage = 0

    def getItems(self):
        return self.items

    def getPageSize(self):
        return self.pageSize

    def getCurrentPage(self):
        return self.currentPage

        # Goes to the previous page
    def prevPage(self):
        self.currentPage -= 1

    def nextPage(self):
        self.currentPage += 1

    def firstPage(self):
        self.currentPage = 0

    def lastPage(self):
        self.currentPage = self.totalPages

    def goToPage(self, pageNum):
        self.currentPage = pageNum

    def getVisibleItems(self):
        pass


alphabetList = "abcdefghijklmnopqrstuvwxyz".split('')

p = Pagination(alphabetList, 4)
