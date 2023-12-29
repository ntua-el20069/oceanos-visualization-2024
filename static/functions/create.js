const parent = document.querySelector('.grid-container');

for (data of numericData.concat(datalist)){
    
    let dataDiv = document.createElement('div');
    dataDiv.classList.add('visualization');

    let h3Element = document.createElement('h3');
    h3Element.textContent = data.definition;

    let errorElement = document.createElement('output');
    errorElement.id = `${data.id}-error`;
    errorElement.style.display = 'block';
    errorElement.style.visibility = 'visible';
    errorElement.style.color = 'red';
    errorElement.textContent = data.error;
    

    dataDiv.appendChild(h3Element);
    
    if (numericData.includes(data)){
        
        let pElement = document.createElement('p');
        pElement.classList.add('numeric');
        pElement.id = data.id;
        pElement.textContent = data.value;

        dataDiv.appendChild(pElement);
    }
    else {
        let containerDiv = document.createElement('div');
        containerDiv.classList.add('container');

        let controlDiv = document.createElement('div');
        controlDiv.classList.add('control');

        let shapeDiv = document.createElement('div');
        shapeDiv.id = data.id;

        // Append elements to construct the structure
        controlDiv.appendChild(shapeDiv);
        containerDiv.appendChild(controlDiv);
        dataDiv.appendChild(containerDiv);
    }
    
    dataDiv.appendChild(errorElement);
    // Add the constructed element to the document body or another parent element
    parent.appendChild(dataDiv);
}

   