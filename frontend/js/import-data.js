$.ajax({ 
  url: 'https://s3.amazonaws.com/jhmede-fa-site/data.json',
  dataType: 'json',
  crossDomain: true,
  success: function (data) {
    populateTable(data);
  }
})

function populateTable(data) {    
  for (var data of data) {
    var trTable = document.createElement("tr");

    var tdInfoPhoto = document.createElement("td");
    var tdInfoName = document.createElement("td");
    var tdInfoSimilarity = document.createElement("td");      

    tdInfoName.textContent = data.name;
    tdInfoSimilarity.textContent = data.similarity;
    tdInfoPhoto = document.createElement("img");
    tdInfoPhoto.height = 300;
    tdInfoPhoto.width = 268;
    tdInfoPhoto.src = 'https://s3.amazonaws.com/jhmede-fa-images/' + data.name + '.jpg';

    trTable.appendChild(tdInfoPhoto);
    trTable.appendChild(tdInfoName);
    trTable.appendChild(tdInfoSimilarity);
    
    var table = document.querySelector("#peoples-table");

    table.appendChild(trTable);
  }
}
