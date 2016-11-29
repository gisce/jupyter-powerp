import sys
import logging
import os
sys.path.append(os.environ['OPENERP_ROOT_PATH'])
from backend import OpenERPService
from backend import Transaction
from backend import PoolWrapper


logger = logging.getLogger('jupyter-powererp.OpenERPService')
logging.basicConfig(level=logging.INFO)

logger.info('Using native OOOP')
service = OpenERPService()
service.db_name = "dbname"
uid = service.login("user", "password")
O = PoolWrapper(service.pool, service.db_name, uid)

polissa_model = O.model('giscedata.polissa')
pol = polissa_model.browse(2)
print("{}".format(pol.name))