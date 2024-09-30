from test_for_admin import db, User, app

def create_user(username, password):
    with app.app_context():
        user = User(username=username)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        print(f'User {username} created successfully.')

if __name__ == '__main__':
    username = input('Enter username: ')
    password = input('Enter password: ')
    create_user(username, password)