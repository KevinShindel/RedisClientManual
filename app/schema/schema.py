import marshmallow_dataclass
import marshmallow

from app.model.model import SiteModel


class FlatCoordinateSchema(marshmallow.Schema):

    @marshmallow.pre_load
    def flat_to_nested_coordinate(self, in_data, **kwargs):
        # Ignore if this is a Coordinate object -- i.e. it only has
        # 'lat' and 'lng' keys.
        if not isinstance(in_data, dict):
            in_data = {}
        if list(in_data.keys()) == ['lat', 'lng']:
            return in_data
        # For all other objects, deserialize a flat coordinate pair
        # to a nested object.
        lat = in_data.pop('lat', None)
        lng = in_data.pop('lng', None)
        if lat and lng:
            in_data['coordinate'] = {'lat': lat, 'lng': lng}
        return in_data

    @marshmallow.post_dump
    def nested_to_flat(self, out_data, **kwargs):
        coordinate = out_data.pop('coordinate', None)
        if coordinate:
            out_data['lat'] = coordinate['lat']
            out_data['lng'] = coordinate['lng']
        return out_data


FlatSiteSchema = marshmallow_dataclass.class_schema(SiteModel, base_schema=FlatCoordinateSchema)
