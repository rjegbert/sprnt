from tethys_sdk.base import TethysAppBase, url_map_maker
from tethys_sdk.app_settings import SpatialDatasetServiceSetting


class Sprnt(TethysAppBase):
    """
    Tethys app class for SPRNT.
    """

    name = 'SPRNT Viewer'
    index = 'sprnt:home'
    icon = 'sprnt/images/SPRNTlogo.JPG'
    package = 'sprnt'
    root_url = 'sprnt'
    color = '#3099fc'
    description = 'This app is a demonstration of the SPRNT dynamic river model. SPRNT means Simulation Program for River Networks. It uses the Saint-Venant equations to take into account the hydraulics as well as the hydrology in river modeling.'
    tags = '&quot;Hydrology&quot;,&quot;Hydraulics&quot;,&quot;River Modeling&quot;,&quot;SPRNT&quot;'
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='sprnt',
                controller='sprnt.controllers.home'
            ),
            UrlMap(
                name='remote_sensing',
                url='sprnt/remote_sensing',
                controller='sprnt.controllers.remote_sensing'
            ),
            UrlMap(
                name='hand',
                url='sprnt/hand',
                controller='sprnt.controllers.hand'
            ),
            UrlMap(
                name='hurricane_matthew',
                url='sprnt/add',
                controller='sprnt.controllers.hurricane_matthew'
            ),
        )



        return url_maps


    def spatial_dataset_service_settings(self):
        """
        Example spatial_dataset_service_settings method.
        """
        sds_settings = (
            SpatialDatasetServiceSetting(
                name='main_geoserver',
                description='spatial dataset service for app to use',
                engine=SpatialDatasetServiceSetting.GEOSERVER,
                required=True,
            ),
        )

        return sds_settings