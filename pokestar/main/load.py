from pathlib import Path
from django.contrib.gis.utils import LayerMapping
from .models import Cities

Cities_mapping = {
    'name' : 'name',
    'adm0name' : 'adm0name',
    'geometry' : 'POINT',
}

Cities_shp = Path(__file__).resolve().parent / 'data' / 'cities.shp'

def run(verbose=True):
    lm = LayerMapping(Cities, Cities_shp, Cities_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)