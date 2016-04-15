function initialize() {
    
    var myCenter=new google.maps.LatLng(51.508742,-0.120850);
    
    
    var mapProp1 = {
    center:myCenter,
    zoom:10,
    mapTypeId:google.maps.MapTypeId.ROADMAP
    };
    
    var mapProp2 = {
    center:myCenter,
    zoom:10,
    mapTypeId:google.maps.MapTypeId.ROADMAP
    };
    
    var mapProp3 = {
    center:myCenter,
    zoom:10,
    mapTypeId:google.maps.MapTypeId.ROADMAP
    };
    
    
    var mapProp4 = {
    center:myCenter,
    zoom:10,
    mapTypeId:google.maps.MapTypeId.ROADMAP
    };
    
    var mapProp5 = {
    center:myCenter,
    zoom:10,
    mapTypeId:google.maps.MapTypeId.ROADMAP
    };
    
    var mapProp6 = {
    center:myCenter,
    zoom:10,
    mapTypeId:google.maps.MapTypeId.ROADMAP
    };
    
    var mapProp7 = {
    center:myCenter,
    zoom:10,
    mapTypeId:google.maps.MapTypeId.ROADMAP
    };
    
    
    var mapProp8 = {
    center:myCenter,
    zoom:10,
    mapTypeId:google.maps.MapTypeId.ROADMAP
    };
    
    
    var mapProp9 = {
    center:myCenter,
    zoom:10,
    mapTypeId:google.maps.MapTypeId.ROADMAP
    };
    
    
    var mapProp10 = {
    center:myCenter,
    zoom:10,
    mapTypeId:google.maps.MapTypeId.ROADMAP
    };
    
    
    var map1=new google.maps.Map(document.getElementById("id1"),mapProp1);
    
    var map2=new google.maps.Map(document.getElementById("id2"),mapProp2);
    
    var map2=new google.maps.Map(document.getElementById("id3"),mapProp2);
    
    var map2=new google.maps.Map(document.getElementById("id4"),mapProp2);
    
    var map2=new google.maps.Map(document.getElementById("id5"),mapProp2);
    
    var map2=new google.maps.Map(document.getElementById("id6"),mapProp2);
    
    var map2=new google.maps.Map(document.getElementById("id7"),mapProp2);
    
    var map2=new google.maps.Map(document.getElementById("id8"),mapProp2);
    
    var map2=new google.maps.Map(document.getElementById("id9"),mapProp2);
    
    var map2=new google.maps.Map(document.getElementById("id10"),mapProp2);
    
    
    /*
     var marker=new google.maps.Marker({
     position:myCenter,
     });
     marker.setMap(map);
     
     */
    
}

google.maps.event.addDomListener(window, 'load', initialize);

