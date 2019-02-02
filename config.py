CSRF_ENABLED = True  # Prevent fake cross-site requests
SECRET_KEY = 'this-is-sample-secret-key-which-protect-this-blog'
OPENID_PROVIDERS = [
    {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}
]
