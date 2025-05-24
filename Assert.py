def login(username, password):
    correct_username = "admin"
    correct_password = "qwerty123"

    try:
        assert username == correct_username, "Невірне ім'я користувача або пароль"
        assert password == correct_password, "Невірне ім'я користувача або пароль"
        print("Вхід виконано успішно")
    except AssertionError:
        print("Невірне ім'я користувача або пароль")


login("admin", "qwerty123")
login("user", "password")
login("admin", "wrongpass")