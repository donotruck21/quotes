from system.core.router import routes

routes['default_controller'] = 'Users'

"""
    routes['GET']['/users'] = 'users#index'
    routes['GET']['/users/new'] = 'users#new'
    routes['POST']['/users'] = 'users#create'
    routes['GET']['/users/<int:id>'] = 'users#show'
    routes['GET']['/users/<int:id>/edit' = 'users#edit'
    routes['PATCH']['/users/<int:id>'] = 'users#update'
    routes['DELETE']['/users/<int:id>'] = 'users#destroy'
"""

routes['POST']['/register'] = 'Users#register'
routes['POST']['/login'] = 'Users#login'
routes['GET']['/logout'] = 'Users#logout'
routes['GET']['/users/<id>'] = 'Users#show'

routes['GET']['/quotes'] = "Quotes#index"
routes['POST']['/quotes/add'] = "Quotes#add"
routes['POST']['/favorite'] = "Quotes#favorite"
routes['POST']['/deletefav'] = "Quotes#delete"