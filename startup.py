import sys
import logging
import os
import osconf


required_vars = ['user', 'password']
config = osconf.config_from_environment('OPENERP', required_vars)

logger = logging.getLogger('jupyter-powererp.OpenERPService')
logger.setLevel(logging.DEBUG)
if 'OPENERP_ROOT_PATH' not in os.environ:
    logger.error('OPENERP_ROOT_PATH variable not set')
    print('OPENERP_ROOT_PATH variable not set')
sys.path.append(os.environ['OPENERP_ROOT_PATH'])

if 'OPENERP_DB_NAME' not in os.environ:
    logger.error('OPENERP_DB_NAME variable not set')
    print('OPENERP_DB_NAME variable not set')

from ooservice import OpenERPService
from ooservice import PoolWrapper

logging.basicConfig(level=logging.INFO)

logger.info('Using native OOOP')
service = OpenERPService()
service.db_name = os.environ['OPENERP_DB_NAME']
uid = service.login(config['user'], config['password'])
O = PoolWrapper(service.pool, service.db_name, uid)