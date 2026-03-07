from novulnerable.settings.base import *

DEBUG = False

#ALLOWED_HOSTS = ['104.248.232.43', 'localhost', 'novulnerable.proyectoprogsd.com']
ALLOWED_HOSTS = ['*']

# DATABASES = {
#      "default": {
#          "ENGINE": 'django.db.backends.mysql',
#          "NAME": "novulnerable",
#          "USER": "novulnerable_user",
#          "PASSWORD": "novulnerable_123",
#          "HOST": "127.0.0.1",
#          "PORT": "3306",
#          'OPTIONS': {'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"},
#
#      }
#  }
#







#SECURE_BROWSER_XSS_FILTER :sets the X-XSS-Protection: 1; mode=block header on all responses that do not 
#already have it. This ensures third parties cannot inject scripts into your 
#project. For example, if a user stores a script in your database using a public
#field, when that script is retrieved and displayed to other users it will not run.

SECURE_BROWSER_XSS_FILTER = True

# CSRF_COOKIE_SECURE: is the same as SESSION_COOKIE_SECURE but applies to your CSRF token. 
#CSRF tokens protect against cross-site request forgery. 
#Django CSRF protection does this by ensuring any forms submitted (for logins, 
#signups, and so on) to your project were created by your project and not a third party.

CSRF_COOKIE_SECURE = True

# SESSION_COOKIE_SECURE: tells the browser that cookies can only be handled over HTTPS. 
# This means cookies your project produces for activities, such as logins, 
# will only work over an encrypted connection.
SESSION_COOKIE_SECURE  = True


# SECURE_SSL_REDIRECT : redirects all HTTP requests to HTTPS (unless exempt). This means your project 
# will always try to use an encrypted connection. You will need to have SSL 
# configured on your server for this to work. Note that if you have Nginx or 
# Apache configured to do this already, this setting will be redundant.
SECURE_SSL_REDIRECT = True


SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_AGE = 5 * 60  # 5 minutos
SESSION_EXPIRE_AT_BROWSER_CLOSE = True


# SECURE_HSTS_SECONDS: is the amount of time in seconds HSTS is set for. If you set this for an hour
# (in seconds), every time you visit a web page on your website, it tells your 
# browser that for the next hour HTTPS is the only way you can visit the site.
# If during that hour you visit an insecure part of your website, the browser 
# will show an error and the insecure page will be inaccessible.

SECURE_HSTS_SECONDS = 31536000

SECURE_HSTS_PRELOAD = True

SECURE_HSTS_INCLUDE_SUBDOMAINS = True


