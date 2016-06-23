from system.core.controller import *

class Users(Controller):
    def __init__(self, action):
        super(Users, self).__init__(action)

        self.load_model('User')
        self.load_model('Quote')
        self.db = self._app.db

    def index(self):

        return self.load_view('/users/index.html')

    def register(self):
        # print "hello" *100
        print request.form['birthday']

        
        user_info = {
            "name" : request.form['name'],
            "alias" : request.form['alias'],
            "email" : request.form['email'],
            "birthday" : request.form['birthday'],
            "password" : request.form['password'],
            "pw_confirm" : request.form['pw_confirmation']
        }
        print user_info
        create_status = self.models['User'].create_user(user_info)

        if create_status['status'] == True:
            session['user_id'] = create_status['user']['id']
            session['name'] = create_status['user']['name']
            session['alias'] = create_status['user']['alias']
            return redirect('/quotes')

        else:
            for message in create_status['errors']:
                flash(message, 'regis_errors')
            return redirect('/')

    def login(self):
        print "l"
        user_info = {
            "email" : request.form['email'],
            "password" : request.form['password'],
        }

        login_user = self.models['User'].login_user(user_info)

        if login_user == False:
            flash('Combination did not match')
            return redirect('/')
        else:
            print login_user[0]
            session['user_id'] = login_user[0]['id']
            session['name'] = login_user[0]['name']
            session['alias'] = login_user[0]['alias']
            return redirect('/quotes')

    def logout(self):
        session.clear()
        return redirect('/')

    def show(self, id):
        print id
        all_quotes = self.models['Quote'].get_quotes_by_user_id(id)
        quote_count = self.models['Quote'].get_count_by_user_id(id)

        return self.load_view('/users/show.html', all_quotes=all_quotes, quote_count=quote_count)

