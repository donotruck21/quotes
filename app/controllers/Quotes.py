from system.core.controller import *

class Quotes(Controller):
    def __init__(self, action):
        super(Quotes, self).__init__(action)

        self.load_model('Quote')
        self.load_model('User')
        self.db = self._app.db

    def index(self):
    	user_id = session['user_id']
    	all_quotes = self.models['Quote'].get_all_quotes()
    	all_favorites = self.models['Quote'].get_all_favorites(user_id)
    	print all_favorites
        return self.load_view('/quotes/index.html', all_quotes=all_quotes, all_favorites=all_favorites)

    def add(self):
    	quote_info = {
    		'author': request.form['author'],
    		'content': request.form['content'],
    		'user_id': session['user_id']
    	}

    	check_errors = self.models['Quote'].check_errors(quote_info)

        if check_errors['status'] == False:
            for message in check_errors['errors']:
                flash(message, 'regis_errors')
            return redirect('/quotes')
        else:
            print "No Errors!"

            added_quote = self.models['Quote'].add_quote(quote_info)

            return redirect('/quotes')

    def favorite(self):
    	fav_info = {
    		'quote_id': request.form['quote_id'],
    		'user_id': session['user_id']
    	}

    	print fav_info

    	add_fav = self.models['Quote'].add_fav(fav_info)

    	return redirect('/quotes')

    def delete(self):
    	fav_id = request.form['favorite_id']
    	print fav_id
    	self.models['Quote'].delete_fav(fav_id)

    	return redirect('/quotes')









