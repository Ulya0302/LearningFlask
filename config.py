import os


class Config(object):
    # CSRF_ENABLED = True  # Prevent fake cross-site requests
    SECRET_KEY = os.environ.get('SECRET_KEY') or \
                 'this-is-sample-secret-key-which-protect-this-blog'
