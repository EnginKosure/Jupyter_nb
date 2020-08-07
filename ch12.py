# https: // edabit.com/challenge/yPzfgnDsPWXwH7dMq


class Pagination:

    def __init__(self, items=[], pageSize=10):
        self.items = items
        self.pageSize = int(pageSize)
        self.totalPages = (len(items)//pageSize) + \
            (1 if len(items) % pageSize else 0)
        self.currentPage = 1

    def getItems(self):
        return self.items

    def getPageSize(self):
        return self.pageSize

    def getCurrentPage(self):
        return self.currentPage

    def prevPage(self):
        if self.currentPage != 1:
            self.currentPage -= 1
        # self.currentPage = max(self.currentPage - 1, 1)
        return self

    def nextPage(self):
        if self.currentPage != self.totalPages:
            self.currentPage += 1
        # self.currentPage = min(self.currentPage + 1, self.totalPages)
        return self

    def firstPage(self):
        self.currentPage = 1
        return self

    def lastPage(self):
        self.currentPage = self.totalPages
        return self

    def goToPage(self, pageNum):
        if 1 < int(pageNum) <= self.totalPages:
            self.currentPage = int(pageNum)
        elif int(pageNum) <= 1:
            self.currentPage = 1
        else:
            self.currentPage = self.totalPages
        # self.currentPage = max(min(int(page), self.totalPages), 1)
        return self

    def getVisibleItems(self):
        return self.items[(self.currentPage-1)*self.pageSize:self.currentPage*self.pageSize]


alphabetList = list("abcdefghijklmnopqrstuvwxyz")

p = Pagination(alphabetList, 4)

print(p.getVisibleItems())  # ["a", "b", "c", "d"]
p.nextPage()
print(p.getVisibleItems())  # ['e', 'f', 'g', 'h']
p.lastPage()
print(p.getVisibleItems())  # ["y", "z"]
