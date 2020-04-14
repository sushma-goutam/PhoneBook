# Logging in Django

### Example of creating an instance of custom logger
``` 
app_logger = logging.getLogger('gclogger')
app_logger.info('Hi!')
``` 

### Define Django logging configuration in settings.py file
```
import logging
from logging.handlers import SysLogHandler

import logzero
from logzero import logger

# Logging configurations
CONSOLE_LOGGING_FILE_LOCATION = os.path.join(BASE_DIR, 'django-server.log')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': "%(asctime)s %(levelname)-8s %(module)s [%(pathname)s:%(lineno)d] %(name)s.%("
                      "funcName)s %(message)s",
            'style': '%',
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
        'my_formatter': {
            'format': "%(asctime)s %(levelname)s %(module)s [%(name)s:%(lineno)s] %(message)s",
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
        'file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': CONSOLE_LOGGING_FILE_LOCATION,
            'mode': 'a',
            'encoding': 'utf-8',
            'formatter': 'my_formatter',
            'backupCount': 3,
            'maxBytes': 10485760,
        },
        'syslog': {
            'level':'INFO',
            'class':'logging.handlers.SysLogHandler',
            'formatter': 'verbose',
            #'facility': SysLogHandler.LOG_LOCAL2,
            'facility': SysLogHandler.LOG_USER,
            # Address should be set according to underlying OS
            #'address': '/dev/log',     # Use it only in a linux system
            'address': ('localhost',1024),
            'socktype': socket.SOCK_DGRAM,
        },
    },
    'loggers': {
        # Root logger: All INFO level messages (or higher) will be printed to the console
        'custom': {
            'level': 'INFO',
            'handlers': ['console', 'file'],
        },
        # Passes all messages to the console and file handler.
        'django': {
            'handlers': ['console', 'file'],
            'level': 'INFO',
            'propagate': False,
        },
        # Log messages related to requests received by the django server.
        'django.server': {
            'propagate': True,
        },
        # Log messages related to the rendering of templates.
        'django.template': {
            'handlers': ['file'],
            'propagate': False,
        },
        'gclogger': {
            'handlers': ['syslog'],
            'level': 'INFO',
            'propagate': True,
            },
    },
}
```

### Writing to syslog

Logs will be available in /var/log/syslog

The SysLogHandler class, located in the logging.handlers module,
supports sending logging messages to a remote or local Unix syslog.

### SysLogHandler

The SysLogHandler class, located in the logging.handlers module, supports sending logging messages to a remote or local 
Unix syslog.

class logging.handlers.SysLogHandler(address=('localhost', SYSLOG_UDP_PORT), facility=LOG_USER, socktype=socket.SOCK_DGRAM)

    Returns a new instance of the SysLogHandler class intended to communicate with a remote Unix machine whose address 
    is given by address in the form of a (host, port) tuple. If address is not specified, ('localhost', 514) is used. 
    The address is used to open a socket. An alternative to providing a (host, port) tuple is providing an address as 
    a string, for example ‘/dev/log’. In this case, a Unix domain socket is used to send the message to the syslog. 
    
    If facility is not specified, LOG_USER is used. The type of socket opened depends on the socktype argument, 
    which defaults to socket.SOCK_DGRAM and thus opens a UDP socket. To open a TCP socket (for use with the newer syslog 
    daemons such as rsyslog), specify a value of socket.SOCK_STREAM.

    Note that if your server is not listening on UDP port 514, SysLogHandler may appear not to work. In that case, 
    check what address you should be using for a domain socket - it’s system dependent. 
    For example, on Linux it’s usually ‘/dev/log’ but on OS/X it’s ‘/var/run/syslog’. You’ll need to check your platform 
    and use the appropriate address (you may need to do this check at runtime if your application needs to run on several 
    platforms). On Windows, you pretty much have to use the UDP option.