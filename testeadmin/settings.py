from decouple import config


SETTINGS_ENVIRONMENT = config('SETTINGS_ENVIRONMENT', default='PROD')

if SETTINGS_ENVIRONMENT == 'DEV':
    from settings.settings_dev import *

elif SETTINGS_ENVIRONMENT == 'STG':
    pass

elif SETTINGS_ENVIRONMENT == 'PROD':
    from settings.settings_prod import  *



