# coding:utf-8
# 迭代器
class Book:
    pass


class BookColletion:
    def __init__(self):
        self.data = ['《往事》', '《只能》', '《回味》']
        self.cur = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.cur >=len(self.data):
            raise StopIteration()
        r = self.data[self.cur]
        self.cur += 1
        return r


#取出所有
books = BookColletion()
for book in books:
    print(book)
