# Тесты для тестирования основных функций сайта магазина электроники DNS

**Команда для установки пакетов из requirements.txt**: pip install -r requirements.txt

**Команда для запуска тестов**:  pytest -sv --alluredir=test_results/ test.py

**Команда для просмотра отчетов allure**:  allure serve test_results/



[Ссылка на Allure отчет из GitHub Actions](https://codeels.github.io/DNS_shop_autotests/)

### Шаги в тесте 1:
1.	логин
2.	подготовка корзины и страницы сравнения для тестов (происходит очистка от товаров)
3.	переход на страницу с процессорами
4.	фильтрация товаров по параметрам
5.	добавление одного товара в корзину
6.	переход в корзину
7.	проверка товара по параметрам
8.	переход к странице оформления заказа
9.	заполнение номера, email, выбор магазина (если не выбран автоматом), подтверждение заказа через смс код


### Шаги в тесте 2:
1.	подготовка корзины и страницы сравнения для тестов (происходит очистка от товаров)
2.	переход на страницу с процессорами
3.	фильтрация товаров по параметрам
4.	добавление одного товара в корзину
5.	переход в корзину
6.	проверка товара по параметрам
7.	переход к странице оформления заказа
8.	логин на странице оформления заказа
9.	заполнение номера, email, выбор магазина (если не выбран автоматом), подтверждение заказа через смс код


### Шаги в тесте 3:
1.	логин
2.	подготовка корзины и страницы сравнения для тестов (происходит очистка от товаров)
3.	переход на страницу с процессорами
4.	фильтрация товаров по параметрам
5.	добавление двух товаров в сравнение
6.	проверка товаров по разным параметрам (проверка на то, что на страницу сравнения добавились выбранные товары)
7.	добавление более дешевого товара в корзину
8.	переход в корзину
9.	переход к странице оформления заказа
10.	заполнение номера, email, выбор магазина (если не выбран автоматом), подтверждение заказа через смс код


### Шаги в тесте 4:
1.	логин
2.	подготовка корзины и страницы сравнения для тестов (происходит очистка от товаров)
3.	переход на страницу с процессорами
4.	фильтрация товаров по параметрам
5.	выбор товара и переход на его страницу
6.	проверка товара по параметрам на странице товара
7.	добавление товара в корзину
8.	переход в корзину
9.	проверка товара по параметрам в корзине
10.	переход к странице оформления заказа
11.	заполнение номера, email, выбор магазина (если не выбран автоматом), подтверждение заказа через смс код
