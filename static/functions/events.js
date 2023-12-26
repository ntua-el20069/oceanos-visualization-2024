display();

let mode = '';
let modeText = '';
function changeSimulate(modeInput){
    mode = modeInput; 
     switch (mode){
        case 'Normal': modeText = "Normal Mode"; break;
        case 'Simulation': modeText = "Simulation Mode"; break;
        case 'Simulate csv': modeText = "Simulate csv Mode"; break;
        case 'Static': modeText = 'Static Mode'
    }
    
    document.querySelector('#mode').textContent = modeText;
}

const fieldnames =["current_time", "latitude", "longitude", "speed", "miles", "miles_lap", "rtc", "millis", "rpm", "input_voltage", "motor_watt", "motor_tempMosfet", "motor_tempMotor", "motor_current", "battery_current","motor_dutyCycle", "motor_error", "rasp_temp", "battery_ampere", "battery_voltage", "charge", "battery_temperature", "autonomy"]

finalFetch(csvURL); // fetch Simulation Data

// if you want to chack data from rows  a (start)-> b (end)
// set     start = a,    and    samples = b-a 

let start = 2;      
let samples = 300;
let counter = 0;

setInterval(function() {
    if (mode=='Simulate csv' || mode=='Simulation') {
        counter += 1;
        counter %= samples;
        for (data of datalist.concat(numericData)) {
        
            const randomFloat = generateRandomFloat(data.min, data.max, data.step);
            let error = noError;
            if (Math.random() < 0.3) error = 'Error!';  // error with probability 0.3 
            if(mode=='Simulation'){
                data.change(randomFloat, error);
            }
            else {
                data.change(localDataSet[start + counter][data.id], noError);
            }

        }
        display();
    }
    else if (mode == 'Static') {  // Static mode (do nothing - do not change)
        ;
    }
    else  {  // Normal mode    // mode == '' or mode == 'Normal'
        reloadPage();
    }
         
}, 1000); // Interval set to 1000ms (1 second)
    