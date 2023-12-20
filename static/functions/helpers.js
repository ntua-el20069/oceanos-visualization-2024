function generateRandomFloat(min, max, step) {
    var randomNumber = Math.random() * (max - min) + min;
    if (step >= 0.1) return Math.round(randomNumber * 10) / 10;
    else if (step >= 0.01) return Math.round(randomNumber * 100) / 100;
    else return randomNumber;
}  

// fetch CSV with JavaScript
// Function to fetch and parse CSV data with a different delimiter (e.g. ;)
async function fetchAndParseCSV(url) {
    try {
      const delimiter = ',';    // Change delimiter here
      const response = await fetch(url);
      const data = await response.text();
  
      // Splitting CSV rows using the semicolon delimiter
      const rows = data.split('\n');
      const headers = rows[0].split(delimiter); // Change delimiter here
      const result = [];
  
      for (let i = 1; i < rows.length; i++) {
        const values = rows[i].split(delimiter); // Change delimiter here
        if (values.length === headers.length) {
          const obj = {};
          for (let j = 0; j < headers.length; j++) {
            obj[headers[j]] = values[j];
          }
          result.push(obj);
        }
      }
  
      return result;
    } catch (error) {
      console.error('Error fetching or parsing CSV:', error);
      return null;
    }
  }
  