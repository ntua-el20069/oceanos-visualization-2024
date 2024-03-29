display();

let mode = '';
let modeText = '';
function changeSimulate(modeInput){
    mode = modeInput; 
     switch (mode){
        case 'Normal': modeText = "Normal"; break;
        case 'Simulation': modeText = "Simulation"; break;
        case 'Simulate csv': modeText = "CSV"; break;
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
        for (data of allData) {
        
            const randomFloat = generateRandomFloat(data.min, data.max, data.step);
            let error = noError;
            if (Math.random() < 0.3) error = 'Error!';  // error with probability 0.3 
            if(mode=='Simulation'){
                data.change(randomFloat, error);
                document.querySelector('#time').textContent = '';
                let motor_error = `We appreciate Indian`;
                if(Math.random() < 0.5) motor_error = '';
                document.querySelector('#motorError').textContent = motor_error;
            }
            else { // Simulate CSV
                data.change(localDataSet[start + counter][data.id], noError);
                document.querySelector('#time').textContent = localDataSet[start + counter]['current_time'];
                let motor_error = localDataSet[start + counter]['motor_error'];
                if(motor_error == '0')  motor_error = '';
                document.querySelector('#motorError').textContent = motor_error;
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
         
}, 500); // Interval set to 500 ms   CHANGE
    