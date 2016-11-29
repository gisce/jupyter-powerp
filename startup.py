import sys
import logging
import os
logger = logging.getLogger('jupyter-powererp.OpenERPService')
logger.setLevel(logging.DEBUG)
if 'OPENERP_ROOT_PATH' not in os.environ:
    logger.error('OPENERP_ROOT_PATH variable not set')
    print('OPENERP_ROOT_PATH variable not set')
sys.path.append(os.environ['OPENERP_ROOT_PATH'])

from backend import OpenERPService
from backend import PoolWrapper


logging.basicConfig(level=logging.INFO)

logger.info('Using native OOOP')
service = OpenERPService()
service.db_name = "dbname"
uid = service.login("user", "password")
O = PoolWrapper(service.pool, service.db_name, uid)
