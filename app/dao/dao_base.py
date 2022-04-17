from abc import ABC

from app.model.model import SiteModel


class SiteDaoBase(ABC):

    def create(self, site: SiteModel, *args, **kwargs):
        raise NotImplemented

    def bulk_create(self, *sites: SiteModel, **kwargs):
        raise NotImplemented

    def get(self, site_id: int, *args, **kwargs):
        raise NotImplemented

    def filter_by_id(self, *site_id: int, **kwargs):
        raise NotImplemented
