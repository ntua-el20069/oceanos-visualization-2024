function display(){
    var totalWidth = window.innerWidth;
    console.log(`Total screen width: ${totalWidth}`);
    console.log(`Total screen height: ${window.innerHeight}`);
    $(document).ready(function () {             // Here I use the function from the roundSlider library
        for (data of allData)  {
            if (data.slider){ // for  data that require roundSlider
                if (data.value > data.limit) color = above_limit_color;
                else color = regular_color;
                
                $(`#${data.id}`).roundSlider({
                    svgMode: true,
                    value: data.value,                          // this is what changes ... (e.g. the value of tempMosfet)
                    sliderType: "min-range",
                    circleShape: "half-top",
                    min: data.min,
                    max: data.max,
                    step: data.step,
                    readOnly: true,
                    rangeColor: color,
                    radius: 80 + (30 * totalWidth) / 1850
                });
                
                if (data.value > data.max || data.value < data.min) {
                    // with the below code, I can change the value of the tooltip, meaning the value of the roundSlider when it is above the limit
                    var dataElement = document.getElementById(`${data.id}`);
                    var tooltipElement = dataElement.querySelector('.rs-tooltip.rs-tooltip-text.rs-editable');
                    console.log(tooltipElement);
                    tooltipElement.textContent = data.value;
                    tooltipElement.style.color = 'red';
                }
            }
        
            else if (!data.slider) {    // for numeric data
                var dataElement = document.querySelector(`#${data.id}`);
                dataElement.textContent = data.value;  
                if (data.value > data.max || data.value < data.min)  dataElement.style.color = 'red';
            }
            // for allData
            
            // This is for the error messages
            /*
            const errorElement = document.querySelector(`#${data.id}-error`);
            errorElement.textContent = data.error;
            if (data.error != noError) errorElement.style.visibility = 'visible';
            else errorElement.style.visibility = 'hidden';
            */
        }
    });
}
