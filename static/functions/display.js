
function display(){
    $(document).ready(function () {             // Here I use the function from the roundSlider library
        for (data of datalist)  {
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
            });
        }
        for (data of numericData) document.querySelector(`#${data.id}`).textContent = data.value;
        
        for (data of datalist.concat(numericData)) {
            const errorElement = document.querySelector(`#${data.id}-error`);
            errorElement.textContent = data.error;
            if (data.error != noError) errorElement.style.visibility = 'visible';
            else errorElement.style.visibility = 'hidden';
        }
    });
}
