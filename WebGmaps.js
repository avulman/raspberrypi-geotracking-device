/**
 * @license
 * Copyright 2019 Google LLC. All Rights Reserved.
 * SPDX-License-Identifier: Apache-2.0
 */
let map;

var lat;
var lang;

function getFileFromServer(url, doneCallback) {
  var xhr;

  xhr = new XMLHttpRequest();
  xhr.onreadystatechange = handleStateChange;
  xhr.open("GET", url, true);
  xhr.send();

  function handleStateChange() {
    if (xhr.readyState === 4) {
      doneCallback(xhr.status == 200 ? xhr.responseText : null);
    }
  }
}

getFileFromServer("path/to/file", function(text) {
    if (text === null) {
        // An error occurred
    }
    else {
        const corArr = text.split(",");
        lat = corArr[0];
        lang = corArr[1];
    }
});




async function initMap() {
  const {
    Map
  } = await google.maps.importLibrary("maps");

  map = new Map(document.getElementById("map"), {
    center: {
      lat: lat,
      lng: lang
    },
    zoom: 8,
  });
}

initMap();