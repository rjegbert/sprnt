/**
 * Created by ryan on 7/17/17.
 */


$(document).ready(function(){

    // Bind to the change event of the check box
    $('#usgsHWM').on('change', function(e){
        var checked = e.target.checked;
        console.log(checked);
        var map = TETHYS_MAP_VIEW.getMap();
        var layers = map.getLayers();
        var streams = layers.item(4);
        streams.setVisible(checked);
    });
    
    // Bind to the change event of the check box
    $('#TrainingLabels').on('change', function(e){
        var checked = e.target.checked;
        console.log(checked);
        var map = TETHYS_MAP_VIEW.getMap();
        var layers = map.getLayers();
        var streams = layers.item(3);
        streams.setVisible(checked);
    });
    
    
    // Bind to the change event of the check box
    $('#ClassifiedRaster').on('change', function(e){
        var checked = e.target.checked;
        console.log(checked);
        var map = TETHYS_MAP_VIEW.getMap();
        var layers = map.getLayers();
        var streams = layers.item(2);
        streams.setVisible(checked);
    });
    
    // Bind to the change event of the check box
    $('#Predictors').on('change', function(e){
        var checked = e.target.checked;
        console.log(checked);
        var map = TETHYS_MAP_VIEW.getMap();
        var layers = map.getLayers();
        var streams = layers.item(1);
        streams.setVisible(checked);
    });
});


// //http://geoserver.byu.edu/arcgis/services/EgbertNation/SPRNT/MapServer/WmsServer?
// // http://geoserver.byu.edu/arcgis/services/West_Virginia_Flood/Flood_' + decimal_value + '/MapServer/WmsServer?
//
//
// function showhidelayer(i){
//     if(document.getElementById(i).checked == true) {
//         map.getLayers().item(i).setVisible(true);
//     } else {
//         map.getLayers().item(i).setVisible(false);
//     }
//   }