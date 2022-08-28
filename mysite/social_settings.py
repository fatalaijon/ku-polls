# import this at the END of settings.py

INSTALLED_APPS += ['social_django']

# comment out unneeded backends
AUTHENTICATION_BACKENDS = [
    'social_core.backends.open_id.OpenIdAuth',
    'social_core.backends.google.GoogleOpenId',
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.google.GoogleOAuth',
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.yahoo.YahooOpenId',
    'django.contrib.auth.backends.ModelBackend',   # required
    ]

# Require HTTPS in redirect after authentication by 3rd party
SOCIAL_AUTH_REDIRECT_IS_HTTPS = False

# where to redirect to in case of error
SOCIAL_AUTH_LOGIN_URL = '/login/'

# redirect after successful login
# If not set, uses LOGIN_REDIRECT_URL
SOCIAL_AUTH_LOGIN_REDIRECT_URL = LOGIN_REDIRECT_URL

# User model must have username and email fields
SOCIAL_AUTH_USER_MODEL = 'django.contrib.auth.models.User'


