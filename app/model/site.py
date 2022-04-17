from app.dao.dao_base import SiteDaoBase
from app.core.dao_redis import RedisDaoBase
from app.model.model import SiteModel
from app.schema.schema import FlatSiteSchema


class SiteDaoRedis(SiteDaoBase, RedisDaoBase):

    def create(self, site: SiteModel, *args, **kwargs):
        hash_key = self.key_schema.site_hash_key(site_id=site.id)
        #
        client = kwargs.get('pipeline', self.redis)
        client.hset(name=hash_key, mapping=FlatSiteSchema().dump(site))
        #
        site_ids_key = self.key_schema.site_ids_key()
        return bool(client.sadd(site_ids_key, site.id))

    def bulk_create(self, *sites: SiteModel, **kwargs):
        for site in sites:  # TODO: Need to refactoring in case low
            self.create(site=site)

    def filter_by_id(self, *site_ids: int, **kwargs):
        hash_keys = [self.key_schema.site_hash_key(site_id) for site_id in site_ids]
        site_hashes = [self.redis.hgetall(hash_key) for hash_key in hash_keys]  # TODO: Need refactoring?
        instances = {FlatSiteSchema().load(site_hash) for site_hash in site_hashes}  # TODO: Need refactoring?
        return instances

    def filter_starts_with(self, pattern):
        hash_keys = self.key_schema.startswith_hash_key(pattern=pattern)
        site_hashes = [self.redis.hgetall(hash_key) for hash_key in self.redis.keys(hash_keys)]
        instances = {FlatSiteSchema().load(site_hash) for site_hash in site_hashes}
        return instances

    def filter_ends_with(self, pattern):
        hash_keys = self.key_schema.endswith_hash_key(pattern=pattern)
        site_hashes = [self.redis.hgetall(hash_key) for hash_key in self.redis.keys(hash_keys)]
        instances = {FlatSiteSchema().load(site_hash) for site_hash in site_hashes}
        return instances

    def get(self, site_id: int, *args, **kwargs):
        hash_key = self.key_schema.site_hash_key(site_id=site_id)
        site_hash = self.redis.hgetall(hash_key)
        if not site_hash:
            raise Exception('Site Not Found!')
        instance = FlatSiteSchema().load(site_hash)
        return instance

    def delete(self, site_id: int):
        hash_key = self.key_schema.site_hash_key(site_id=site_id)
        return bool(self.redis.delete(hash_key))
