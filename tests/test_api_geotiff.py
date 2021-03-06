import geoextent.lib.extent as geoextent
import pytest
from osgeo import gdal

@pytest.mark.skipif(gdal.__version__.startswith("2"), reason="coordinate order mismatch for old GDAL versions")
def test_geotiff_extract_bbox():
    result = geoextent.fromFile('tests/testdata/tif/wf_100m_klas.tif', bbox=True)
    assert "bbox" in result
    assert result["bbox"] == pytest.approx([50.310252, 5.9153008, 52.5307755, 9.4683987])

def test_geotiff_extract_time():
    result = geoextent.fromFile('tests/testdata/tif/wf_100m_klas.tif', bbox=True)
    assert "temporal_extent" not in result

def test_geotiff_crs_used():
    result = geoextent.fromFile('tests/testdata/tif/wf_100m_klas.tif', bbox=True)
    assert "crs" in result
    assert result["crs"] == '4326'
