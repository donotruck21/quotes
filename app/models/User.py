from system.core.model import Model
import re

class User(Model):
    def __init__(self):
        super(User, self).__init__()


    def create_user(self, info):
        EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
        errors = []

        if not info['name']:
            errors.append('Name cannot be blank')
        # elif len(info['name']) < 2:
            # errors.append('First name must be at least 2 characters long')

        if not info['alias']:
            errors.append('Alias cannot be blank')
        # elif len(info['last_name']) < 2:
            # errors.append('Last name must be at least 2 characters long')

        if not info['email']:
            errors.append('Email cannot be blank')
        elif not EMAIL_REGEX.match(info['email']):
            errors.append('Email format must be valid!')

        if not info['birthday']:
            errors.append('Birthday cannot be blank')

        if not info['password']:
            errors.append('Password cannot be blank')
        elif len(info['password']) < 8:
            errors.append('Password must be at least 8 characters long')
        elif info['password'] != info['pw_confirm']:
            errors.append('Password and confirmation must match!')

        if errors:
            return {'status': False, 'errors': errors}
        else:
            pw_hash = self.bcrypt.generate_password_hash(info['password'])
            query =  "INSERT INTO users (name, alias, email, birthday, pw_hash, created_at, updated_at) VALUES (:name, :alias, :email, :birthday, :pw_hash, NOW(), NOW())"
            data = {
                'name': info['name'],
                'alias': info['alias'],
                'email': info['email'],
                'birthday': info['birthday'],
                'pw_hash': pw_hash,
            }
            self.db.query_db(query, data)

            get_user_query = "SELECT * FROM users ORDER BY id DESC LIMIT 1"
            user = self.db.query_db(get_user_query)
            return {'status': True, 'user': user[0]}

    def login_user(self, info):
        password = info['password']

        query = "SELECT * FROM users WHERE email = :email LIMIT 1"
        data = {'email': info['email']}

        user = self.db.query_db(query, data)
        print user
        if user:
            if self.bcrypt.check_password_hash(user[0]['pw_hash'], password):
                return user
        return False



    """
    def get_users(self):
        query = "SELECT * from users"
        return self.db.query_db(query)

    def get_user(self):
        query = "SELECT * from users where id = :id"
        data = {'id': 1}
        return self.db.get_one(query, data)

    def add_message(self):
        sql = "INSERT into messages (message, created_at, users_id) values(:message, NOW(), :users_id)"
        data = {'message': 'awesome bro', 'users_id': 1}
        self.db.query_db(sql, data)
        return True
    
    def grab_messages(self):
        query = "SELECT * from messages where users_id = :user_id"
        data = {'user_id':1}
        return self.db.query_db(query, data)

    """