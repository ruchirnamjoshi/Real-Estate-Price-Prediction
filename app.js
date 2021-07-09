function onClickedEstimatePrice() {
  //console.log("Estimate price button clicked");
    
    var itemWeight = document.getElementById("iw");
    var itemVisibility = document.getElementById("iv");
    var itemMRP = document.getElementById("im");
    var outletIdentifier = document.getElementById("oi");
    var years = document.getElementById("oa");
    var itemFatcontent = document.getElementById("ifc");
    var itemType = document.getElementById("it");
    var outletSize = document.getElementById("os");
    var outletLocationtype = document.getElementById("olt");
    var outletType = document.getElementById("ot");
    var newType = document.getElementById("ft");    
    var estPrice = document.getElementById("uiEstimatedPrice");


  var url = "http://127.0.0.1:5000/predict_sales_price"; //Use this if you are NOT using nginx which is first 7 tutorials
  //var url = "/api/predict_home_price"; // Use this if  you are using nginx. i.e tutorial 8 and onwards

  $.post(url, {
      
      item_weight: parseFloat(itemWeight.value),
      item_visibility: parseFloat(itemVisibility.value),
      item_MRP: parseFloat(itemMRP.value),
      outlet_identifier: parseFloat(outletIdentifier.value),
      years: parseFloat(years.value),
      item_fat_content: itemFatcontent.value,
      item_type: itemType.value,
      outlet_size: outletSize.value,
      outlet_location_type: outletLocationtype.value,
      outlet_type: outletType.value,
      new_type: newType.value
      
  },function(data, status) {
      console.log(data.estimated_price);
      estPrice.innerHTML = "<h2>" + data.estimated_price.toString() + " Lakh</h2>";
      console.log(status);
  });
}