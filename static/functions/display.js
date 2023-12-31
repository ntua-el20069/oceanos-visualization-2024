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
                    radius: 70 + (25 * totalWidth) / 1850
                });
            }
        
            else if (!data.slider) document.querySelector(`#${data.id}`).textContent = data.value; // for numeric data
            // for allData
            const errorElement = document.querySelector(`#${data.id}-error`);
            errorElement.textContent = data.error;
            if (data.error != noError) errorElement.style.visibility = 'visible';
            else errorElement.style.visibility = 'hidden';
        }
    });
}
