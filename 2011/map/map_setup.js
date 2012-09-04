var map, vector_layer, selectControl ;
function init_map() {
    // Basic map setup
    OpenLayers.Lang.setCode('fr');
    map = new OpenLayers.Map('map', {
        projection: new OpenLayers.Projection('EPSG:900913'),
        controls: [
            new OpenLayers.Control.Navigation(),
            new OpenLayers.Control.PanZoomBar(),
            new OpenLayers.Control.LayerSwitcher({'roundedCorner': false}),
            new OpenLayers.Control.ScaleLine({'bottomOutUnits': ''}),
            new OpenLayers.Control.Attribution()
        ]
    });
    map.addLayer(new OpenLayers.Layer.OSM('OpenStreetMap', [
        'http://a.tile.openstreetmap.org/${z}/${x}/${y}.png',
        'http://b.tile.openstreetmap.org/${z}/${x}/${y}.png',
        'http://c.tile.openstreetmap.org/${z}/${x}/${y}.png',
    ]));

    // Vector overlay
    vector_layer = new OpenLayers.Layer.Vector('DjangoCong', {
        'styleMap': new OpenLayers.StyleMap({
            'pointRadius': 10,
            'externalGraphic': 'map/symbol-${type}.png',
            'label': '${name}',
            'labelYOffset': -16,
            'fontFamily': 'sans-serif',
            'fontSize': '10px'
        })
    });
    map.addLayer(vector_layer);
    OpenLayers.Request.GET({
        'url': 'map/lieux.json',
        'success': function(request) {
            var parser = new OpenLayers.Format.GeoJSON();
            vector_layer.addFeatures(parser.read(request.responseText));
        }
    });

    // Popups
    selectControl = new OpenLayers.Control.SelectFeature(vector_layer, {
        onSelect: function(feature) {
            content = '';
            content += '<div><p><a href="';
            content += feature.attributes.url;
            content += '">';
            content += feature.attributes.name;
            content += '</a></p><p>';
            content += feature.attributes.description;
            content += '</p></div>';
            popup = new OpenLayers.Popup.Anchored('infobulle',
                            feature.geometry.getBounds().getCenterLonLat(),
                            null,
                            content,
                            null,
                            true,
                            function(e) {
                                selectControl.unselect(feature);
                            });
            popup.autoSize = true;
            feature.popup = popup;
            map.addPopup(popup);
        },
        onUnselect: function(feature) {
            map.removePopup(feature.popup);
            feature.popup.destroy();
            feature.popup = null;
        }
    });
    map.addControl(selectControl);
    selectControl.activate();

    // Initial map view
    map.zoomToExtent(new OpenLayers.Bounds(594343.21791613, 5352193.1472484, 608579.6144317, 5367232.1325609));

    //HACK: setting style in CSS with !important is a better solution but does not work properly in IE6/7
    map.controls[4].div.style.bottom = '3px';
    map.controls[4].div.style.top = 'auto';
    map.controls[2].layersDiv.style.color = '#777';
    map.controls[2].layersDiv.style.backgroundColor = '#fff';
}
OpenLayers.Event.observe(window, 'load', init_map);
