from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from tethys_sdk.gizmos import *
from .app import Sprnt as app

#Geoserver imports
import random
import string

WORKSPACE = 'sprnt'
GEOSERVER_URI = 'http://byu.edu/sprnt'

@login_required()
def home(request):
    """
    Controller for the app home page.
    """
    view_options = MVView(
        projection='EPSG:4326',
        center=[-77.986177, 35.380000],
        zoom=12.1,
        maxZoom=18,
        minZoom=2
    )

    map_layers = []

    SPRNT_HAND = MVLayer(
        source='TileArcGISRest',
        options={
            'url': 'http://geoserver.byu.edu/arcgis/rest/services/EgbertNation/SPRNT_HAND/MapServer'},
        legend_title='SPRNT HAND',
        legend_extent=[-173, 17, -65, 72],
        feature_selection=True
    )

    NWM_HAND = MVLayer(
        source='TileArcGISRest',
        options={
            'url': 'http://geoserver.byu.edu/arcgis/rest/services/EgbertNation/NWM_HAND/MapServer'},
        legend_title='NWM HAND',
        legend_extent=[-173, 17, -65, 72],
        feature_selection=True
    )

    ValidationMap = MVLayer(
        source='TileArcGISRest',
        options={
            'url': 'http://geoserver.byu.edu/arcgis/rest/services/EgbertNation/ValidationMap/MapServer'},
        legend_title='Validation Map',
        legend_extent=[-173, 17, -65, 72],
        feature_selection=True
    )

    Intersect = MVLayer(
        source='TileArcGISRest',
        options={
            'url': 'http://geoserver.byu.edu/arcgis/rest/services/EgbertNation/Intersect/MapServer'},
        legend_title='Intersect',
        legend_extent=[-173, 17, -65, 72],
        feature_selection=False,
        layer_options={'visible': False}
    )

    map_layers.append(ValidationMap)
    map_layers.append(Intersect)
    map_layers.append(SPRNT_HAND)
    map_layers.append(NWM_HAND)

    sprnt_map = MapView(
        height='100%',
        width='100%',
        layers=map_layers,
        basemap={'Bing': {'key': '5TC0yID7CYaqv3nVQLKe~xWVt4aXWMJq2Ed72cO4xsA~ApdeyQwHyH_btMjQS1NJ7OHKY8BK-W-EMQMrIavoQUMYXeZIQOUURnKGBOC7UCt4', 'imagerySet': 'Aerial'}},
        legend=True,
        view=view_options

    )

    context = {"sprnt_map":sprnt_map,
               "view_options":view_options
               }

    return render(request, 'sprnt/home.html', context)

@login_required()
def remote_sensing(request):
    """
    Controller for the Remote Sensing page.
    """

    # Define view options

    view_options = MVView(
        projection='EPSG:4326',
        center=[-77.986177, 35.377625],
        zoom=12,
        maxZoom=18,
        minZoom=2
    )

    map_layers = []

    usgsHWM = MVLayer(
        source='TileArcGISRest',
        options={
            'url': 'http://geoserver.byu.edu/arcgis/rest/services/EgbertNation/usgsHWM/MapServer'},
        legend_title='USGS High Water Marks',
        legend_extent=[-173, 17, -65, 72],
        feature_selection=True
    )

    TrainingLabels = MVLayer(
        source='TileArcGISRest',
        options={
            'url': 'http://geoserver.byu.edu/arcgis/rest/services/EgbertNation/TrainingLabels/MapServer'},
        legend_title='Training Labels',
        legend_extent=[-173, 17, -65, 72],
        feature_selection=True
    )

    ClassifiedRaster = MVLayer(
        source='TileArcGISRest',
        options={
            'url': 'http://geoserver.byu.edu/arcgis/rest/services/EgbertNation/ClassifiedRaster/MapServer'},
        legend_title='Classified Raster',
        legend_extent=[-173, 17, -65, 72],
        feature_selection=False
    )

    Predictors = MVLayer(
        source='TileArcGISRest',
        options={
            'url': 'http://geoserver.byu.edu/arcgis/rest/services/EgbertNation/Predictors/MapServer'},
        legend_title='Predictors',
        legend_extent=[-173, 17, -65, 72],
        feature_selection=False,
        layer_options = {'visible': False}
    )

    map_layers.append(usgsHWM)
    map_layers.append(TrainingLabels)
    map_layers.append(ClassifiedRaster)
    map_layers.append(Predictors)

    # # Define map view options
    # watershed_map = MapView(
    #     height='100%',
    #     width='100%',
    #     controls=['ZoomSlider', 'Rotate', 'FullScreen',
    #               {'ZoomToExtent': {'projection': 'EPSG:4326', 'extent': [-130, 22, -65, 54]}}],
    #     layers=map_layers,
    #     view=view_options,
    #     basemap={'Bing': {
    #         'key': '5TC0yID7CYaqv3nVQLKe~xWVt4aXWMJq2Ed72cO4xsA~ApdeyQwHyH_btMjQS1NJ7OHKY8BK-W-EMQMrIavoQUMYXeZIQOUURnKGBOC7UCt4',
    #         'imagerySet': 'Aerial'}},
    #     legend=True
    # )

    # view_options = MVView(
    #     projection='EPSG:4326',
    #     center=[-77.986177, 35.377625],
    #     zoom=12,
    #     maxZoom=18,
    #     minZoom=2
    # )
    #
    map_options = MapView(
        height='700px',
        width='100%',
        layers=map_layers,
        basemap={'Bing': {'key': '5TC0yID7CYaqv3nVQLKe~xWVt4aXWMJq2Ed72cO4xsA~ApdeyQwHyH_btMjQS1NJ7OHKY8BK-W-EMQMrIavoQUMYXeZIQOUURnKGBOC7UCt4', 'imagerySet': 'AerialWithLabels'}},
        legend=False,
        view=view_options
    )

    context = {
        'map_options': map_options,
        'view_options': view_options
    }

    return render(request, 'sprnt/remote_sensing.html', context)

@login_required()
def hand(request):
    """
    Controller for the HAND page.
    """

    view_options = MVView(
        projection='EPSG:4326',
        center=[-77.986177, 35.392000],
        zoom=11.6,
        maxZoom=18,
        minZoom=2
    )

    map_layers = []

    Gboro_flowlines = MVLayer(
        source='TileArcGISRest',
        options={
            'url': 'http://geoserver.byu.edu/arcgis/rest/services/EgbertNation/Gboro_flowlines/MapServer'},
        legend_title='Flowlines',
        legend_extent=[-173, 17, -65, 72],
        feature_selection=True
    )

    HandCatch1 = MVLayer(
        source='TileArcGISRest',
        options={
            'url': 'http://geoserver.byu.edu/arcgis/rest/services/EgbertNation/HandCatch1/MapServer'},
        legend_title='Hand Catch 1',
        legend_extent=[-173, 17, -65, 72],
        feature_selection=False,
        layer_options = {'visible': False}
    )

    HandCatch5 = MVLayer(
        source='TileArcGISRest',
        options={
            'url': 'http://geoserver.byu.edu/arcgis/rest/services/EgbertNation/HandCatch5/MapServer'},
        legend_title='Hand Catch 5',
        legend_extent=[-173, 17, -65, 72],
        feature_selection=False
    )

    HandCatch20 = MVLayer(
        source='TileArcGISRest',
        options={
            'url': 'http://geoserver.byu.edu/arcgis/rest/services/EgbertNation/HandCatch20a/MapServer'},
        legend_title='Hand Catch 20',
        legend_extent=[-173, 17, -65, 72],
        feature_selection=False,
        layer_options = {'visible': False}
    )

    HandMap1 = MVLayer(
        source='TileArcGISRest',
        options={
            'url': 'http://geoserver.byu.edu/arcgis/rest/services/EgbertNation/HandMap1/MapServer'},
        legend_title='Hand Map 1',
        legend_extent=[-173, 17, -65, 72],
        feature_selection=False,
        layer_options = {'visible': False}
    )

    HandMap5 = MVLayer(
        source='TileArcGISRest',
        options={
            'url': 'http://geoserver.byu.edu/arcgis/rest/services/EgbertNation/HandMap5/MapServer'},
        legend_title='Hand Map 5',
        legend_extent=[-173, 17, -65, 72],
        feature_selection=False
    )

    HandMap20 = MVLayer(
        source='TileArcGISRest',
        options={
            'url': 'http://geoserver.byu.edu/arcgis/rest/services/EgbertNation/HandMap20/MapServer'},
        legend_title='Hand Map 20',
        legend_extent=[-173, 17, -65, 72],
        feature_selection=False,
        layer_options = {'visible': False}
    )

    map_layers.append(HandCatch1)
    map_layers.append(HandCatch5)
    map_layers.append(HandCatch20)
    map_layers.append(Gboro_flowlines)
    map_layers.append(HandMap1)
    map_layers.append(HandMap5)
    map_layers.append(HandMap20)


    # # Define map view options
    # watershed_map = MapView(
    #     height='100%',
    #     width='100%',
    #     controls=['ZoomSlider', 'Rotate', 'FullScreen',
    #               {'ZoomToExtent': {'projection': 'EPSG:4326', 'extent': [-130, 22, -65, 54]}}],
    #     layers=map_layers,
    #     view=view_options,
    #     basemap={'Bing': {
    #         'key': '5TC0yID7CYaqv3nVQLKe~xWVt4aXWMJq2Ed72cO4xsA~ApdeyQwHyH_btMjQS1NJ7OHKY8BK-W-EMQMrIavoQUMYXeZIQOUURnKGBOC7UCt4',
    #         'imagerySet': 'Aerial'}},
    #     legend=True
    # )

    # view_options = MVView(
    #     projection='EPSG:4326',
    #     center=[-77.986177, 35.377625],
    #     zoom=12,
    #     maxZoom=18,
    #     minZoom=2
    # )
    #
    map_options = MapView(
        height='700px',
        width='100%',
        layers=map_layers,
        basemap={'Bing': {
            'key': '5TC0yID7CYaqv3nVQLKe~xWVt4aXWMJq2Ed72cO4xsA~ApdeyQwHyH_btMjQS1NJ7OHKY8BK-W-EMQMrIavoQUMYXeZIQOUURnKGBOC7UCt4',
            'imagerySet': 'AerialWithLabels'}},
        legend=False,
        view=view_options
    )

    context = {
        'map_options': map_options,
        'view_options': view_options
    }
    return render(request, 'sprnt/hand.html', context)

@login_required()
def hurricane_matthew(request):
    """
    Controller for the Hurricane Matthew page.
    """

    context = {}
    return render(request, 'sprnt/hurricane_matthew.html', context)