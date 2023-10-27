import time
import logging
from yoyo import read_migrations, get_backend

logger = logging.getLogger()
logging.basicConfig(
    format='%(asctime)s %(filename)25s:%(lineno)5s - %(levelname)10s %(message)s'
)
logger.setLevel(logging.INFO)

time.sleep(5)
backend = get_backend("postgres://postgres:postgres@192.168.100.71:5432/countries")

logger.info(f"Backend object: {backend}")

migrations = read_migrations('./migrations')

logger.info(f"Migrations: {migrations}")

with backend:
    with backend.lock():#"8000:8000"
        backend.apply_migrations(backend.to_apply(migrations))
