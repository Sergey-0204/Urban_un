def test_function():
    def inner_function():  # функция внутри функции
        print("Я в области видимости функции test_function")

    inner_function()  # Вызов функции inner_function внутри функции test_function


test_function()  # Вызов функции test_function

# Попытка вызвать inner_function вне функции test_function
inner_function()
