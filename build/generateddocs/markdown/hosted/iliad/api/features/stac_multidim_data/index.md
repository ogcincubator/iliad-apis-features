
# STAC records with dcat mapping (Schema)

`ogc.hosted.iliad.api.features.stac_multidim_data` *v0.1*

Defines example records conformant to STAC and OGC Records API

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## Ocean Information Model Records profile

Currently a stub where requirements for OIM implementation can be defined as required.

Note specific profiles will define specific requirements for interaction with external systems.

The JSON-LD Context declares the default baseURI of Observation with generic STA context and OIM specific context.

TODO: (MVP)
1 - complete OIM mapping in the context files
2 - test with more cases

Note that it may have an externally resolvable URI or be a proxy handled by ILIAD (using the OGC RAINBOW)

## Examples

### Defines example records conformant to STAC and OGC Records API with CF data extracte
#### json
```json
{
    "bbox": [
      24.351858139038086,
      40.41341018676758,
      9.969209968386869e+36,
      9.969209968386869e+36
    ],
    "type": "Feature",
    "geometry": {
      "type": "Polygon",
      "coordinates": [
        [
          [
            24.351858139038086,
            40.41341018676758
          ],
          [
            24.351858139038086,
            9.969209968386869e+36
          ],
          [
            9.969209968386869e+36,
            9.969209968386869e+36
          ],
          [
            9.969209968386869e+36,
            40.41341018676758
          ],
          [
            24.351858139038086,
            40.41341018676758
          ]
        ]
      ]
    },
    "properties": {
      "title": "No Title",
      "description": "No Description",
      "datetime": [
        "2023-04-09T01:00:00Z"
      ],
      "created": "2024-10-03 10:22:35.026590+00:00",
      "updated": [
        "2024-10-03T10:59:34.887874Z"
      ],
      "start_datetime": "2023-04-09T01:00:00Z",
      "end_datetime": "2023-04-12T01:00:00.000Z",
      "license": "optional legal provisions under which this collection is made available. use links where available, preferably from SPDX register",
      "cube:dimensions": {
        "trajectory": {
          "type": "trajectory",
          "extent": [
            1,
            1000
          ],
          "unit": "1"
        },
        "time": {
          "type": "temporal",
          "extent": [
            "2023-04-09T01:00:00",
            "2023-04-12T01:00:00"
          ]
        }
      },
      "cube:variables": {
        "status": {
          "dimensions": [
            "trajectory",
            "time"
          ],
          "type": "data"
        },
        "moving": {
          "dimensions": [
            "trajectory",
            "time"
          ],
          "type": "data"
        },
        "age_seconds": {
          "dimensions": [
            "trajectory",
            "time"
          ],
          "type": "data",
          "unit": "s"
        },
        "origin_marker": {
          "dimensions": [
            "trajectory",
            "time"
          ],
          "type": "data"
        },
        "lon": {
          "dimensions": [
            "trajectory",
            "time"
          ],
          "type": "data",
          "unit": "degrees_east"
        },
        "lat": {
          "dimensions": [
            "trajectory",
            "time"
          ],
          "type": "data",
          "unit": "degrees_north"
        },
        "z": {
          "dimensions": [
            "trajectory",
            "time"
          ],
          "type": "data",
          "unit": "m"
        },
        "wind_drift_factor": {
          "dimensions": [
            "trajectory",
            "time"
          ],
          "type": "data",
          "unit": "%"
        },
        "current_drift_factor": {
          "dimensions": [
            "trajectory",
            "time"
          ],
          "type": "data",
          "unit": "1"
        },
        "terminal_velocity": {
          "dimensions": [
            "trajectory",
            "time"
          ],
          "type": "data",
          "unit": "m/s"
        },
        "mass_oil": {
          "dimensions": [
            "trajectory",
            "time"
          ],
          "type": "data",
          "unit": "kg"
        },
        "viscosity": {
          "dimensions": [
            "trajectory",
            "time"
          ],
          "type": "data",
          "unit": "m2/s"
        },
        "density": {
          "dimensions": [
            "trajectory",
            "time"
          ],
          "type": "data",
          "unit": "kg/m^3"
        },
        "bulltime": {
          "dimensions": [
            "trajectory",
            "time"
          ],
          "type": "data",
          "unit": "s"
        },
        "interfacial_area": {
          "dimensions": [
            "trajectory",
            "time"
          ],
          "type": "data",
          "unit": "m2"
        },
        "mass_dispersed": {
          "dimensions": [
            "trajectory",
            "time"
          ],
          "type": "data",
          "unit": "kg"
        },
        "mass_evaporated": {
          "dimensions": [
            "trajectory",
            "time"
          ],
          "type": "data",
          "unit": "kg"
        },
        "mass_biodegraded": {
          "dimensions": [
            "trajectory",
            "time"
          ],
          "type": "data",
          "unit": "kg"
        },
        "fraction_evaporated": {
          "dimensions": [
            "trajectory",
            "time"
          ],
          "type": "data",
          "unit": "%"
        },
        "water_fraction": {
          "dimensions": [
            "trajectory",
            "time"
          ],
          "type": "data",
          "unit": "%"
        },
        "oil_film_thickness": {
          "dimensions": [
            "trajectory",
            "time"
          ],
          "type": "data",
          "unit": "m"
        },
        "diameter": {
          "dimensions": [
            "trajectory",
            "time"
          ],
          "type": "data",
          "unit": "m"
        },
        "x_sea_water_velocity": {
          "dimensions": [
            "trajectory",
            "time"
          ],
          "type": "data"
        },
        "y_sea_water_velocity": {
          "dimensions": [
            "trajectory",
            "time"
          ],
          "type": "data"
        },
        "x_wind": {
          "dimensions": [
            "trajectory",
            "time"
          ],
          "type": "data"
        },
        "y_wind": {
          "dimensions": [
            "trajectory",
            "time"
          ],
          "type": "data"
        },
        "upward_sea_water_velocity": {
          "dimensions": [
            "trajectory",
            "time"
          ],
          "type": "data"
        },
        "sea_surface_wave_significant_height": {
          "dimensions": [
            "trajectory",
            "time"
          ],
          "type": "data"
        },
        "sea_surface_wave_stokes_drift_x_velocity": {
          "dimensions": [
            "trajectory",
            "time"
          ],
          "type": "data"
        },
        "sea_surface_wave_stokes_drift_y_velocity": {
          "dimensions": [
            "trajectory",
            "time"
          ],
          "type": "data"
        },
        "sea_surface_wave_period_at_variance_spectral_density_maximum": {
          "dimensions": [
            "trajectory",
            "time"
          ],
          "type": "data"
        },
        "sea_surface_wave_mean_period_from_variance_spectral_density_second_frequency_moment": {
          "dimensions": [
            "trajectory",
            "time"
          ],
          "type": "data"
        },
        "sea_ice_area_fraction": {
          "dimensions": [
            "trajectory",
            "time"
          ],
          "type": "data"
        },
        "sea_ice_x_velocity": {
          "dimensions": [
            "trajectory",
            "time"
          ],
          "type": "data"
        },
        "sea_ice_y_velocity": {
          "dimensions": [
            "trajectory",
            "time"
          ],
          "type": "data"
        },
        "sea_water_temperature": {
          "dimensions": [
            "trajectory",
            "time"
          ],
          "type": "data"
        },
        "sea_water_salinity": {
          "dimensions": [
            "trajectory",
            "time"
          ],
          "type": "data"
        },
        "sea_floor_depth_below_sea_level": {
          "dimensions": [
            "trajectory",
            "time"
          ],
          "type": "data"
        },
        "ocean_vertical_diffusivity": {
          "dimensions": [
            "trajectory",
            "time"
          ],
          "type": "data"
        },
        "land_binary_mask": {
          "dimensions": [
            "trajectory",
            "time"
          ],
          "type": "data"
        },
        "ocean_mixed_layer_thickness": {
          "dimensions": [
            "trajectory",
            "time"
          ],
          "type": "data"
        }
      },
      "themes": [
        {
          "concepts": [
            {
              "id": "12301",
              "name": "water resources management"
            },
            {
              "id": "water_resources_management",
              "url": "http://www.eionet.europa.eu/gemet/concept/12301"
            }
          ],
          "scheme": "http://www.eionet.europa.eu/gemet/concept/"
        },
        {
          "concepts": [
            {
              "id": "water_quality"
            }
          ],
          "scheme": "http://mmisw.org/ont/ioos/category"
        }
      ],
      "keywords": [
        "water",
        "ozoother keyword"
      ],
      "wasGeneratedBy": {
        "provType": "Activity",
        "id": "surveys:DP-1-S1",
        "activityType": "InitialSurvey",
        "endedAtTime": "2023-10-05T05:03:15+01:00",
        "wasAssociatedWith": "staff:jd234",
        "used": {
          "id": "regulations:Act3",
          "entityType": "Legislation",
          "wasAttributedTo": "agents:someGovernment",
          "links": [
            {
              "href": "https://some.gov/linktoact/",
              "rel": "related"
            }
          ]
        }
      },
      "contacts": [
        {
          "name": "name of the contact, name or organisation is required or both, all the other fields are optiopnal. Roles can be defined on the contact or phones|emails|addresses level",
          "organization": "name of the organisation, name or organisation is required or both, all the other fields are optional. schema https://github.com/opengeospatial/ogcapi-records/blob/master/core/openapi/schemas/contact.yaml",
          "identifier": " optional identifier of the contact",
          "position": "optional position of the contact",
          "logo": {
            "href": "https://example.com/logo.png",
            "rel": "icon",
            "type": "image/png",
            "description": "descritpion is not required here just for a not in the example: link shall have rel=icon and type shall be image"
          },
          "links": [
            {
              "href": "https://woudc.org",
              "rel": "about",
              "type": "text/html"
            }
          ],
          "phones": [
            {
              "value": "+99123456983123",
              "role": "contactPoint"
            }
          ],
          "emails": [
            {
              "value": "jsmith@example.com",
              "role": "rightsHolder"
            }
          ],
          "addresses": [
            {
              "deliveryPoint": [
                "optional detailed address"
              ],
              "city": "optional city",
              "administrativeArea": "optional administrativeArea",
              "postalCode": "optional postalCode",
              "country": "optional country"
            }
          ],
          "contactInstructions": "SEE PAGE: https://woudc.org/contact.php",
          "roles": [
            "contactPoint",
            "rightsHolder",
            "pubisher",
            "creator",
            "distributor",
            "originator",
            "principalInvestigator",
            "processor",
            "resourceProvider",
            "u"
          ]
        }
      ],
      "rights": "optional statement that concerns all rights not addressed by the license such as a copyright statement; string defining access rights inline or as URL",
      "applicableLegislation": "string defining applicable legislation inline or as URL, use wasGeneratedBy.used for cases whereever you can assign quality measure to particular processing step",
      "convention": "CF-1.6",
      "version": "optional resource behind the record version string",
      "deprecated": false,
      "latest-version": "optional link to the record with latest version",
      "predecessor-version": "optional link to the record with previous version",
      "successor-version": "optional link to the record with next version",
      "cf:parameter": [
        {
          "name": "sea_water_salinity",
          "schema": "http://vocab.nerc.ac.uk/standard_name/",
          "unit": "https://qudt.org/2.1/vocab/unit/GM-PER-KiloGM"
        }
      ],
      "dqv:hasQualityMeasurement": "optional description of the quality measures used to generate the content, use wasGeneratedBy.used for cases whereever you can assign quality measure to particular processing step",
      "dqv:hasQualityMetadata": "optional quality metadata as string or object (with structure TBD)"
    },
    "id": "simulation",
    "stac_version": "1.1.0",
    "assets": {
      "data": {
        "href": "~/Downloads/simulation.nc",
        "title": "NetCDF Data",
        "media_type": "application/x-netcdf"
      }
    },
    "links": [
      {
        "href": "tests/simulation/simulation.json",
        "rel": "self",
        "title": "optional link to this record"
      },
      {
        "href": "~/Downloads/simulation.nc",
        "rel": "enclosure",
        "type": "application/x-hdf",
        "title": "optional raw file"
      },
      {
        "href": "~/Downloads/simulation.nc",
        "rel": "preview",
        "type": "image/png",
        "title": "optional thumbnail image preview"
      },
      {
        "href": "tests/simulation/simulation.zip",
        "rel": "sample",
        "type": "application/x-hdf",
        "title": "optional link to the sample data, either one enclosure or service is required in Iliad profile"
      },
      {
        "href": "tests/simulation/simulation.zip",
        "rel": "sample",
        "type": "application/x-hdf",
        "title": "link to the data, either one enclosure or service is required in Iliad profile"
      },
      {
        "href": "https://cfconventions.org/Data/cf-conventions/cf-conventions-1.11/cf-conventions.pdf",
        "rel": "conformance",
        "type": "text/html",
        "title": "link to the resource confirmance speficication"
      },
      {
        "href": "https://example.com/ows/wms",
        "rel": "service",
        "type": "application/xml",
        "title": "optional link to the web service (not raw file) like OGC Web Map Service (WMS) either one enclosure or service is required in Iliad profile"
      },
      {
        "href": "https://example.com/license",
        "rel": "license",
        "type": "text/html",
        "title": "optional link to the license"
      },
      {
        "href": "https://example.com/next_data_record",
        "rel": "next",
        "type": "text/html",
        "title": "optional link to the next in the serie"
      },
      {
        "href": "https://example.com/prev_data_record",
        "rel": "prev",
        "type": "text/html",
        "title": "optional link to the previous in the serie"
      },
      {
        "href": "https://example.com/prev_data_record",
        "rel": "parent",
        "type": "text/html",
        "title": "optional link to the parent if data in series or other parent in the hierarchy"
      }
    ],
    "stac_extensions": [
      "https://stac-extensions.github.io/datacube/v2.2.0/schema.json",
      "https://stac-extensions.github.io/themes/v1.0.0/schema.json",
      "https://stac-extensions.github.io/cf/v0.2.0/schema.json",
      "https://stac-extensions.github.io/contacts/v0.1.1/schema.json",
      "https://stac-extensions.github.io/version/v1.2.0/schema.json",
      "https://stac-extensions.github.io/processing/v1.2.0/schema.json"
    ],
    "time": {
      "interval": [
        "2023-04-09 01:00:00+00:00",
        "2023-04-12 01:00:00+00:00"
      ],
      "resolution": "P1D"
    },
    "crs": "EPSG:4326",
    "conformsTo": [
      "https://ogcincubator.github.io/geodcat-ogcapi-records/bblock/ogc.geo.geodcat.geodcat-stac-eo/",
      "https://ogcincubator.github.io/iliad-apis-features/bblock/ogc.hosted.iliad.api.stac_record",
      "https://stac-extensions.github.io/datacube/v2.2.0/schema.json",
      "https://stac-extensions.github.io/datacube/v2.2.0/schema.json",
      "https://stac-extensions.github.io/themes/v1.0.0/schema.json",
      "https://stac-extensions.github.io/cf/v0.2.0/schema.json",
      "https://stac-extensions.github.io/contacts/v0.1.1/schema.json",
      "https://stac-extensions.github.io/version/v1.2.0/schema.json",
      "https://stac-extensions.github.io/processing/v1.2.0/schema.json"
    ]
  }
```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/iliad-apis-features/build/annotated/hosted/iliad/api/features/stac_multidim_data/context.jsonld",
  "bbox": [
    24.351858139038086,
    40.41341018676758,
    9.969209968386869e+36,
    9.969209968386869e+36
  ],
  "type": "Feature",
  "geometry": {
    "type": "Polygon",
    "coordinates": [
      [
        [
          24.351858139038086,
          40.41341018676758
        ],
        [
          24.351858139038086,
          9.969209968386869e+36
        ],
        [
          9.969209968386869e+36,
          9.969209968386869e+36
        ],
        [
          9.969209968386869e+36,
          40.41341018676758
        ],
        [
          24.351858139038086,
          40.41341018676758
        ]
      ]
    ]
  },
  "properties": {
    "title": "No Title",
    "description": "No Description",
    "datetime": [
      "2023-04-09T01:00:00Z"
    ],
    "created": "2024-10-03 10:22:35.026590+00:00",
    "updated": [
      "2024-10-03T10:59:34.887874Z"
    ],
    "start_datetime": "2023-04-09T01:00:00Z",
    "end_datetime": "2023-04-12T01:00:00.000Z",
    "license": "optional legal provisions under which this collection is made available. use links where available, preferably from SPDX register",
    "cube:dimensions": {
      "trajectory": {
        "type": "trajectory",
        "extent": [
          1,
          1000
        ],
        "unit": "1"
      },
      "time": {
        "type": "temporal",
        "extent": [
          "2023-04-09T01:00:00",
          "2023-04-12T01:00:00"
        ]
      }
    },
    "cube:variables": {
      "status": {
        "dimensions": [
          "trajectory",
          "time"
        ],
        "type": "data"
      },
      "moving": {
        "dimensions": [
          "trajectory",
          "time"
        ],
        "type": "data"
      },
      "age_seconds": {
        "dimensions": [
          "trajectory",
          "time"
        ],
        "type": "data",
        "unit": "s"
      },
      "origin_marker": {
        "dimensions": [
          "trajectory",
          "time"
        ],
        "type": "data"
      },
      "lon": {
        "dimensions": [
          "trajectory",
          "time"
        ],
        "type": "data",
        "unit": "degrees_east"
      },
      "lat": {
        "dimensions": [
          "trajectory",
          "time"
        ],
        "type": "data",
        "unit": "degrees_north"
      },
      "z": {
        "dimensions": [
          "trajectory",
          "time"
        ],
        "type": "data",
        "unit": "m"
      },
      "wind_drift_factor": {
        "dimensions": [
          "trajectory",
          "time"
        ],
        "type": "data",
        "unit": "%"
      },
      "current_drift_factor": {
        "dimensions": [
          "trajectory",
          "time"
        ],
        "type": "data",
        "unit": "1"
      },
      "terminal_velocity": {
        "dimensions": [
          "trajectory",
          "time"
        ],
        "type": "data",
        "unit": "m/s"
      },
      "mass_oil": {
        "dimensions": [
          "trajectory",
          "time"
        ],
        "type": "data",
        "unit": "kg"
      },
      "viscosity": {
        "dimensions": [
          "trajectory",
          "time"
        ],
        "type": "data",
        "unit": "m2/s"
      },
      "density": {
        "dimensions": [
          "trajectory",
          "time"
        ],
        "type": "data",
        "unit": "kg/m^3"
      },
      "bulltime": {
        "dimensions": [
          "trajectory",
          "time"
        ],
        "type": "data",
        "unit": "s"
      },
      "interfacial_area": {
        "dimensions": [
          "trajectory",
          "time"
        ],
        "type": "data",
        "unit": "m2"
      },
      "mass_dispersed": {
        "dimensions": [
          "trajectory",
          "time"
        ],
        "type": "data",
        "unit": "kg"
      },
      "mass_evaporated": {
        "dimensions": [
          "trajectory",
          "time"
        ],
        "type": "data",
        "unit": "kg"
      },
      "mass_biodegraded": {
        "dimensions": [
          "trajectory",
          "time"
        ],
        "type": "data",
        "unit": "kg"
      },
      "fraction_evaporated": {
        "dimensions": [
          "trajectory",
          "time"
        ],
        "type": "data",
        "unit": "%"
      },
      "water_fraction": {
        "dimensions": [
          "trajectory",
          "time"
        ],
        "type": "data",
        "unit": "%"
      },
      "oil_film_thickness": {
        "dimensions": [
          "trajectory",
          "time"
        ],
        "type": "data",
        "unit": "m"
      },
      "diameter": {
        "dimensions": [
          "trajectory",
          "time"
        ],
        "type": "data",
        "unit": "m"
      },
      "x_sea_water_velocity": {
        "dimensions": [
          "trajectory",
          "time"
        ],
        "type": "data"
      },
      "y_sea_water_velocity": {
        "dimensions": [
          "trajectory",
          "time"
        ],
        "type": "data"
      },
      "x_wind": {
        "dimensions": [
          "trajectory",
          "time"
        ],
        "type": "data"
      },
      "y_wind": {
        "dimensions": [
          "trajectory",
          "time"
        ],
        "type": "data"
      },
      "upward_sea_water_velocity": {
        "dimensions": [
          "trajectory",
          "time"
        ],
        "type": "data"
      },
      "sea_surface_wave_significant_height": {
        "dimensions": [
          "trajectory",
          "time"
        ],
        "type": "data"
      },
      "sea_surface_wave_stokes_drift_x_velocity": {
        "dimensions": [
          "trajectory",
          "time"
        ],
        "type": "data"
      },
      "sea_surface_wave_stokes_drift_y_velocity": {
        "dimensions": [
          "trajectory",
          "time"
        ],
        "type": "data"
      },
      "sea_surface_wave_period_at_variance_spectral_density_maximum": {
        "dimensions": [
          "trajectory",
          "time"
        ],
        "type": "data"
      },
      "sea_surface_wave_mean_period_from_variance_spectral_density_second_frequency_moment": {
        "dimensions": [
          "trajectory",
          "time"
        ],
        "type": "data"
      },
      "sea_ice_area_fraction": {
        "dimensions": [
          "trajectory",
          "time"
        ],
        "type": "data"
      },
      "sea_ice_x_velocity": {
        "dimensions": [
          "trajectory",
          "time"
        ],
        "type": "data"
      },
      "sea_ice_y_velocity": {
        "dimensions": [
          "trajectory",
          "time"
        ],
        "type": "data"
      },
      "sea_water_temperature": {
        "dimensions": [
          "trajectory",
          "time"
        ],
        "type": "data"
      },
      "sea_water_salinity": {
        "dimensions": [
          "trajectory",
          "time"
        ],
        "type": "data"
      },
      "sea_floor_depth_below_sea_level": {
        "dimensions": [
          "trajectory",
          "time"
        ],
        "type": "data"
      },
      "ocean_vertical_diffusivity": {
        "dimensions": [
          "trajectory",
          "time"
        ],
        "type": "data"
      },
      "land_binary_mask": {
        "dimensions": [
          "trajectory",
          "time"
        ],
        "type": "data"
      },
      "ocean_mixed_layer_thickness": {
        "dimensions": [
          "trajectory",
          "time"
        ],
        "type": "data"
      }
    },
    "themes": [
      {
        "concepts": [
          {
            "id": "12301",
            "name": "water resources management"
          },
          {
            "id": "water_resources_management",
            "url": "http://www.eionet.europa.eu/gemet/concept/12301"
          }
        ],
        "scheme": "http://www.eionet.europa.eu/gemet/concept/"
      },
      {
        "concepts": [
          {
            "id": "water_quality"
          }
        ],
        "scheme": "http://mmisw.org/ont/ioos/category"
      }
    ],
    "keywords": [
      "water",
      "ozoother keyword"
    ],
    "wasGeneratedBy": {
      "provType": "Activity",
      "id": "surveys:DP-1-S1",
      "activityType": "InitialSurvey",
      "endedAtTime": "2023-10-05T05:03:15+01:00",
      "wasAssociatedWith": "staff:jd234",
      "used": {
        "id": "regulations:Act3",
        "entityType": "Legislation",
        "wasAttributedTo": "agents:someGovernment",
        "links": [
          {
            "href": "https://some.gov/linktoact/",
            "rel": "related"
          }
        ]
      }
    },
    "contacts": [
      {
        "name": "name of the contact, name or organisation is required or both, all the other fields are optiopnal. Roles can be defined on the contact or phones|emails|addresses level",
        "organization": "name of the organisation, name or organisation is required or both, all the other fields are optional. schema https://github.com/opengeospatial/ogcapi-records/blob/master/core/openapi/schemas/contact.yaml",
        "identifier": " optional identifier of the contact",
        "position": "optional position of the contact",
        "logo": {
          "href": "https://example.com/logo.png",
          "rel": "icon",
          "type": "image/png",
          "description": "descritpion is not required here just for a not in the example: link shall have rel=icon and type shall be image"
        },
        "links": [
          {
            "href": "https://woudc.org",
            "rel": "about",
            "type": "text/html"
          }
        ],
        "phones": [
          {
            "value": "+99123456983123",
            "role": "contactPoint"
          }
        ],
        "emails": [
          {
            "value": "jsmith@example.com",
            "role": "rightsHolder"
          }
        ],
        "addresses": [
          {
            "deliveryPoint": [
              "optional detailed address"
            ],
            "city": "optional city",
            "administrativeArea": "optional administrativeArea",
            "postalCode": "optional postalCode",
            "country": "optional country"
          }
        ],
        "contactInstructions": "SEE PAGE: https://woudc.org/contact.php",
        "roles": [
          "contactPoint",
          "rightsHolder",
          "pubisher",
          "creator",
          "distributor",
          "originator",
          "principalInvestigator",
          "processor",
          "resourceProvider",
          "u"
        ]
      }
    ],
    "rights": "optional statement that concerns all rights not addressed by the license such as a copyright statement; string defining access rights inline or as URL",
    "applicableLegislation": "string defining applicable legislation inline or as URL, use wasGeneratedBy.used for cases whereever you can assign quality measure to particular processing step",
    "convention": "CF-1.6",
    "version": "optional resource behind the record version string",
    "deprecated": false,
    "latest-version": "optional link to the record with latest version",
    "predecessor-version": "optional link to the record with previous version",
    "successor-version": "optional link to the record with next version",
    "cf:parameter": [
      {
        "name": "sea_water_salinity",
        "schema": "http://vocab.nerc.ac.uk/standard_name/",
        "unit": "https://qudt.org/2.1/vocab/unit/GM-PER-KiloGM"
      }
    ],
    "dqv:hasQualityMeasurement": "optional description of the quality measures used to generate the content, use wasGeneratedBy.used for cases whereever you can assign quality measure to particular processing step",
    "dqv:hasQualityMetadata": "optional quality metadata as string or object (with structure TBD)"
  },
  "id": "simulation",
  "stac_version": "1.1.0",
  "assets": {
    "data": {
      "href": "~/Downloads/simulation.nc",
      "title": "NetCDF Data",
      "media_type": "application/x-netcdf"
    }
  },
  "links": [
    {
      "href": "tests/simulation/simulation.json",
      "rel": "self",
      "title": "optional link to this record"
    },
    {
      "href": "~/Downloads/simulation.nc",
      "rel": "enclosure",
      "type": "application/x-hdf",
      "title": "optional raw file"
    },
    {
      "href": "~/Downloads/simulation.nc",
      "rel": "preview",
      "type": "image/png",
      "title": "optional thumbnail image preview"
    },
    {
      "href": "tests/simulation/simulation.zip",
      "rel": "sample",
      "type": "application/x-hdf",
      "title": "optional link to the sample data, either one enclosure or service is required in Iliad profile"
    },
    {
      "href": "tests/simulation/simulation.zip",
      "rel": "sample",
      "type": "application/x-hdf",
      "title": "link to the data, either one enclosure or service is required in Iliad profile"
    },
    {
      "href": "https://cfconventions.org/Data/cf-conventions/cf-conventions-1.11/cf-conventions.pdf",
      "rel": "conformance",
      "type": "text/html",
      "title": "link to the resource confirmance speficication"
    },
    {
      "href": "https://example.com/ows/wms",
      "rel": "service",
      "type": "application/xml",
      "title": "optional link to the web service (not raw file) like OGC Web Map Service (WMS) either one enclosure or service is required in Iliad profile"
    },
    {
      "href": "https://example.com/license",
      "rel": "license",
      "type": "text/html",
      "title": "optional link to the license"
    },
    {
      "href": "https://example.com/next_data_record",
      "rel": "next",
      "type": "text/html",
      "title": "optional link to the next in the serie"
    },
    {
      "href": "https://example.com/prev_data_record",
      "rel": "prev",
      "type": "text/html",
      "title": "optional link to the previous in the serie"
    },
    {
      "href": "https://example.com/prev_data_record",
      "rel": "parent",
      "type": "text/html",
      "title": "optional link to the parent if data in series or other parent in the hierarchy"
    }
  ],
  "stac_extensions": [
    "https://stac-extensions.github.io/datacube/v2.2.0/schema.json",
    "https://stac-extensions.github.io/themes/v1.0.0/schema.json",
    "https://stac-extensions.github.io/cf/v0.2.0/schema.json",
    "https://stac-extensions.github.io/contacts/v0.1.1/schema.json",
    "https://stac-extensions.github.io/version/v1.2.0/schema.json",
    "https://stac-extensions.github.io/processing/v1.2.0/schema.json"
  ],
  "time": {
    "interval": [
      "2023-04-09 01:00:00+00:00",
      "2023-04-12 01:00:00+00:00"
    ],
    "resolution": "P1D"
  },
  "crs": "EPSG:4326",
  "conformsTo": [
    "https://ogcincubator.github.io/geodcat-ogcapi-records/bblock/ogc.geo.geodcat.geodcat-stac-eo/",
    "https://ogcincubator.github.io/iliad-apis-features/bblock/ogc.hosted.iliad.api.stac_record",
    "https://stac-extensions.github.io/datacube/v2.2.0/schema.json",
    "https://stac-extensions.github.io/datacube/v2.2.0/schema.json",
    "https://stac-extensions.github.io/themes/v1.0.0/schema.json",
    "https://stac-extensions.github.io/cf/v0.2.0/schema.json",
    "https://stac-extensions.github.io/contacts/v0.1.1/schema.json",
    "https://stac-extensions.github.io/version/v1.2.0/schema.json",
    "https://stac-extensions.github.io/processing/v1.2.0/schema.json"
  ]
}
```

#### ttl
```ttl
@prefix dcat: <http://www.w3.org/ns/dcat#> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix geojson: <https://purl.org/geojson/vocab#> .
@prefix ns1: <http://www.iana.org/assignments/> .
@prefix ns2: <http://www.opengis.net/swe/2.0/> .
@prefix ns3: <cube:> .
@prefix ns4: <http://qudt.org/schema/qudt/> .
@prefix ns5: <cf:> .
@prefix ns6: <dqv:> .
@prefix ns7: <http://www.w3.org/2003/01/geo/wgs84_pos#> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix rec: <https://www.opengis.net/def/ogc-api/records/> .
@prefix time: <http://www.w3.org/2006/time#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<http://w3id.org/ogcincubator/simulation> a geojson:Feature ;
    rdfs:label "No Title" ;
    ns5:parameter [ ns4:unit <https://qudt.org/2.1/vocab/unit/GM-PER-KiloGM> ;
            ns2:name "sea_water_salinity"^^xsd:string ] ;
    ns3:dimensions [ dcterms:temporal [ a dcterms:temporal ] ] ;
    ns3:variables [ ns7:lat [ a <http://w3id.org/ogcincubator/data> ;
                    ns4:unit <http://w3id.org/ogcincubator/degrees_north> ] ] ;
    ns6:hasQualityMeasurement "optional description of the quality measures used to generate the content, use wasGeneratedBy.used for cases whereever you can assign quality measure to particular processing step" ;
    ns6:hasQualityMetadata "optional quality metadata as string or object (with structure TBD)" ;
    dcterms:conformsTo <https://ogcincubator.github.io/geodcat-ogcapi-records/bblock/ogc.geo.geodcat.geodcat-stac-eo/>,
        <https://ogcincubator.github.io/iliad-apis-features/bblock/ogc.hosted.iliad.api.stac_record>,
        <https://stac-extensions.github.io/cf/v0.2.0/schema.json>,
        <https://stac-extensions.github.io/contacts/v0.1.1/schema.json>,
        <https://stac-extensions.github.io/datacube/v2.2.0/schema.json>,
        <https://stac-extensions.github.io/processing/v1.2.0/schema.json>,
        <https://stac-extensions.github.io/themes/v1.0.0/schema.json>,
        <https://stac-extensions.github.io/version/v1.2.0/schema.json> ;
    dcterms:created "2024-10-03 10:22:35.026590+00:00" ;
    dcterms:description "No Description" ;
    dcterms:modified "2024-10-03T10:59:34.887874Z" ;
    dcterms:temporal [ time:hasTime ( "2023-04-09 01:00:00+00:00" "2023-04-12 01:00:00+00:00" ) ;
            rec:iso8601period "P1D" ] ;
    rdfs:seeAlso [ rdfs:label "optional link to this record" ;
            ns1:relation <http://www.iana.org/assignments/relation/self> ;
            oa:hasTarget <http://w3id.org/ogcincubator/tests/simulation/simulation.json> ],
        [ rdfs:label "optional link to the web service (not raw file) like OGC Web Map Service (WMS) either one enclosure or service is required in Iliad profile" ;
            dcterms:type "application/xml" ;
            ns1:relation <http://www.iana.org/assignments/relation/service> ;
            oa:hasTarget <https://example.com/ows/wms> ],
        [ rdfs:label "link to the data, either one enclosure or service is required in Iliad profile" ;
            dcterms:type "application/x-hdf" ;
            ns1:relation <http://www.iana.org/assignments/relation/sample> ;
            oa:hasTarget <http://w3id.org/ogcincubator/tests/simulation/simulation.zip> ],
        [ rdfs:label "optional link to the license" ;
            dcterms:type "text/html" ;
            ns1:relation <http://www.iana.org/assignments/relation/license> ;
            oa:hasTarget <https://example.com/license> ],
        [ rdfs:label "optional raw file" ;
            dcterms:type "application/x-hdf" ;
            ns1:relation <http://www.iana.org/assignments/relation/enclosure> ;
            oa:hasTarget <http://w3id.org/ogcincubator/~/Downloads/simulation.nc> ],
        [ rdfs:label "optional link to the next in the serie" ;
            dcterms:type "text/html" ;
            ns1:relation <http://www.iana.org/assignments/relation/next> ;
            oa:hasTarget <https://example.com/next_data_record> ],
        [ rdfs:label "optional thumbnail image preview" ;
            dcterms:type "image/png" ;
            ns1:relation <http://www.iana.org/assignments/relation/preview> ;
            oa:hasTarget <http://w3id.org/ogcincubator/~/Downloads/simulation.nc> ],
        [ rdfs:label "optional link to the previous in the serie" ;
            dcterms:type "text/html" ;
            ns1:relation <http://www.iana.org/assignments/relation/prev> ;
            oa:hasTarget <https://example.com/prev_data_record> ],
        [ rdfs:label "optional link to the parent if data in series or other parent in the hierarchy" ;
            dcterms:type "text/html" ;
            ns1:relation <http://www.iana.org/assignments/relation/parent> ;
            oa:hasTarget <https://example.com/prev_data_record> ],
        [ rdfs:label "optional link to the sample data, either one enclosure or service is required in Iliad profile" ;
            dcterms:type "application/x-hdf" ;
            ns1:relation <http://www.iana.org/assignments/relation/sample> ;
            oa:hasTarget <http://w3id.org/ogcincubator/tests/simulation/simulation.zip> ],
        [ rdfs:label "link to the resource confirmance speficication" ;
            dcterms:type "text/html" ;
            ns1:relation <http://www.iana.org/assignments/relation/conformance> ;
            oa:hasTarget <https://cfconventions.org/Data/cf-conventions/cf-conventions-1.11/cf-conventions.pdf> ] ;
    owl:deprecated false ;
    dcat:contactPoint [ dcterms:identifier " optional identifier of the contact" ;
            ns2:name "name of the contact, name or organisation is required or both, all the other fields are optiopnal. Roles can be defined on the contact or phones|emails|addresses level"^^xsd:string ;
            rdfs:seeAlso [ dcterms:type "text/html" ;
                    ns1:relation <http://www.iana.org/assignments/relation/about> ;
                    oa:hasTarget <https://woudc.org> ] ] ;
    dcat:keyword "ozoother keyword",
        "water" ;
    dcat:license "optional legal provisions under which this collection is made available. use links where available, preferably from SPDX register" ;
    dcat:rights "optional statement that concerns all rights not addressed by the license such as a copyright statement; string defining access rights inline or as URL" ;
    geojson:bbox ( 2.435186e+01 4.041341e+01 9.96921e+36 9.96921e+36 ) ;
    geojson:geometry [ a geojson:Polygon ;
            geojson:coordinates ( ( ( 2.435186e+01 4.041341e+01 ) ( 2.435186e+01 9.96921e+36 ) ( 9.96921e+36 9.96921e+36 ) ( 9.96921e+36 4.041341e+01 ) ( 2.435186e+01 4.041341e+01 ) ) ) ] ;
    rec:themes [ rec:concept [ rec:conceptID "water_resources_management"^^xsd:string ],
                [ ns2:name "water resources management"^^xsd:string ;
                    rec:conceptID "12301"^^xsd:string ] ;
            rec:scheme "http://www.eionet.europa.eu/gemet/concept/" ],
        [ rec:concept [ rec:conceptID "water_quality"^^xsd:string ] ;
            rec:scheme "http://mmisw.org/ont/ioos/category" ] .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: A OIM aligned Records schema
description: Component of Records conformant with STAC. no particular added constraints
  are added for selected extensions
$ref: https://ogcincubator.github.io/geodcat-ogcapi-records/build/annotated/geo/geodcat/dcat-records/schema.json
x-jsonld-extra-terms:
  IndexAxisType: http://www.opengis.net/cis/1.1/IndexAxisType
  spatial: http://purl.org/dc/terms/spatial
  previewInfo:
    x-jsonld-id: https://w3id.org/iliad/oim/metadata/previewInfo
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#string
  coverage:
    x-jsonld-id: http://www.opengis.net/cis/1.1/coverage
    x-jsonld-type: '@id'
  VideoResource: https://w3id.org/idsa/core/VideoResource
  DigitalContent: https://w3id.org/idsa/core/DigitalContent
  affiliation: https://schema.org/affiliation
  endpointArtifact:
    x-jsonld-id: https://w3id.org/idsa/core/endpointArtifact
    x-jsonld-type: '@id'
  versionInfo: http://www.w3.org/2002/07/owl#versionInfo
  created: http://purl.org/dc/terms/created
  VDataBlockType: http://www.opengis.net/cis/1.1/VDataBlockType
  ImageRepresentation: https://w3id.org/idsa/core/ImageRepresentation
  lowerBound:
    x-jsonld-id: http://www.opengis.net/cis/1.1/lowerBound
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#integer
  Dataset: http://www.w3.org/ns/dcat#Dataset
  EnvelopeByAxisType: http://www.opengis.net/cis/1.1/EnvelopeByAxisType
  width:
    x-jsonld-id: https://w3id.org/idsa/core/width
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#decimal
  license: http://www.w3.org/ns/dcat#license
  Representation: https://w3id.org/idsa/core/Representation
  accrualPeriodicity:
    x-jsonld-id: https://w3id.org/idsa/core/accrualPeriodicity
    x-jsonld-type: '@id'
  model:
    x-jsonld-id: http://www.opengis.net/cis/1.1/model
    x-jsonld-type: '@id'
  MediaType: http://purl.org/dc/terms/MediaType
  Distribution: http://www.w3.org/ns/dcat#Distribution
  dataset:
    x-jsonld-id: http://www.w3.org/ns/dcat#dataset
    x-jsonld-type: '@id'
  AudioRepresentation: https://w3id.org/idsa/core/AudioRepresentation
  usageNote: http://purl.org/vocab/vann/usageNote
  AxisExtendType: http://www.opengis.net/cis/1.1/AxisExtendType
  height:
    x-jsonld-id: https://w3id.org/idsa/core/height
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#decimal
  hasQualityMetadata:
    x-jsonld-id: http://www.w3.org/ns/dqv#hasQualityMetadata
    x-jsonld-type: '@id'
  coordinate:
    x-jsonld-id: http://www.opengis.net/cis/1.1/coordinate
    x-jsonld-type: '@id'
  frameRate:
    x-jsonld-id: https://w3id.org/idsa/core/frameRate
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#decimal
  QualityMetadata: http://www.w3.org/ns/dqv#QualityMetadata
  GridLimitsType: http://www.opengis.net/cis/1.1/GridLimitsType
  temporalResolution: http://www.w3.org/ns/dcat#temporalResolution
  VideoRepresentation: https://w3id.org/idsa/core/VideoRepresentation
  maker: http://xmlns.com/foaf/0.1/maker
  fileReference: http://www.opengis.net/cis/1.1/fileReference
  DataRepresentation: https://w3id.org/idsa/core/DataRepresentation
  sensorInstanceRef:
    x-jsonld-id: http://www.sensorml.com/sensorML-2.0/sensorInstanceRef
    x-jsonld-type: '@id'
  generalGrid:
    x-jsonld-id: http://www.opengis.net/cis/1.1/generalGrid
    x-jsonld-type: '@id'
  label: http://www.w3.org/2000/01/rdf-schema#label
  positionValuePair:
    x-jsonld-id: http://www.opengis.net/cis/1.1/positionValuePair
    x-jsonld-type: '@id'
  PVPType: http://www.opengis.net/cis/1.1/PVPType
  scaleFactor:
    x-jsonld-id: https://w3id.org/iliad/oim/metadata/scaleFactor
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#float
  AllowedValues: http://www.opengis.net/swe/2.0/AllowedValues
  project: https://w3id.org/iliad/oim/metadata/project
  gridLimits:
    x-jsonld-id: http://www.opengis.net/cis/1.1/gridLimits
    x-jsonld-type: '@id'
  TextRepresentation: https://w3id.org/idsa/core/TextRepresentation
  TextResource: https://w3id.org/idsa/core/TextResource
  DataResource: https://w3id.org/idsa/core/DataResource
  rangeSet:
    x-jsonld-id: http://www.opengis.net/cis/1.1/rangeSet
    x-jsonld-type: '@id'
  Location: https://w3id.org/idsa/core/Location
  rangeType:
    x-jsonld-id: http://www.opengis.net/cis/1.1/rangeType
    x-jsonld-type: '@id'
  axisLabels:
    x-jsonld-id: http://www.opengis.net/cis/1.1/axisLabels
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#string
  path:
    x-jsonld-id: https://w3id.org/idsa/core/path
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#string
  interpolationRestriction:
    x-jsonld-id: http://www.opengis.net/cis/1.1/interpolationRestriction
    x-jsonld-type: '@id'
  axis:
    x-jsonld-id: http://www.opengis.net/cis/1.1/axis
    x-jsonld-type: '@id'
  ImageResource: https://w3id.org/idsa/core/ImageResource
  spatialResolutionInMeters: http://www.w3.org/ns/dcat#spatialResolutionInMeters
  partition:
    x-jsonld-id: http://www.opengis.net/cis/1.1/partition
    x-jsonld-type: '@id'
  CoverageByPartitioningType: http://www.opengis.net/cis/1.1/CoverageByPartitioningType
  GeneralGridCoverageType: http://www.opengis.net/cis/1.1/GeneralGridCoverageType
  homepage: http://xmlns.com/foaf/0.1/homepage
  maxValue: https://w3id.org/iliad/oim/metadata/maxValue
  sensorModelRef:
    x-jsonld-id: http://www.sensorml.com/sensorML-2.0/sensorModelRef
    x-jsonld-type: '@id'
  Axis: http://www.opengis.net/cis/1.1/Axis
  appliedModel:
    x-jsonld-id: https://w3id.org/iliad/oim/metadata/appliedModel
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#string
  Graph: http://www.w3.org/2004/03/trix/rdfg-1/Graph
  unitsDescription:
    x-jsonld-id: https://w3id.org/iliad/oim/metadata/unitsDescription
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#string
  Artifact: https://w3id.org/idsa/core/Artifact
  filters:
    x-jsonld-id: https://w3id.org/iliad/oim/metadata/filters
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#string
  noDataValue:
    x-jsonld-id: https://w3id.org/iliad/oim/metadata/noDataValue
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#string
  searchText:
    x-jsonld-id: https://w3id.org/iliad/oim/metadata/searchText
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#string
  profileSchema:
    x-jsonld-id: https://w3id.org/iliad/oim/metadata/profileSchema
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#string
  coverageRef:
    x-jsonld-id: http://www.opengis.net/cis/1.1/coverageRef
    x-jsonld-type: '@id'
  Agent: http://xmlns.com/foaf/0.1/Agent
  ContentType: https://w3id.org/idsa/core/ContentType
  creator: http://purl.org/dc/terms/creator
  name:
    x-jsonld-id: http://www.opengis.net/swe/2.0/name
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#string
  dataBlock:
    x-jsonld-id: http://www.opengis.net/cis/1.1/dataBlock
    x-jsonld-type: '@id'
  DataService: http://www.w3.org/ns/dcat#DataService
  representation:
    x-jsonld-id: https://w3id.org/idsa/core/representation
    x-jsonld-type: '@id'
  minDate:
    x-jsonld-id: https://w3id.org/iliad/oim/metadata/minDate
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#dateTimeStamp
  value: http://www.opengis.net/cis/1.1/value
  interval:
    x-jsonld-id: http://www.opengis.net/swe/2.0/interval
    x-jsonld-type: '@id'
  uomLabel:
    x-jsonld-id: http://www.opengis.net/cis/1.1/uomLabel
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#string
  RangeSetType: http://www.opengis.net/cis/1.1/RangeSetType
  allowedInterpolation:
    x-jsonld-id: http://www.opengis.net/cis/1.1/allowedInterpolation
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#anyURI
  axisLabel:
    x-jsonld-id: http://www.opengis.net/cis/1.1/axisLabel
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#string
  rights: http://www.w3.org/ns/dcat#rights
  TemporalEntity: http://www.w3.org/2006/time#TemporalEntity
  DataRecordType: http://www.opengis.net/swe/2.0/DataRecordType
  IrregularAxisType: http://www.opengis.net/cis/1.1/IrregularAxisType
  field:
    x-jsonld-id: http://www.opengis.net/swe/2.0/field
    x-jsonld-type: '@id'
  PartitionSetType: http://www.opengis.net/cis/1.1/PartitionSetType
  identifier: http://purl.org/dc/terms/identifier
  keyword: http://www.w3.org/ns/dcat#keyword
  envelope:
    x-jsonld-id: http://www.opengis.net/cis/1.1/envelope
    x-jsonld-type: '@id'
  endpointInformation:
    x-jsonld-id: https://w3id.org/idsa/core/endpointInformation
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#string
  fileName:
    x-jsonld-id: https://w3id.org/idsa/core/fileName
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#string
  metadata:
    x-jsonld-id: http://www.opengis.net/cis/1.1/metadata
    x-jsonld-type: '@id'
  byteSize:
    x-jsonld-id: https://w3id.org/idsa/core/byteSize
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#integer
  instance:
    x-jsonld-id: https://w3id.org/idsa/core/instance
    x-jsonld-type: '@id'
  isDefinedBy: http://www.w3.org/2000/01/rdf-schema#isDefinedBy
  definition:
    x-jsonld-id: http://www.w3.org/2004/02/skos/core#definition
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#string
  RangeSetRefType: http://www.opengis.net/cis/1.1/RangeSetRefType
  srsName:
    x-jsonld-id: http://www.opengis.net/cis/1.1/srsName
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#anyURI
  QuantityType: http://www.opengis.net/swe/2.0/QuantityType
  technicalManagerInfo:
    x-jsonld-id: https://w3id.org/iliad/oim/metadata/technicalManagerInfo
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#string
  colorTable:
    x-jsonld-id: https://w3id.org/iliad/oim/metadata/colorTable
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#string
  names:
    x-jsonld-id: http://www.opengis.net/swe/2.0/names
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#string
  title: http://www.w3.org/2000/01/rdf-schema#label
  dataType:
    x-jsonld-id: https://w3id.org/idsa/core/dataType
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#anyURI
  source: http://purl.org/dc/terms/source
  type: '@type'
  publisher:
    x-jsonld-id: https://w3id.org/idsa/core/publisher
    x-jsonld-type: '@id'
  mediaType: http://purl.org/dc/terms/mediaType
  uom:
    x-jsonld-id: http://www.opengis.net/swe/2.0/uom
    x-jsonld-type: '@id'
  licence: http://purl.org/dc/terms/licence
  subDatasetName: https://w3id.org/iliad/oim/metadata/subDatasetName
  upperBound:
    x-jsonld-id: http://www.opengis.net/cis/1.1/upperBound
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#integer
  modified: http://purl.org/dc/terms/modified
  Frequency: https://w3id.org/idsa/core/Frequency
  Endpoint: https://w3id.org/idsa/core/Endpoint
  samplingRate:
    x-jsonld-id: https://w3id.org/idsa/core/samplingRate
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#decimal
  CoverageByDomainAndRangeType: http://www.opengis.net/cis/1.1/CoverageByDomainAndRangeType
  endpointDocumentation:
    x-jsonld-id: https://w3id.org/idsa/core/endpointDocumentation
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#anyURI
  accessRights: http://purl.org/dc/terms/accessRights
  DCMIType: http://purl.org/dc/terms/DCMIType
  checkSum:
    x-jsonld-id: https://w3id.org/idsa/core/checkSum
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#string
  seeAlso: http://www.w3.org/2000/01/rdf-schema#seeAlso
  contentType:
    x-jsonld-id: https://w3id.org/idsa/core/contentType
    x-jsonld-type: '@id'
  RepresentationInstance: https://w3id.org/idsa/core/RepresentationInstance
  partitionSet:
    x-jsonld-id: http://www.opengis.net/cis/1.1/partitionSet
    x-jsonld-type: '@id'
  datasetManagerInfo:
    x-jsonld-id: https://w3id.org/iliad/oim/metadata/datasetManagerInfo
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#string
  contentStandard:
    x-jsonld-id: https://w3id.org/idsa/core/contentStandard
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#anyURI
  dataTypeSchema:
    x-jsonld-id: https://w3id.org/idsa/core/dataTypeSchema
    x-jsonld-type: '@id'
  Language: https://w3id.org/idsa/core/Language
  Resource: https://w3id.org/idsa/core/Resource
  domainSet:
    x-jsonld-id: http://www.opengis.net/cis/1.1/domainSet
    x-jsonld-type: '@id'
  SpatialThing: http://www.w3.org/2003/01/geo/wgs84_pos#SpatialThing
  Party: http://www.w3.org/ns/odrl/2/Party
  comment: http://www.w3.org/2000/01/rdf-schema#comment
  License: http://purl.org/dc/terms/License
  language:
    x-jsonld-id: https://www.opengis.net/def/ogc-api/records/language
    x-jsonld-context:
      code: https://www.opengis.net/def/ogc-api/records/languageCode
      name: http://www.w3.org/2004/02/skos/core#prefLabel
  TransformationBySensorModelType: http://www.opengis.net/cis/1.1/TransformationBySensorModelType
  uomLabels:
    x-jsonld-id: http://www.opengis.net/cis/1.1/uomLabels
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#string
  contributor: http://purl.org/dc/terms/contributor
  resolutionUnit:
    x-jsonld-id: https://w3id.org/iliad/oim/metadata/resolutionUnit
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#string
  AudioResource: https://w3id.org/idsa/core/AudioResource
  DisplacementAxisNestType: http://www.opengis.net/cis/1.1/DisplacementAxisNestType
  DomainSetType: http://www.opengis.net/cis/1.1/DomainSetType
  conformsTo:
    x-jsonld-id: http://purl.org/dc/terms/conformsTo
    x-jsonld-container: '@set'
    x-jsonld-type: '@id'
  displacement:
    x-jsonld-id: http://www.opengis.net/cis/1.1/displacement
    x-jsonld-type: '@id'
  minValue: https://w3id.org/iliad/oim/metadata/minValue
  UnitReference: http://www.opengis.net/swe/2.0/UnitReference
  acrualPeriodicity: http://purl.org/dc/terms/acrualPeriodicity
  customLicense:
    x-jsonld-id: https://w3id.org/idsa/core/customLicense
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#anyURI
  code:
    x-jsonld-id: http://www.opengis.net/swe/2.0/code
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#string
  epsg:
    x-jsonld-id: https://w3id.org/iliad/oim/metadata/epsg
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#string
  description:
    x-jsonld-id: http://purl.org/dc/terms/description
    x-jsonld-container: '@set'
  format: http://purl.org/dc/terms/format
  accessURL:
    x-jsonld-id: https://w3id.org/idsa/core/accessURL
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#anyURI
  credits:
    x-jsonld-id: https://w3id.org/iliad/oim/metadata/credits
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#string
  temporal: http://purl.org/dc/terms/temporal
  accrualPolicy: http://purl.org/dc/terms/accrualPolicy
  resolution:
    x-jsonld-id: http://www.opengis.net/cis/1.1/resolution
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#string
  maxDate:
    x-jsonld-id: https://w3id.org/iliad/oim/metadata/maxDate
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#dateTimeStamp
  constraint:
    x-jsonld-id: http://www.opengis.net/swe/2.0/constraint
    x-jsonld-type: '@id'
  ConnectorEndpoint: https://w3id.org/idsa/core/ConnectorEndpoint
  numberOfRecords:
    x-jsonld-id: https://w3id.org/iliad/oim/metadata/numberOfRecords
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#integer
  RegularAxisType: http://www.opengis.net/cis/1.1/RegularAxisType
  standardLicense:
    x-jsonld-id: https://w3id.org/idsa/core/standardLicense
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#anyURI
  PhotonFluxDensity: http://purl.oclc.org/NET/ssnx/qu/dim#PhotonFluxDensity
  implements:
    x-jsonld-id: http://www.w3.org/ns/ssn/implements
    x-jsonld-type: '@id'
  invalidatedAtTime:
    x-jsonld-id: http://www.w3.org/ns/prov#invalidatedAtTime
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#dateTime
  MultiLineString: https://purl.org/geojson/vocab#MultiLineString
  Attachable: http://purl.org/linked-data/cube#Attachable
  QuantityValue: http://qudt.org/schema/qudt/QuantityValue
  Unit: http://qudt.org/schema/qudt/Unit
  Line: http://www.opengis.net/ont/sf#Line
  member:
    x-jsonld-id: http://xmlns.com/foaf/0.1/member
    x-jsonld-type: '@id'
  generatedAtTime:
    x-jsonld-id: http://www.w3.org/ns/prov#generatedAtTime
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#dateTime
  example: http://www.w3.org/2004/02/skos/core#example
  Slice: http://purl.org/linked-data/cube#Slice
  Concentration: http://purl.oclc.org/NET/ssnx/qu/dim#Concentration
  dataSet:
    x-jsonld-id: http://purl.org/linked-data/cube#dataSet
    x-jsonld-type: '@id'
  componentAttachment:
    x-jsonld-id: http://purl.org/linked-data/cube#componentAttachment
    x-jsonld-type: '@id'
  Platform: http://www.w3.org/ns/sosa/Platform
  concept:
    x-jsonld-id: http://purl.org/linked-data/cube#concept
    x-jsonld-type: '@id'
  Deployment: http://www.w3.org/ns/ssn/Deployment
  MultiSurface: http://www.opengis.net/ont/sf#MultiSurface
  TemporalDuration: http://www.w3.org/2006/time#TemporalDuration
  Procedure: http://www.w3.org/ns/sosa/Procedure
  DiffusionCoefficient: http://purl.oclc.org/NET/ssnx/qu/dim#DiffusionCoefficient
  asGeoJSON:
    x-jsonld-id: http://www.opengis.net/ont/geosparql#asGeoJSON
    x-jsonld-type: http://www.opengis.net/ont/geosparql#geoJSONLiteral
  Organization: https://schema.org/Organization
  Volume: http://purl.oclc.org/NET/ssnx/qu/dim#Volume
  Thing: http://www.w3.org/2002/07/owl#Thing
  GFI_Feature: http://def.isotc211.org/iso19156/2011/GeneralFeatureInstance#GFI_Feature
  AttributeProperty: http://purl.org/linked-data/cube#AttributeProperty
  quantityValue:
    x-jsonld-id: http://qudt.org/schema/qudt/quantityValue
    x-jsonld-type: '@id'
  TemporalUnit: http://www.w3.org/2006/time#TemporalUnit
  hosts:
    x-jsonld-id: http://www.w3.org/ns/sosa/hosts
    x-jsonld-type: '@id'
  asWKT:
    x-jsonld-id: http://www.opengis.net/ont/geosparql#asWKT
    x-jsonld-type: http://www.opengis.net/ont/geosparql#wktLiteral
  hasOutput:
    x-jsonld-id: http://www.w3.org/ns/ssn/hasOutput
    x-jsonld-type: '@id'
  Angle: http://purl.oclc.org/NET/ssnx/qu/dim#Angle
  TemperatureDrift: http://purl.oclc.org/NET/ssnx/qu/dim#TemperatureDrift
  RotationalSpeed: http://purl.oclc.org/NET/ssnx/qu/dim#RotationalSpeed
  FeatureOfInterest: http://www.w3.org/ns/sosa/FeatureOfInterest
  ComponentProperty: http://purl.org/linked-data/cube#ComponentProperty
  Class: http://www.w3.org/2000/01/rdf-schema#Class
  ObservationCollection: http://www.w3.org/ns/sosa/ObservationCollection
  Geometry: http://www.opengis.net/ont/geosparql#Geometry
  NumberPerArea: http://purl.oclc.org/NET/ssnx/qu/dim#NumberPerArea
  depiction: http://xmlns.com/foaf/0.1/depiction
  Curve: http://www.opengis.net/ont/sf#Curve
  Instant: http://www.w3.org/2006/time#Instant
  sfWithin:
    x-jsonld-id: http://www.opengis.net/ont/geosparql#sfWithin
    x-jsonld-type: '@id'
  ThermalConductivity: http://purl.oclc.org/NET/ssnx/qu/dim#ThermalConductivity
  hasUltimateFeatureOfInterest:
    x-jsonld-id: http://www.w3.org/ns/sosa/hasUltimateFeatureOfInterest
    x-jsonld-type: '@id'
  domainIncludes: https://schema.org/domainIncludes
  madeBySensor:
    x-jsonld-id: http://www.w3.org/ns/sosa/madeBySensor
    x-jsonld-type: '@id'
  long: http://www.w3.org/2003/01/geo/wgs84_pos#long
  ActuatableProperty: http://www.w3.org/ns/sosa/ActuatableProperty
  Feature: https://purl.org/geojson/vocab#Feature
  LineString: https://purl.org/geojson/vocab#LineString
  numericValue: http://qudt.org/schema/qudt/numericValue
  Concept: http://www.w3.org/2004/02/skos/core#Concept
  component:
    x-jsonld-id: http://purl.org/linked-data/cube#component
    x-jsonld-type: '@id'
  measure:
    x-jsonld-id: http://purl.org/linked-data/cube#measure
    x-jsonld-type: '@id'
  SliceKey: http://purl.org/linked-data/cube#SliceKey
  Result: http://www.w3.org/ns/sosa/Result
  isHostedBy:
    x-jsonld-id: http://www.w3.org/ns/sosa/isHostedBy
    x-jsonld-type: '@id'
  Compressibility: http://purl.oclc.org/NET/ssnx/qu/dim#Compressibility
  inDeployment:
    x-jsonld-id: http://www.w3.org/ns/ssn/inDeployment
    x-jsonld-type: '@id'
  ComponentSet: http://purl.org/linked-data/cube#ComponentSet
  MassPerTimePerArea: http://purl.oclc.org/NET/ssnx/qu/dim#MassPerTimePerArea
  numericDuration:
    x-jsonld-id: http://www.w3.org/2006/time#numericDuration
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#decimal
  ElectricConductivity: http://purl.oclc.org/NET/ssnx/qu/dim#ElectricConductivity
  Temperature: http://purl.oclc.org/NET/ssnx/qu/dim#Temperature
  hasProperty:
    x-jsonld-id: http://www.w3.org/ns/ssn/hasProperty
    x-jsonld-type: '@id'
  Measure: http://def.seegrid.csiro.au/isotc211/iso19103/2005/basic#Measure
  Person: http://xmlns.com/foaf/0.1/Person
  Triangle: http://www.opengis.net/ont/sf#Triangle
  note: http://www.w3.org/2004/02/skos/core#note
  observationGroup:
    x-jsonld-id: http://purl.org/linked-data/cube#observationGroup
    x-jsonld-type: '@id'
  Interval: http://www.w3.org/2006/time#Interval
  EnergyFlux: http://purl.oclc.org/NET/ssnx/qu/dim#EnergyFlux
  StressOrPressure: http://purl.oclc.org/NET/ssnx/qu/dim#StressOrPressure
  resultTime:
    x-jsonld-id: http://www.w3.org/ns/sosa/resultTime
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#dateTime
  VolumeDensityRate: http://purl.oclc.org/NET/ssnx/qu/dim#VolumeDensityRate
  phenomenonTime:
    x-jsonld-id: http://www.w3.org/ns/sosa/phenomenonTime
    x-jsonld-type: '@id'
  Energy: http://purl.oclc.org/NET/ssnx/qu/dim#Energy
  foaf.name: http://xmlns.com/foaf/0.1/name
  Role: https://schema.org/Role
  hasSerialization:
    x-jsonld-id: http://www.opengis.net/ont/geosparql#hasSerialization
    x-jsonld-type: http://www.w3.org/2000/01/rdf-schema#Literal
  hasTime:
    x-jsonld-id: http://www.w3.org/2006/time#hasTime
    x-jsonld-type: '@id'
  SF_SamplingFeature.sampledFeature:
    x-jsonld-id: http://def.isotc211.org/iso19156/2011/SamplingFeature#SF_SamplingFeature.sampledFeature
    x-jsonld-type: '@id'
  hasMember:
    x-jsonld-id: http://www.w3.org/ns/sosa/hasMember
    x-jsonld-type: '@id'
  rangeIncludes: https://schema.org/rangeIncludes
  hasInput:
    x-jsonld-id: http://www.w3.org/ns/ssn/hasInput
    x-jsonld-type: '@id'
  Mass: http://purl.oclc.org/NET/ssnx/qu/dim#Mass
  implementedBy:
    x-jsonld-id: http://www.w3.org/ns/ssn/implementedBy
    x-jsonld-type: '@id'
  location:
    x-jsonld-id: http://www.w3.org/2003/01/geo/wgs84_pos#location
    x-jsonld-type: '@id'
  ComponentSpecification: http://purl.org/linked-data/cube#ComponentSpecification
  Scheme: http://www.w3.org/2004/02/skos/core#Scheme
  hasEnd:
    x-jsonld-id: http://www.w3.org/2006/time#hasEnd
    x-jsonld-type: '@id'
  GeometryCollection: https://purl.org/geojson/vocab#GeometryCollection
  hasBeginning:
    x-jsonld-id: http://www.w3.org/2006/time#hasBeginning
    x-jsonld-type: '@id'
  isResultOf:
    x-jsonld-id: http://www.w3.org/ns/sosa/isResultOf
    x-jsonld-type: '@id'
  SF_SamplingFeature: http://def.isotc211.org/iso19156/2011/SamplingFeature#SF_SamplingFeature
  DimensionProperty: http://purl.org/linked-data/cube#DimensionProperty
  alt: http://www.w3.org/2003/01/geo/wgs84_pos#alt
  Acceleration: http://purl.oclc.org/NET/ssnx/qu/dim#Acceleration
  hasSubSystem:
    x-jsonld-id: http://www.w3.org/ns/ssn/hasSubSystem
    x-jsonld-type: '@id'
  Quantity: http://qudt.org/schema/qudt/Quantity
  MassFlowRate: http://purl.oclc.org/NET/ssnx/qu/dim#MassFlowRate
  qu.QuantityKind: http://purl.oclc.org/NET/ssnx/qu/qu#QuantityKind
  SpatialObjectCollection: http://www.opengis.net/ont/geosparql#SpatialObjectCollection
  Distance: http://purl.oclc.org/NET/ssnx/qu/dim#Distance
  deprecated: http://www.w3.org/2002/07/owl#deprecated
  Radiance: http://purl.oclc.org/NET/ssnx/qu/dim#Radiance
  Duration: http://www.w3.org/2006/time#Duration
  TIN: http://www.opengis.net/ont/sf#TIN
  SurfaceDensity: http://purl.oclc.org/NET/ssnx/qu/dim#SurfaceDensity
  wgs84.Point: http://www.w3.org/2003/01/geo/wgs84_pos#Point
  editorialNote: http://www.w3.org/2004/02/skos/core#editorialNote
  observes:
    x-jsonld-id: http://www.w3.org/ns/sosa/observes
    x-jsonld-type: '@id'
  hasDeployment:
    x-jsonld-id: http://www.w3.org/ns/ssn/hasDeployment
    x-jsonld-type: '@id'
  hasResult:
    x-jsonld-id: http://www.w3.org/ns/sosa/hasResult
    x-jsonld-type: '@id'
  order:
    x-jsonld-id: http://purl.org/linked-data/cube#order
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#int
  hasGeometry:
    x-jsonld-id: http://www.opengis.net/ont/geosparql#hasGeometry
    x-jsonld-type: '@id'
  usedProcedure:
    x-jsonld-id: http://www.w3.org/ns/sosa/usedProcedure
    x-jsonld-type: '@id'
  ssn.Property: http://www.w3.org/ns/ssn/Property
  sfContains:
    x-jsonld-id: http://www.opengis.net/ont/geosparql#sfContains
    x-jsonld-type: '@id'
  Density: http://purl.oclc.org/NET/ssnx/qu/dim#Density
  LinearRing: http://www.opengis.net/ont/sf#LinearRing
  Molality: http://purl.oclc.org/NET/ssnx/qu/dim#Molality
  inXSDDateTimeStamp:
    x-jsonld-id: http://www.w3.org/2006/time#inXSDDateTimeStamp
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#dateTimeStamp
  MeasureProperty: http://purl.org/linked-data/cube#MeasureProperty
  PropertyKind: http://purl.oclc.org/NET/ssnx/qu/qu#PropertyKind
  SpatialObject: http://www.opengis.net/ont/geosparql#SpatialObject
  sliceStructure:
    x-jsonld-id: http://purl.org/linked-data/cube#sliceStructure
    x-jsonld-type: '@id'
  hasFeatureOfInterest:
    x-jsonld-id: http://www.w3.org/ns/sosa/hasFeatureOfInterest
    x-jsonld-type: '@id'
  NumberPerLength: http://purl.oclc.org/NET/ssnx/qu/dim#NumberPerLength
  lat: http://www.w3.org/2003/01/geo/wgs84_pos#lat
  VolumeFlowRate: http://purl.oclc.org/NET/ssnx/qu/dim#VolumeFlowRate
  SpecificEntropy: http://purl.oclc.org/NET/ssnx/qu/dim#SpecificEntropy
  CodedProperty: http://purl.org/linked-data/cube#CodedProperty
  observedProperty:
    x-jsonld-id: http://www.w3.org/ns/sosa/observedProperty
    x-jsonld-type: '@id'
  slice:
    x-jsonld-id: http://purl.org/linked-data/cube#slice
    x-jsonld-type: '@id'
  madeObservation:
    x-jsonld-id: http://www.w3.org/ns/sosa/madeObservation
    x-jsonld-type: '@id'
  FeatureCollection: https://purl.org/geojson/vocab#FeatureCollection
  unit:
    x-jsonld-id: http://qudt.org/schema/qudt/unit
    x-jsonld-type: '@id'
  date: http://purl.org/dc/terms/date
  isPropertyOf:
    x-jsonld-id: http://www.w3.org/ns/ssn/isPropertyOf
    x-jsonld-type: '@id'
  ObservationGroup: http://purl.org/linked-data/cube#ObservationGroup
  Sample: http://www.w3.org/ns/sosa/Sample
  DataSet: http://purl.org/linked-data/cube#DataSet
  PolyhedralSurface: http://www.opengis.net/ont/sf#PolyhedralSurface
  Polygon: https://purl.org/geojson/vocab#Polygon
  MultiPolygon: https://purl.org/geojson/vocab#MultiPolygon
  ObservableProperty: http://www.w3.org/ns/sosa/ObservableProperty
  deployedSystem:
    x-jsonld-id: http://www.w3.org/ns/ssn/deployedSystem
    x-jsonld-type: '@id'
  System: http://www.w3.org/ns/ssn/System
  unitKind:
    x-jsonld-id: http://purl.oclc.org/NET/ssnx/qu/qu#unitKind
    x-jsonld-type: '@id'
  dimension:
    x-jsonld-id: http://purl.org/linked-data/cube#dimension
    x-jsonld-type: '@id'
  RadianceExposure: http://purl.oclc.org/NET/ssnx/qu/dim#RadianceExposure
  VelocityOrSpeed: http://purl.oclc.org/NET/ssnx/qu/dim#VelocityOrSpeed
  deployedOnPlatform:
    x-jsonld-id: http://www.w3.org/ns/ssn/deployedOnPlatform
    x-jsonld-type: '@id'
  inXSDDate:
    x-jsonld-id: http://www.w3.org/2006/time#inXSDDate
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#date
  GFI_DomainFeature: http://def.isotc211.org/iso19156/2011/GeneralFeatureInstance#GFI_DomainFeature
  Actuation: http://www.w3.org/ns/sosa/Actuation
  observation:
    x-jsonld-id: http://purl.org/linked-data/cube#observation
    x-jsonld-type: '@id'
  Dimensionless: http://purl.oclc.org/NET/ssnx/qu/dim#Dimensionless
  Area: http://purl.oclc.org/NET/ssnx/qu/dim#Area
  Sampling: http://www.w3.org/ns/sosa/Sampling
  Power: http://purl.oclc.org/NET/ssnx/qu/dim#Power
  OM_Observation: http://def.isotc211.org/iso19156/2011/Observation#OM_Observation
  prefLabel: http://www.w3.org/2004/02/skos/core#prefLabel
  Surface: http://www.opengis.net/ont/sf#Surface
  sliceKey:
    x-jsonld-id: http://purl.org/linked-data/cube#sliceKey
    x-jsonld-type: '@id'
  inScheme: http://www.w3.org/2004/02/skos/core#inScheme
  dct.description: http://purl.org/dc/terms/description
  MultiCurve: http://www.opengis.net/ont/sf#MultiCurve
  hasQuantityKind:
    x-jsonld-id: http://qudt.org/schema/qudt/hasQuantityKind
    x-jsonld-type: '@id'
  DataStructureDefinition: http://purl.org/linked-data/cube#DataStructureDefinition
  MultiPoint: https://purl.org/geojson/vocab#MultiPoint
  qb.Observation: http://purl.org/linked-data/cube#Observation
  EnergyDensity: http://purl.oclc.org/NET/ssnx/qu/dim#EnergyDensity
  Sensor: http://www.w3.org/ns/sosa/Sensor
  hasSimpleResult: http://www.w3.org/ns/sosa/hasSimpleResult
  unitType:
    x-jsonld-id: http://www.w3.org/2006/time#unitType
    x-jsonld-type: '@id'
  componentProperty:
    x-jsonld-id: http://purl.org/linked-data/cube#componentProperty
    x-jsonld-type: '@id'
  isFeatureOfInterestOf:
    x-jsonld-id: http://www.w3.org/ns/sosa/isFeatureOfInterestOf
    x-jsonld-type: '@id'
  sf.Geometry: http://www.opengis.net/ont/sf#Geometry
  schema.Person: https://schema.org/Person
  Observation: http://www.w3.org/ns/sosa/Observation
  Point: https://purl.org/geojson/vocab#Point
  schema.name: https://schema.org/name
  QuantityKind: http://qudt.org/schema/qudt/QuantityKind
  coordinates:
    x-jsonld-container: '@list'
    x-jsonld-id: https://purl.org/geojson/vocab#coordinates
  bbox:
    x-jsonld-container: '@list'
    x-jsonld-id: https://purl.org/geojson/vocab#bbox
  href:
    x-jsonld-type: '@id'
    x-jsonld-id: http://www.w3.org/ns/oa#hasTarget
  rel:
    x-jsonld-context:
      '@base': http://www.iana.org/assignments/relation/
    x-jsonld-id: http://www.iana.org/assignments/relation
    x-jsonld-type: '@id'
  hreflang: http://purl.org/dc/terms/language
  length: http://purl.org/dc/terms/extent
  updated: http://purl.org/dc/terms/modified
  uriTemplate:
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#string
    x-jsonld-id: http://www.w3.org/ns/oa#hasTarget
  id: '@id'
  properties: '@nest'
  geometry: https://purl.org/geojson/vocab#geometry
  features:
    x-jsonld-container: '@set'
    x-jsonld-id: https://purl.org/geojson/vocab#features
  links:
    x-jsonld-context:
      type: http://purl.org/dc/terms/type
    x-jsonld-id: http://www.w3.org/2000/01/rdf-schema#seeAlso
  time:
    x-jsonld-id: http://purl.org/dc/terms/temporal
    x-jsonld-context:
      interval:
        '@id': http://www.w3.org/2006/time#hasTime
        '@container': '@list'
      resolution: https://www.opengis.net/def/ogc-api/records/iso8601period
  keywords:
    x-jsonld-container: '@set'
    x-jsonld-id: http://www.w3.org/ns/dcat#keyword
  languages:
    x-jsonld-container: '@set'
    x-jsonld-id: https://www.opengis.net/def/ogc-api/records/languages
    x-jsonld-context:
      code: https://www.opengis.net/def/ogc-api/records/languageCode
      name: http://www.w3.org/2004/02/skos/core#prefLabel
  resourceLanguages:
    x-jsonld-container: '@set'
    x-jsonld-id: https://www.opengis.net/def/ogc-api/records/resourceLanguages
    x-jsonld-context:
      code: https://www.opengis.net/def/ogc-api/records/languageCode
      name: http://www.w3.org/2004/02/skos/core#prefLabel
  externalIds:
    x-jsonld-container: '@set'
    x-jsonld-id: https://www.opengis.net/def/ogc-api/records/scopedIdentifier
    x-jsonld-context:
      scheme: https://www.opengis.net/def/ogc-api/records/scheme
      value: https://www.opengis.net/def/ogc-api/records/id
  themes:
    x-jsonld-container: '@set'
    x-jsonld-id: https://www.opengis.net/def/ogc-api/records/themes
    x-jsonld-context:
      concepts:
        '@id': https://www.opengis.net/def/ogc-api/records/concept
        '@context':
          id:
            '@type': http://www.w3.org/2001/XMLSchema#string
            '@id': https://www.opengis.net/def/ogc-api/records/conceptID
      scheme: https://www.opengis.net/def/ogc-api/records/scheme
  formats:
    x-jsonld-container: '@set'
    x-jsonld-id: https://www.opengis.net/def/ogc-api/records/format
    x-jsonld-type: '@id'
  contacts:
    x-jsonld-container: '@set'
    x-jsonld-id: http://www.w3.org/ns/dcat#contactPoint
    x-jsonld-type: '@id'
  linkTemplates: https://www.opengis.net/def/ogc-api/records/hasLinkTemplate
  variables:
    x-jsonld-container: '@id'
    x-jsonld-id: https://www.opengis.net/def/ogc-api/records/hasVariable
    x-jsonld-context:
      '@base': http://example.com/variables/
      '@vocab': https://www.opengis.net/def/ogc-api/records/
x-jsonld-prefixes:
  geojson: https://purl.org/geojson/vocab#
  oa: http://www.w3.org/ns/oa#
  dct: http://purl.org/dc/terms/
  rdfs: http://www.w3.org/2000/01/rdf-schema#
  xsd: http://www.w3.org/2001/XMLSchema#
  w3ctime: http://www.w3.org/2006/time#
  rec: https://www.opengis.net/def/ogc-api/records/
  dcat: http://www.w3.org/ns/dcat#
  skos: http://www.w3.org/2004/02/skos/core#
  owl: http://www.w3.org/2002/07/owl#
  rdf: http://www.w3.org/1999/02/22-rdf-syntax-ns#
  dctype: http://purl.org/dc/dcmitype/
  vcard: http://www.w3.org/2006/vcard/ns#
  prov: http://www.w3.org/ns/prov#
  foaf: http://xmlns.com/foaf/0.1/

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/iliad-apis-features/build/annotated/hosted/iliad/api/features/stac_multidim_data/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/iliad-apis-features/build/annotated/hosted/iliad/api/features/stac_multidim_data/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "type": "@type",
    "coordinates": {
      "@container": "@list",
      "@id": "geojson:coordinates"
    },
    "bbox": {
      "@container": "@list",
      "@id": "geojson:bbox"
    },
    "href": {
      "@type": "@id",
      "@id": "oa:hasTarget"
    },
    "rel": {
      "@context": {
        "@base": "http://www.iana.org/assignments/relation/"
      },
      "@id": "http://www.iana.org/assignments/relation",
      "@type": "@id"
    },
    "hreflang": "dct:language",
    "title": "rdfs:label",
    "length": "dct:extent",
    "created": "dct:created",
    "updated": "dct:modified",
    "uriTemplate": {
      "@type": "xsd:string",
      "@id": "oa:hasTarget"
    },
    "id": "@id",
    "properties": "@nest",
    "geometry": "geojson:geometry",
    "Feature": "geojson:Feature",
    "FeatureCollection": "geojson:FeatureCollection",
    "GeometryCollection": "geojson:GeometryCollection",
    "LineString": "geojson:LineString",
    "MultiLineString": "geojson:MultiLineString",
    "MultiPoint": "geojson:MultiPoint",
    "MultiPolygon": "geojson:MultiPolygon",
    "Point": "geojson:Point",
    "Polygon": "geojson:Polygon",
    "features": {
      "@container": "@set",
      "@id": "geojson:features"
    },
    "links": {
      "@context": {
        "type": "dct:type"
      },
      "@id": "rdfs:seeAlso"
    },
    "time": {
      "@id": "dct:temporal",
      "@context": {
        "interval": {
          "@id": "w3ctime:hasTime",
          "@container": "@list"
        },
        "resolution": "rec:iso8601period"
      }
    },
    "description": {
      "@container": "@set",
      "@id": "dct:description"
    },
    "keywords": {
      "@container": "@set",
      "@id": "dcat:keyword"
    },
    "conformsTo": {
      "@container": "@set",
      "@id": "dct:conformsTo",
      "@type": "@id"
    },
    "language": {
      "@id": "rec:language",
      "@context": {
        "code": "rec:languageCode",
        "name": "skos:prefLabel"
      }
    },
    "languages": {
      "@container": "@set",
      "@id": "rec:languages",
      "@context": {
        "code": "rec:languageCode",
        "name": "skos:prefLabel"
      }
    },
    "resourceLanguages": {
      "@container": "@set",
      "@id": "rec:resourceLanguages",
      "@context": {
        "code": "rec:languageCode",
        "name": "skos:prefLabel"
      }
    },
    "externalIds": {
      "@container": "@set",
      "@id": "rec:scopedIdentifier",
      "@context": {
        "scheme": "rec:scheme",
        "value": "rec:id"
      }
    },
    "themes": {
      "@container": "@set",
      "@id": "rec:themes",
      "@context": {
        "concepts": {
          "@id": "rec:concept",
          "@context": {
            "id": {
              "@type": "xsd:string",
              "@id": "rec:conceptID"
            }
          }
        },
        "scheme": "rec:scheme"
      }
    },
    "formats": {
      "@container": "@set",
      "@id": "rec:format",
      "@type": "@id"
    },
    "contacts": {
      "@container": "@set",
      "@id": "dcat:contactPoint",
      "@type": "@id"
    },
    "license": "dcat:license",
    "rights": "dcat:rights",
    "linkTemplates": "rec:hasLinkTemplate",
    "variables": {
      "@container": "@id",
      "@id": "rec:hasVariable",
      "@context": {
        "@base": "http://example.com/variables/",
        "@vocab": "https://www.opengis.net/def/ogc-api/records/"
      }
    },
    "IndexAxisType": "http://www.opengis.net/cis/1.1/IndexAxisType",
    "spatial": "dct:spatial",
    "previewInfo": {
      "@id": "https://w3id.org/iliad/oim/metadata/previewInfo",
      "@type": "xsd:string"
    },
    "coverage": {
      "@id": "http://www.opengis.net/cis/1.1/coverage",
      "@type": "@id"
    },
    "VideoResource": "https://w3id.org/idsa/core/VideoResource",
    "DigitalContent": "https://w3id.org/idsa/core/DigitalContent",
    "affiliation": "https://schema.org/affiliation",
    "endpointArtifact": {
      "@id": "https://w3id.org/idsa/core/endpointArtifact",
      "@type": "@id"
    },
    "versionInfo": "owl:versionInfo",
    "VDataBlockType": "http://www.opengis.net/cis/1.1/VDataBlockType",
    "ImageRepresentation": "https://w3id.org/idsa/core/ImageRepresentation",
    "lowerBound": {
      "@id": "http://www.opengis.net/cis/1.1/lowerBound",
      "@type": "xsd:integer"
    },
    "Dataset": "dcat:Dataset",
    "EnvelopeByAxisType": "http://www.opengis.net/cis/1.1/EnvelopeByAxisType",
    "width": {
      "@id": "https://w3id.org/idsa/core/width",
      "@type": "xsd:decimal"
    },
    "Representation": "https://w3id.org/idsa/core/Representation",
    "accrualPeriodicity": {
      "@id": "https://w3id.org/idsa/core/accrualPeriodicity",
      "@type": "@id"
    },
    "model": {
      "@id": "http://www.opengis.net/cis/1.1/model",
      "@type": "@id"
    },
    "MediaType": "dct:MediaType",
    "Distribution": "dcat:Distribution",
    "dataset": {
      "@id": "dcat:dataset",
      "@type": "@id"
    },
    "AudioRepresentation": "https://w3id.org/idsa/core/AudioRepresentation",
    "usageNote": "http://purl.org/vocab/vann/usageNote",
    "AxisExtendType": "http://www.opengis.net/cis/1.1/AxisExtendType",
    "height": {
      "@id": "https://w3id.org/idsa/core/height",
      "@type": "xsd:decimal"
    },
    "hasQualityMetadata": {
      "@id": "http://www.w3.org/ns/dqv#hasQualityMetadata",
      "@type": "@id"
    },
    "coordinate": {
      "@id": "http://www.opengis.net/cis/1.1/coordinate",
      "@type": "@id"
    },
    "frameRate": {
      "@id": "https://w3id.org/idsa/core/frameRate",
      "@type": "xsd:decimal"
    },
    "QualityMetadata": "http://www.w3.org/ns/dqv#QualityMetadata",
    "GridLimitsType": "http://www.opengis.net/cis/1.1/GridLimitsType",
    "temporalResolution": "dcat:temporalResolution",
    "VideoRepresentation": "https://w3id.org/idsa/core/VideoRepresentation",
    "maker": "foaf:maker",
    "fileReference": "http://www.opengis.net/cis/1.1/fileReference",
    "DataRepresentation": "https://w3id.org/idsa/core/DataRepresentation",
    "sensorInstanceRef": {
      "@id": "http://www.sensorml.com/sensorML-2.0/sensorInstanceRef",
      "@type": "@id"
    },
    "generalGrid": {
      "@id": "http://www.opengis.net/cis/1.1/generalGrid",
      "@type": "@id"
    },
    "label": "rdfs:label",
    "positionValuePair": {
      "@id": "http://www.opengis.net/cis/1.1/positionValuePair",
      "@type": "@id"
    },
    "PVPType": "http://www.opengis.net/cis/1.1/PVPType",
    "scaleFactor": {
      "@id": "https://w3id.org/iliad/oim/metadata/scaleFactor",
      "@type": "xsd:float"
    },
    "AllowedValues": "http://www.opengis.net/swe/2.0/AllowedValues",
    "project": "https://w3id.org/iliad/oim/metadata/project",
    "gridLimits": {
      "@id": "http://www.opengis.net/cis/1.1/gridLimits",
      "@type": "@id"
    },
    "TextRepresentation": "https://w3id.org/idsa/core/TextRepresentation",
    "TextResource": "https://w3id.org/idsa/core/TextResource",
    "DataResource": "https://w3id.org/idsa/core/DataResource",
    "rangeSet": {
      "@id": "http://www.opengis.net/cis/1.1/rangeSet",
      "@type": "@id"
    },
    "Location": "https://w3id.org/idsa/core/Location",
    "rangeType": {
      "@id": "http://www.opengis.net/cis/1.1/rangeType",
      "@type": "@id"
    },
    "axisLabels": {
      "@id": "http://www.opengis.net/cis/1.1/axisLabels",
      "@type": "xsd:string"
    },
    "path": {
      "@id": "https://w3id.org/idsa/core/path",
      "@type": "xsd:string"
    },
    "interpolationRestriction": {
      "@id": "http://www.opengis.net/cis/1.1/interpolationRestriction",
      "@type": "@id"
    },
    "axis": {
      "@id": "http://www.opengis.net/cis/1.1/axis",
      "@type": "@id"
    },
    "ImageResource": "https://w3id.org/idsa/core/ImageResource",
    "spatialResolutionInMeters": "dcat:spatialResolutionInMeters",
    "partition": {
      "@id": "http://www.opengis.net/cis/1.1/partition",
      "@type": "@id"
    },
    "CoverageByPartitioningType": "http://www.opengis.net/cis/1.1/CoverageByPartitioningType",
    "GeneralGridCoverageType": "http://www.opengis.net/cis/1.1/GeneralGridCoverageType",
    "homepage": "foaf:homepage",
    "maxValue": "https://w3id.org/iliad/oim/metadata/maxValue",
    "sensorModelRef": {
      "@id": "http://www.sensorml.com/sensorML-2.0/sensorModelRef",
      "@type": "@id"
    },
    "Axis": "http://www.opengis.net/cis/1.1/Axis",
    "appliedModel": {
      "@id": "https://w3id.org/iliad/oim/metadata/appliedModel",
      "@type": "xsd:string"
    },
    "Graph": "http://www.w3.org/2004/03/trix/rdfg-1/Graph",
    "unitsDescription": {
      "@id": "https://w3id.org/iliad/oim/metadata/unitsDescription",
      "@type": "xsd:string"
    },
    "Artifact": "https://w3id.org/idsa/core/Artifact",
    "filters": {
      "@id": "https://w3id.org/iliad/oim/metadata/filters",
      "@type": "xsd:string"
    },
    "noDataValue": {
      "@id": "https://w3id.org/iliad/oim/metadata/noDataValue",
      "@type": "xsd:string"
    },
    "searchText": {
      "@id": "https://w3id.org/iliad/oim/metadata/searchText",
      "@type": "xsd:string"
    },
    "profileSchema": {
      "@id": "https://w3id.org/iliad/oim/metadata/profileSchema",
      "@type": "xsd:string"
    },
    "coverageRef": {
      "@id": "http://www.opengis.net/cis/1.1/coverageRef",
      "@type": "@id"
    },
    "Agent": "foaf:Agent",
    "ContentType": "https://w3id.org/idsa/core/ContentType",
    "creator": "dct:creator",
    "name": {
      "@id": "http://www.opengis.net/swe/2.0/name",
      "@type": "xsd:string"
    },
    "dataBlock": {
      "@id": "http://www.opengis.net/cis/1.1/dataBlock",
      "@type": "@id"
    },
    "DataService": "dcat:DataService",
    "representation": {
      "@id": "https://w3id.org/idsa/core/representation",
      "@type": "@id"
    },
    "minDate": {
      "@id": "https://w3id.org/iliad/oim/metadata/minDate",
      "@type": "xsd:dateTimeStamp"
    },
    "value": "http://www.opengis.net/cis/1.1/value",
    "interval": {
      "@id": "http://www.opengis.net/swe/2.0/interval",
      "@type": "@id"
    },
    "uomLabel": {
      "@id": "http://www.opengis.net/cis/1.1/uomLabel",
      "@type": "xsd:string"
    },
    "RangeSetType": "http://www.opengis.net/cis/1.1/RangeSetType",
    "allowedInterpolation": {
      "@id": "http://www.opengis.net/cis/1.1/allowedInterpolation",
      "@type": "xsd:anyURI"
    },
    "axisLabel": {
      "@id": "http://www.opengis.net/cis/1.1/axisLabel",
      "@type": "xsd:string"
    },
    "TemporalEntity": "w3ctime:TemporalEntity",
    "DataRecordType": "http://www.opengis.net/swe/2.0/DataRecordType",
    "IrregularAxisType": "http://www.opengis.net/cis/1.1/IrregularAxisType",
    "field": {
      "@id": "http://www.opengis.net/swe/2.0/field",
      "@type": "@id"
    },
    "PartitionSetType": "http://www.opengis.net/cis/1.1/PartitionSetType",
    "identifier": "dct:identifier",
    "keyword": "dcat:keyword",
    "envelope": {
      "@id": "http://www.opengis.net/cis/1.1/envelope",
      "@type": "@id"
    },
    "endpointInformation": {
      "@id": "https://w3id.org/idsa/core/endpointInformation",
      "@type": "xsd:string"
    },
    "fileName": {
      "@id": "https://w3id.org/idsa/core/fileName",
      "@type": "xsd:string"
    },
    "metadata": {
      "@id": "http://www.opengis.net/cis/1.1/metadata",
      "@type": "@id"
    },
    "byteSize": {
      "@id": "https://w3id.org/idsa/core/byteSize",
      "@type": "xsd:integer"
    },
    "instance": {
      "@id": "https://w3id.org/idsa/core/instance",
      "@type": "@id"
    },
    "isDefinedBy": "rdfs:isDefinedBy",
    "definition": {
      "@id": "skos:definition",
      "@type": "xsd:string"
    },
    "RangeSetRefType": "http://www.opengis.net/cis/1.1/RangeSetRefType",
    "srsName": {
      "@id": "http://www.opengis.net/cis/1.1/srsName",
      "@type": "xsd:anyURI"
    },
    "QuantityType": "http://www.opengis.net/swe/2.0/QuantityType",
    "technicalManagerInfo": {
      "@id": "https://w3id.org/iliad/oim/metadata/technicalManagerInfo",
      "@type": "xsd:string"
    },
    "colorTable": {
      "@id": "https://w3id.org/iliad/oim/metadata/colorTable",
      "@type": "xsd:string"
    },
    "names": {
      "@id": "http://www.opengis.net/swe/2.0/names",
      "@type": "xsd:string"
    },
    "dataType": {
      "@id": "https://w3id.org/idsa/core/dataType",
      "@type": "xsd:anyURI"
    },
    "source": "dct:source",
    "publisher": {
      "@id": "https://w3id.org/idsa/core/publisher",
      "@type": "@id"
    },
    "mediaType": "dct:mediaType",
    "uom": {
      "@id": "http://www.opengis.net/swe/2.0/uom",
      "@type": "@id"
    },
    "licence": "dct:licence",
    "subDatasetName": "https://w3id.org/iliad/oim/metadata/subDatasetName",
    "upperBound": {
      "@id": "http://www.opengis.net/cis/1.1/upperBound",
      "@type": "xsd:integer"
    },
    "modified": "dct:modified",
    "Frequency": "https://w3id.org/idsa/core/Frequency",
    "Endpoint": "https://w3id.org/idsa/core/Endpoint",
    "samplingRate": {
      "@id": "https://w3id.org/idsa/core/samplingRate",
      "@type": "xsd:decimal"
    },
    "CoverageByDomainAndRangeType": "http://www.opengis.net/cis/1.1/CoverageByDomainAndRangeType",
    "endpointDocumentation": {
      "@id": "https://w3id.org/idsa/core/endpointDocumentation",
      "@type": "xsd:anyURI"
    },
    "accessRights": "dct:accessRights",
    "DCMIType": "dct:DCMIType",
    "checkSum": {
      "@id": "https://w3id.org/idsa/core/checkSum",
      "@type": "xsd:string"
    },
    "seeAlso": "rdfs:seeAlso",
    "contentType": {
      "@id": "https://w3id.org/idsa/core/contentType",
      "@type": "@id"
    },
    "RepresentationInstance": "https://w3id.org/idsa/core/RepresentationInstance",
    "partitionSet": {
      "@id": "http://www.opengis.net/cis/1.1/partitionSet",
      "@type": "@id"
    },
    "datasetManagerInfo": {
      "@id": "https://w3id.org/iliad/oim/metadata/datasetManagerInfo",
      "@type": "xsd:string"
    },
    "contentStandard": {
      "@id": "https://w3id.org/idsa/core/contentStandard",
      "@type": "xsd:anyURI"
    },
    "dataTypeSchema": {
      "@id": "https://w3id.org/idsa/core/dataTypeSchema",
      "@type": "@id"
    },
    "Language": "https://w3id.org/idsa/core/Language",
    "Resource": "https://w3id.org/idsa/core/Resource",
    "domainSet": {
      "@id": "http://www.opengis.net/cis/1.1/domainSet",
      "@type": "@id"
    },
    "SpatialThing": "http://www.w3.org/2003/01/geo/wgs84_pos#SpatialThing",
    "Party": "http://www.w3.org/ns/odrl/2/Party",
    "comment": "rdfs:comment",
    "License": "dct:License",
    "TransformationBySensorModelType": "http://www.opengis.net/cis/1.1/TransformationBySensorModelType",
    "uomLabels": {
      "@id": "http://www.opengis.net/cis/1.1/uomLabels",
      "@type": "xsd:string"
    },
    "contributor": "dct:contributor",
    "resolutionUnit": {
      "@id": "https://w3id.org/iliad/oim/metadata/resolutionUnit",
      "@type": "xsd:string"
    },
    "AudioResource": "https://w3id.org/idsa/core/AudioResource",
    "DisplacementAxisNestType": "http://www.opengis.net/cis/1.1/DisplacementAxisNestType",
    "DomainSetType": "http://www.opengis.net/cis/1.1/DomainSetType",
    "displacement": {
      "@id": "http://www.opengis.net/cis/1.1/displacement",
      "@type": "@id"
    },
    "minValue": "https://w3id.org/iliad/oim/metadata/minValue",
    "UnitReference": "http://www.opengis.net/swe/2.0/UnitReference",
    "acrualPeriodicity": "dct:acrualPeriodicity",
    "customLicense": {
      "@id": "https://w3id.org/idsa/core/customLicense",
      "@type": "xsd:anyURI"
    },
    "code": {
      "@id": "http://www.opengis.net/swe/2.0/code",
      "@type": "xsd:string"
    },
    "epsg": {
      "@id": "https://w3id.org/iliad/oim/metadata/epsg",
      "@type": "xsd:string"
    },
    "format": "dct:format",
    "accessURL": {
      "@id": "https://w3id.org/idsa/core/accessURL",
      "@type": "xsd:anyURI"
    },
    "credits": {
      "@id": "https://w3id.org/iliad/oim/metadata/credits",
      "@type": "xsd:string"
    },
    "temporal": "dct:temporal",
    "accrualPolicy": "dct:accrualPolicy",
    "resolution": {
      "@id": "http://www.opengis.net/cis/1.1/resolution",
      "@type": "xsd:string"
    },
    "maxDate": {
      "@id": "https://w3id.org/iliad/oim/metadata/maxDate",
      "@type": "xsd:dateTimeStamp"
    },
    "constraint": {
      "@id": "http://www.opengis.net/swe/2.0/constraint",
      "@type": "@id"
    },
    "ConnectorEndpoint": "https://w3id.org/idsa/core/ConnectorEndpoint",
    "numberOfRecords": {
      "@id": "https://w3id.org/iliad/oim/metadata/numberOfRecords",
      "@type": "xsd:integer"
    },
    "RegularAxisType": "http://www.opengis.net/cis/1.1/RegularAxisType",
    "standardLicense": {
      "@id": "https://w3id.org/idsa/core/standardLicense",
      "@type": "xsd:anyURI"
    },
    "PhotonFluxDensity": "http://purl.oclc.org/NET/ssnx/qu/dim#PhotonFluxDensity",
    "implements": {
      "@id": "http://www.w3.org/ns/ssn/implements",
      "@type": "@id"
    },
    "invalidatedAtTime": {
      "@id": "prov:invalidatedAtTime",
      "@type": "xsd:dateTime"
    },
    "Attachable": "http://purl.org/linked-data/cube#Attachable",
    "QuantityValue": "http://qudt.org/schema/qudt/QuantityValue",
    "Unit": "http://qudt.org/schema/qudt/Unit",
    "Line": "http://www.opengis.net/ont/sf#Line",
    "member": {
      "@id": "foaf:member",
      "@type": "@id"
    },
    "generatedAtTime": {
      "@id": "prov:generatedAtTime",
      "@type": "xsd:dateTime"
    },
    "example": "skos:example",
    "Slice": "http://purl.org/linked-data/cube#Slice",
    "Concentration": "http://purl.oclc.org/NET/ssnx/qu/dim#Concentration",
    "dataSet": {
      "@id": "http://purl.org/linked-data/cube#dataSet",
      "@type": "@id"
    },
    "componentAttachment": {
      "@id": "http://purl.org/linked-data/cube#componentAttachment",
      "@type": "@id"
    },
    "Platform": "http://www.w3.org/ns/sosa/Platform",
    "concept": {
      "@id": "http://purl.org/linked-data/cube#concept",
      "@type": "@id"
    },
    "Deployment": "http://www.w3.org/ns/ssn/Deployment",
    "MultiSurface": "http://www.opengis.net/ont/sf#MultiSurface",
    "TemporalDuration": "w3ctime:TemporalDuration",
    "Procedure": "http://www.w3.org/ns/sosa/Procedure",
    "DiffusionCoefficient": "http://purl.oclc.org/NET/ssnx/qu/dim#DiffusionCoefficient",
    "asGeoJSON": {
      "@id": "http://www.opengis.net/ont/geosparql#asGeoJSON",
      "@type": "http://www.opengis.net/ont/geosparql#geoJSONLiteral"
    },
    "Organization": "https://schema.org/Organization",
    "Volume": "http://purl.oclc.org/NET/ssnx/qu/dim#Volume",
    "Thing": "owl:Thing",
    "GFI_Feature": "http://def.isotc211.org/iso19156/2011/GeneralFeatureInstance#GFI_Feature",
    "AttributeProperty": "http://purl.org/linked-data/cube#AttributeProperty",
    "quantityValue": {
      "@id": "http://qudt.org/schema/qudt/quantityValue",
      "@type": "@id"
    },
    "TemporalUnit": "w3ctime:TemporalUnit",
    "hosts": {
      "@id": "http://www.w3.org/ns/sosa/hosts",
      "@type": "@id"
    },
    "asWKT": {
      "@id": "http://www.opengis.net/ont/geosparql#asWKT",
      "@type": "http://www.opengis.net/ont/geosparql#wktLiteral"
    },
    "hasOutput": {
      "@id": "http://www.w3.org/ns/ssn/hasOutput",
      "@type": "@id"
    },
    "Angle": "http://purl.oclc.org/NET/ssnx/qu/dim#Angle",
    "TemperatureDrift": "http://purl.oclc.org/NET/ssnx/qu/dim#TemperatureDrift",
    "RotationalSpeed": "http://purl.oclc.org/NET/ssnx/qu/dim#RotationalSpeed",
    "FeatureOfInterest": "http://www.w3.org/ns/sosa/FeatureOfInterest",
    "ComponentProperty": "http://purl.org/linked-data/cube#ComponentProperty",
    "Class": "rdfs:Class",
    "ObservationCollection": "http://www.w3.org/ns/sosa/ObservationCollection",
    "Geometry": "http://www.opengis.net/ont/geosparql#Geometry",
    "NumberPerArea": "http://purl.oclc.org/NET/ssnx/qu/dim#NumberPerArea",
    "depiction": "foaf:depiction",
    "Curve": "http://www.opengis.net/ont/sf#Curve",
    "Instant": "w3ctime:Instant",
    "sfWithin": {
      "@id": "http://www.opengis.net/ont/geosparql#sfWithin",
      "@type": "@id"
    },
    "ThermalConductivity": "http://purl.oclc.org/NET/ssnx/qu/dim#ThermalConductivity",
    "hasUltimateFeatureOfInterest": {
      "@id": "http://www.w3.org/ns/sosa/hasUltimateFeatureOfInterest",
      "@type": "@id"
    },
    "domainIncludes": "https://schema.org/domainIncludes",
    "madeBySensor": {
      "@id": "http://www.w3.org/ns/sosa/madeBySensor",
      "@type": "@id"
    },
    "long": "http://www.w3.org/2003/01/geo/wgs84_pos#long",
    "ActuatableProperty": "http://www.w3.org/ns/sosa/ActuatableProperty",
    "numericValue": "http://qudt.org/schema/qudt/numericValue",
    "Concept": "skos:Concept",
    "component": {
      "@id": "http://purl.org/linked-data/cube#component",
      "@type": "@id"
    },
    "measure": {
      "@id": "http://purl.org/linked-data/cube#measure",
      "@type": "@id"
    },
    "SliceKey": "http://purl.org/linked-data/cube#SliceKey",
    "Result": "http://www.w3.org/ns/sosa/Result",
    "isHostedBy": {
      "@id": "http://www.w3.org/ns/sosa/isHostedBy",
      "@type": "@id"
    },
    "Compressibility": "http://purl.oclc.org/NET/ssnx/qu/dim#Compressibility",
    "inDeployment": {
      "@id": "http://www.w3.org/ns/ssn/inDeployment",
      "@type": "@id"
    },
    "ComponentSet": "http://purl.org/linked-data/cube#ComponentSet",
    "MassPerTimePerArea": "http://purl.oclc.org/NET/ssnx/qu/dim#MassPerTimePerArea",
    "numericDuration": {
      "@id": "w3ctime:numericDuration",
      "@type": "xsd:decimal"
    },
    "ElectricConductivity": "http://purl.oclc.org/NET/ssnx/qu/dim#ElectricConductivity",
    "Temperature": "http://purl.oclc.org/NET/ssnx/qu/dim#Temperature",
    "hasProperty": {
      "@id": "http://www.w3.org/ns/ssn/hasProperty",
      "@type": "@id"
    },
    "Measure": "http://def.seegrid.csiro.au/isotc211/iso19103/2005/basic#Measure",
    "Person": "foaf:Person",
    "Triangle": "http://www.opengis.net/ont/sf#Triangle",
    "note": "skos:note",
    "observationGroup": {
      "@id": "http://purl.org/linked-data/cube#observationGroup",
      "@type": "@id"
    },
    "Interval": "w3ctime:Interval",
    "EnergyFlux": "http://purl.oclc.org/NET/ssnx/qu/dim#EnergyFlux",
    "StressOrPressure": "http://purl.oclc.org/NET/ssnx/qu/dim#StressOrPressure",
    "resultTime": {
      "@id": "http://www.w3.org/ns/sosa/resultTime",
      "@type": "xsd:dateTime"
    },
    "VolumeDensityRate": "http://purl.oclc.org/NET/ssnx/qu/dim#VolumeDensityRate",
    "phenomenonTime": {
      "@id": "http://www.w3.org/ns/sosa/phenomenonTime",
      "@type": "@id"
    },
    "Energy": "http://purl.oclc.org/NET/ssnx/qu/dim#Energy",
    "foaf.name": "foaf:name",
    "Role": "https://schema.org/Role",
    "hasSerialization": {
      "@id": "http://www.opengis.net/ont/geosparql#hasSerialization",
      "@type": "rdfs:Literal"
    },
    "hasTime": {
      "@id": "w3ctime:hasTime",
      "@type": "@id"
    },
    "SF_SamplingFeature.sampledFeature": {
      "@id": "http://def.isotc211.org/iso19156/2011/SamplingFeature#SF_SamplingFeature.sampledFeature",
      "@type": "@id"
    },
    "hasMember": {
      "@id": "http://www.w3.org/ns/sosa/hasMember",
      "@type": "@id"
    },
    "rangeIncludes": "https://schema.org/rangeIncludes",
    "hasInput": {
      "@id": "http://www.w3.org/ns/ssn/hasInput",
      "@type": "@id"
    },
    "Mass": "http://purl.oclc.org/NET/ssnx/qu/dim#Mass",
    "implementedBy": {
      "@id": "http://www.w3.org/ns/ssn/implementedBy",
      "@type": "@id"
    },
    "location": {
      "@id": "http://www.w3.org/2003/01/geo/wgs84_pos#location",
      "@type": "@id"
    },
    "ComponentSpecification": "http://purl.org/linked-data/cube#ComponentSpecification",
    "Scheme": "skos:Scheme",
    "hasEnd": {
      "@id": "w3ctime:hasEnd",
      "@type": "@id"
    },
    "hasBeginning": {
      "@id": "w3ctime:hasBeginning",
      "@type": "@id"
    },
    "isResultOf": {
      "@id": "http://www.w3.org/ns/sosa/isResultOf",
      "@type": "@id"
    },
    "SF_SamplingFeature": "http://def.isotc211.org/iso19156/2011/SamplingFeature#SF_SamplingFeature",
    "DimensionProperty": "http://purl.org/linked-data/cube#DimensionProperty",
    "alt": "http://www.w3.org/2003/01/geo/wgs84_pos#alt",
    "Acceleration": "http://purl.oclc.org/NET/ssnx/qu/dim#Acceleration",
    "hasSubSystem": {
      "@id": "http://www.w3.org/ns/ssn/hasSubSystem",
      "@type": "@id"
    },
    "Quantity": "http://qudt.org/schema/qudt/Quantity",
    "MassFlowRate": "http://purl.oclc.org/NET/ssnx/qu/dim#MassFlowRate",
    "qu.QuantityKind": "http://purl.oclc.org/NET/ssnx/qu/qu#QuantityKind",
    "SpatialObjectCollection": "http://www.opengis.net/ont/geosparql#SpatialObjectCollection",
    "Distance": "http://purl.oclc.org/NET/ssnx/qu/dim#Distance",
    "deprecated": "owl:deprecated",
    "Radiance": "http://purl.oclc.org/NET/ssnx/qu/dim#Radiance",
    "Duration": "w3ctime:Duration",
    "TIN": "http://www.opengis.net/ont/sf#TIN",
    "SurfaceDensity": "http://purl.oclc.org/NET/ssnx/qu/dim#SurfaceDensity",
    "wgs84.Point": "http://www.w3.org/2003/01/geo/wgs84_pos#Point",
    "editorialNote": "skos:editorialNote",
    "observes": {
      "@id": "http://www.w3.org/ns/sosa/observes",
      "@type": "@id"
    },
    "hasDeployment": {
      "@id": "http://www.w3.org/ns/ssn/hasDeployment",
      "@type": "@id"
    },
    "hasResult": {
      "@id": "http://www.w3.org/ns/sosa/hasResult",
      "@type": "@id"
    },
    "order": {
      "@id": "http://purl.org/linked-data/cube#order",
      "@type": "xsd:int"
    },
    "hasGeometry": {
      "@id": "http://www.opengis.net/ont/geosparql#hasGeometry",
      "@type": "@id"
    },
    "usedProcedure": {
      "@id": "http://www.w3.org/ns/sosa/usedProcedure",
      "@type": "@id"
    },
    "ssn.Property": "http://www.w3.org/ns/ssn/Property",
    "sfContains": {
      "@id": "http://www.opengis.net/ont/geosparql#sfContains",
      "@type": "@id"
    },
    "Density": "http://purl.oclc.org/NET/ssnx/qu/dim#Density",
    "LinearRing": "http://www.opengis.net/ont/sf#LinearRing",
    "Molality": "http://purl.oclc.org/NET/ssnx/qu/dim#Molality",
    "inXSDDateTimeStamp": {
      "@id": "w3ctime:inXSDDateTimeStamp",
      "@type": "xsd:dateTimeStamp"
    },
    "MeasureProperty": "http://purl.org/linked-data/cube#MeasureProperty",
    "PropertyKind": "http://purl.oclc.org/NET/ssnx/qu/qu#PropertyKind",
    "SpatialObject": "http://www.opengis.net/ont/geosparql#SpatialObject",
    "sliceStructure": {
      "@id": "http://purl.org/linked-data/cube#sliceStructure",
      "@type": "@id"
    },
    "hasFeatureOfInterest": {
      "@id": "http://www.w3.org/ns/sosa/hasFeatureOfInterest",
      "@type": "@id"
    },
    "NumberPerLength": "http://purl.oclc.org/NET/ssnx/qu/dim#NumberPerLength",
    "lat": "http://www.w3.org/2003/01/geo/wgs84_pos#lat",
    "VolumeFlowRate": "http://purl.oclc.org/NET/ssnx/qu/dim#VolumeFlowRate",
    "SpecificEntropy": "http://purl.oclc.org/NET/ssnx/qu/dim#SpecificEntropy",
    "CodedProperty": "http://purl.org/linked-data/cube#CodedProperty",
    "observedProperty": {
      "@id": "http://www.w3.org/ns/sosa/observedProperty",
      "@type": "@id"
    },
    "slice": {
      "@id": "http://purl.org/linked-data/cube#slice",
      "@type": "@id"
    },
    "madeObservation": {
      "@id": "http://www.w3.org/ns/sosa/madeObservation",
      "@type": "@id"
    },
    "unit": {
      "@id": "http://qudt.org/schema/qudt/unit",
      "@type": "@id"
    },
    "date": "dct:date",
    "isPropertyOf": {
      "@id": "http://www.w3.org/ns/ssn/isPropertyOf",
      "@type": "@id"
    },
    "ObservationGroup": "http://purl.org/linked-data/cube#ObservationGroup",
    "Sample": "http://www.w3.org/ns/sosa/Sample",
    "DataSet": "http://purl.org/linked-data/cube#DataSet",
    "PolyhedralSurface": "http://www.opengis.net/ont/sf#PolyhedralSurface",
    "ObservableProperty": "http://www.w3.org/ns/sosa/ObservableProperty",
    "deployedSystem": {
      "@id": "http://www.w3.org/ns/ssn/deployedSystem",
      "@type": "@id"
    },
    "System": "http://www.w3.org/ns/ssn/System",
    "unitKind": {
      "@id": "http://purl.oclc.org/NET/ssnx/qu/qu#unitKind",
      "@type": "@id"
    },
    "dimension": {
      "@id": "http://purl.org/linked-data/cube#dimension",
      "@type": "@id"
    },
    "RadianceExposure": "http://purl.oclc.org/NET/ssnx/qu/dim#RadianceExposure",
    "VelocityOrSpeed": "http://purl.oclc.org/NET/ssnx/qu/dim#VelocityOrSpeed",
    "deployedOnPlatform": {
      "@id": "http://www.w3.org/ns/ssn/deployedOnPlatform",
      "@type": "@id"
    },
    "inXSDDate": {
      "@id": "w3ctime:inXSDDate",
      "@type": "xsd:date"
    },
    "GFI_DomainFeature": "http://def.isotc211.org/iso19156/2011/GeneralFeatureInstance#GFI_DomainFeature",
    "Actuation": "http://www.w3.org/ns/sosa/Actuation",
    "observation": {
      "@id": "http://purl.org/linked-data/cube#observation",
      "@type": "@id"
    },
    "Dimensionless": "http://purl.oclc.org/NET/ssnx/qu/dim#Dimensionless",
    "Area": "http://purl.oclc.org/NET/ssnx/qu/dim#Area",
    "Sampling": "http://www.w3.org/ns/sosa/Sampling",
    "Power": "http://purl.oclc.org/NET/ssnx/qu/dim#Power",
    "OM_Observation": "http://def.isotc211.org/iso19156/2011/Observation#OM_Observation",
    "prefLabel": "skos:prefLabel",
    "Surface": "http://www.opengis.net/ont/sf#Surface",
    "sliceKey": {
      "@id": "http://purl.org/linked-data/cube#sliceKey",
      "@type": "@id"
    },
    "inScheme": "skos:inScheme",
    "dct.description": "dct:description",
    "MultiCurve": "http://www.opengis.net/ont/sf#MultiCurve",
    "hasQuantityKind": {
      "@id": "http://qudt.org/schema/qudt/hasQuantityKind",
      "@type": "@id"
    },
    "DataStructureDefinition": "http://purl.org/linked-data/cube#DataStructureDefinition",
    "qb.Observation": "http://purl.org/linked-data/cube#Observation",
    "EnergyDensity": "http://purl.oclc.org/NET/ssnx/qu/dim#EnergyDensity",
    "Sensor": "http://www.w3.org/ns/sosa/Sensor",
    "hasSimpleResult": "http://www.w3.org/ns/sosa/hasSimpleResult",
    "unitType": {
      "@id": "w3ctime:unitType",
      "@type": "@id"
    },
    "componentProperty": {
      "@id": "http://purl.org/linked-data/cube#componentProperty",
      "@type": "@id"
    },
    "isFeatureOfInterestOf": {
      "@id": "http://www.w3.org/ns/sosa/isFeatureOfInterestOf",
      "@type": "@id"
    },
    "sf.Geometry": "http://www.opengis.net/ont/sf#Geometry",
    "schema.Person": "https://schema.org/Person",
    "Observation": "http://www.w3.org/ns/sosa/Observation",
    "schema.name": "https://schema.org/name",
    "QuantityKind": "http://qudt.org/schema/qudt/QuantityKind",
    "geojson": "https://purl.org/geojson/vocab#",
    "oa": "http://www.w3.org/ns/oa#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "dct": "http://purl.org/dc/terms/",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "w3ctime": "http://www.w3.org/2006/time#",
    "rec": "https://www.opengis.net/def/ogc-api/records/",
    "dcat": "http://www.w3.org/ns/dcat#",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "owl": "http://www.w3.org/2002/07/owl#",
    "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    "dctype": "http://purl.org/dc/dcmitype/",
    "vcard": "http://www.w3.org/2006/vcard/ns#",
    "prov": "http://www.w3.org/ns/prov#",
    "foaf": "http://xmlns.com/foaf/0.1/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://ogcincubator.github.io/iliad-apis-features/build/annotated/hosted/iliad/api/features/stac_multidim_data/context.jsonld)

## Sources

* [Reference to ILIAD](https://example.com/sources/1)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/iliad-apis-features](https://github.com/ogcincubator/iliad-apis-features)
* Path: `_sources/stac_multidim_data`

