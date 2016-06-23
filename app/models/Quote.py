from system.core.model import Model

class Quote(Model):
    def __init__(self):
        super(Quote, self).__init__()


    def check_errors(self, quote_info):
        print quote_info
        errors = []

        if not quote_info['author']:
            errors.append('Author cannot be blank')
        elif len(quote_info['author']) < 4:
            errors.append('Author must be at least 4 characters')

        if not quote_info['content']:
            errors.append('Message cannot be blank')
        elif len(quote_info['content']) < 10:
            errors.append('Message must be at least 10 characters')


        if errors:
            return {'status': False, 'errors': errors}
        else:
            return{'status': True}

    def add_quote(self, quote_info):
        query = "INSERT INTO quotes (user_id, author, content, created_at, updated_at) VALUES (:user_id, :author, :content, NOW(), NOW())"
        data = {
            'user_id': quote_info['user_id'],
            'author': quote_info['author'],
            'content': quote_info['content']
        }
        return self.db.query_db(query, data)

    def get_all_quotes(self):
        query = "SELECT quotes.id, quotes.author, quotes.content, quotes.created_at, quotes.user_id, users.alias FROM quotes JOIN users ON quotes.user_id = users.id ORDER BY quotes.id DESC"
        return self.db.query_db(query)

    def add_fav(self, fav_info):
        query = "INSERT INTO favorites (user_id, quote_id) VALUES (:user_id, :quote_id)"
        data = {
            'user_id': fav_info['user_id'],
            'quote_id': fav_info['quote_id'],
        }

        return self.db.query_db(query, data)

    def get_all_favorites(self, user_id):

        query = "SELECT favorites.id AS favorite_id, favorites.quote_id, favorites.user_id, quotes.content, quotes.author, quotes.user_id AS poster, users.alias FROM favorites JOIN quotes ON favorites.quote_id = quotes.id JOIN users on quotes.user_id = users.id WHERE favorites.user_id = :user_id"
        data = {
            'user_id': user_id
        }

        return self.db.query_db(query, data)

    def delete_fav(self, fav_id):
        query = "DELETE FROM favorites WHERE id = :id"
        data = {
            'id': fav_id
        }
        return self.db.query_db(query, data)

    def get_quotes_by_user_id(self, id):
        query = "SELECT quotes.id, quotes.author, quotes.content, quotes.user_id, users.alias FROM quotes JOIN users ON quotes.user_id = users.id WHERE quotes.user_id = :id"
        data = {
            'id': id
        }

        return self.db.query_db(query, data)

    def get_count_by_user_id(self, id):
        query = "SELECT COUNT(quotes.id) AS num_quotes FROM quotes WHERE user_id = :id"
        data = {
            'id': id
        }

        return self.db.query_db(query, data)


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