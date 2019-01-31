// from data.js
var tableData = data;

// Get references to the tbody element, input field and button
var tbody = d3.select("tbody");
var button = d3.select("#filter-btn");

// Create a function to display the data
function displayData(tableData){

  var row = tbody.append("tr");
  
  Object.entries(tableData).forEach(function([key, value]) {

    var cell = tbody.append("td")
    cell.text(value);
    
  }); 
};

// Display data
data.forEach(displayData);

// Create a function to filter using the
button.on("click", function() {

  // Prevent the page from refreshing
  d3.event.preventDefault()

  // Select the input element and get the raw HTML node
  var inputElement = d3.select("#datetime")

  // Get the value property of the input element
  var inputValue = inputElement.property("value")

  console.log(inputValue)

  var filteredData = tableData.filter(tableData => tableData.datetime === inputValue)

  console.log(filteredData)

  list = filteredData.lenght 

  console.log(list)

  if (list === 0){
    data.forEach(displayData);
  }

  else{
    tbody.html("")
    filteredData.forEach(displayData);
  }

});