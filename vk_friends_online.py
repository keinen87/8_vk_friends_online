import getpass
import vk


APP_ID = 6225886


def get_user_login():
    login = input('Enter login: ')
    return login


def get_user_password():
    password = getpass.getpass(prompt='Enter password: ')
    return password


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope='friends',
    )
    api = vk.API(session)
    friends_ids_list = api.friends.getOnline()
    return api.users.get(user_ids=friends_ids_list)


def output_friends_to_console(friends_online):
    print('Online is {} people(s)'.format(len(friends_online)))
    for i, friend in enumerate(friends_online, 1):
        print('{}. {} {}'.format(i, friend['last_name'], friend['first_name']))


if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    friends_online = get_online_friends(login, password)
    output_friends_to_console(friends_online)
