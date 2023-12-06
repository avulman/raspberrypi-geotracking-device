var lat;
var lang;

function getFile(){
  var file = "pCor.txt";
  var reader = new FileReader(file);
  reader.onload = function(e){
    var contents = e.target.result;
    const tArray = contents.split(",");
    lat = tArray[0];
    lang = tArray[1];
  }
}
