/**
 * Created by ryan on 7/17/17.
 */


$(document).ready(function(){

    // Bind to the change event of the check box
    $('#HandCatch1').on('change', function(e){
        var checked = e.target.checked;
        console.log(checked);
        var map = TETHYS_MAP_VIEW.getMap();
        var layers = map.getLayers();
        var streams = layers.item(7);
        streams.setVisible(checked);
    });

    // Bind to the change event of the check box
    $('#HandCatch5').on('change', function(e){
        var checked = e.target.checked;
        console.log(checked);
        var map = TETHYS_MAP_VIEW.getMap();
        var layers = map.getLayers();
        var streams = layers.item(6);
        streams.setVisible(checked);
    });

    // Bind to the change event of the check box
    $('#HandCatch20').on('change', function(e){
        var checked = e.target.checked;
        console.log(checked);
        var map = TETHYS_MAP_VIEW.getMap();
        var layers = map.getLayers();
        var streams = layers.item(5);
        streams.setVisible(checked);
    });

    // Bind to the change event of the check box
    $('#Gboro_flowlines').on('change', function(e){
        var checked = e.target.checked;
        console.log(checked);
        var map = TETHYS_MAP_VIEW.getMap();
        var layers = map.getLayers();
        var streams = layers.item(4);
        streams.setVisible(checked);
    });

    // Bind to the change event of the check box
    $('#HandMap1').on('change', function(e){
        var checked = e.target.checked;
        console.log(checked);
        var map = TETHYS_MAP_VIEW.getMap();
        var layers = map.getLayers();
        var streams = layers.item(3);
        streams.setVisible(checked);
    });

    // Bind to the change event of the check box
    $('#HandMap5').on('change', function(e){
        var checked = e.target.checked;
        console.log(checked);
        var map = TETHYS_MAP_VIEW.getMap();
        var layers = map.getLayers();
        var streams = layers.item(2);
        streams.setVisible(checked);
    });
    
    // Bind to the change event of the check box
    $('#HandMap20').on('change', function(e){
        var checked = e.target.checked;
        console.log(checked);
        var map = TETHYS_MAP_VIEW.getMap();
        var layers = map.getLayers();
        var streams = layers.item(1);
        streams.setVisible(checked);
    });

    
    // Selection stuff
    function my_callback(points_layer, lines_layer, polygons_layer) {
       console.log(polygons_layer);
    }

    TETHYS_MAP_VIEW.onSelectionChange(my_callback);
});