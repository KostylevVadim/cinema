# База данных для онлайн кинотеатра

База данных онлайн кинотеатра и скрипты для заполнения. СУБД - PostgreSQL, для подключения и заполнения использовал psycopg2.

В файле data_fillers - функции для заполнения соответствующих таблиц.

SQL - запросы к базе данных. SELECTORS - простые SELECT, AGR - имеют агригаторы, CASE - имеют CASE, REGULAR - связаны с регулярными выражениями.

context_manager - менеджер контекстов для работы с БД

cinema_worker - класс для работы с базой данных cinema Cinema_worker

Класс Cinema_worker требует при инициации подключение и курсор. В случае, если база данных - не cinema, экземпляр не создается.

Класс Cinema_worker имеет методы:

public:

add_film_or_series - добавляет в БД фильм или сериал, на вход требует название, дату релиза, возраст просмотра, фильм или сериал, бюджет, сезон, серия.

add_user - добавляет в БД пользователя, на вход требует имя пользователя, почту, пароль, является ли пользователь "важным", имеет ли подписку.

your_select_command - позволяет написать свой SELECT запрос к БД. На вход требует строку с запросом и переменные для подстановки. В резултате возвращает список.

restore_user - восстанавливает удаленного пользователя, на вход требует имя пользователя.

delete_user - удаляет пользователя, на вход требует имя пользователя.

dump_table_to_json - позваляет выгрузить таблицу в json файл, на вход требует имя таблицы.

Private:

__uniq_password - проверяет уникальность пароля. На вход получает пароль.

__uniq_username - проверяет уникальность имени пользователя. На вход получает имя.

__uniq_mail - проверяет уникальность почты. На вход получает почту.

__is_valid_mail - проверяет, является ли почта допустимой. На вход получает почту.

__getting_data - получает данные по всей таблице. На вход получает имя талицы.

__transform_to_list_of_dicts - превращает список результата выбора по таблице и списка имен колонок таблиц в список словарей.