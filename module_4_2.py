def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function()#не даёт ошибку, но и не выводит
#inner_function() даёт ошибку
test_function()# выводит только тут