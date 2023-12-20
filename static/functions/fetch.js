function reloadPage() {
    fetch('/reload') // Fetch the '/reload' endpoint
    .then(response => response.json())
    .then(jsonData => {
        console.log(jsonData);
        for (data of datalist.concat(numericData)) {
            data.change(parseFloat(jsonData[data.id]), noError);
        }
        display();
    })
    .catch(error => {
        console.error('Error fetching /reload:', error);
    });
}

function finalFetch(csvURL){
    fetchAndParseCSV(csvURL)
    .then(dataSet => {
        if (dataSet) {
            console.log('Parsed CSV data:', dataSet);
            console.log('First 3 rows');
            for (let i=0; i<3; i++) {
                let row = dataSet[i];
                console.log(`row ${i}:`);
                for (field of fieldnames) console.log(`${field}: ${row[field]}`);
            }
            localDataSet = dataSet;
    
        } else {
            console.log('Failed to parse CSV data.');
            localDataSet = null;
        }
        });
}
  