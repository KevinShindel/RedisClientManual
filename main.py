import sys

from app.core.core import (get_redis_connection,
                           get_async_redis_connection,
                           get_cloud_redis_connection,
                           get_cluster_redis_connection)
from app.model.model import SiteModel
from app.model.site import SiteDaoRedis


def main():
    client_type = sys.argv[1]
    if client_type == 'd':
        client = get_redis_connection()
    elif client_type == 'a':
        client = get_async_redis_connection()
    elif client_type == 'c':
        client = get_cloud_redis_connection()
    elif client_type == 't':
        client = get_cluster_redis_connection()
    else:
        client = get_redis_connection()

    db = SiteDaoRedis(client=client)
    sites = [SiteModel(id=i) for i in range(10000)]
    result = db.bulk_create(*sites)
    print(result)


if __name__ == '__main__':
    main()
