const noError = 'No error';
const regular_color = "#54BBE0";
const above_limit_color = "#EEAA00";
let color = regular_color;
const maxOmittedValues = 15;

class Data {
    constructor(id, definition,  max = 100, min = 0, step = 0.1, value = (min + max) / 2, error = noError, limit = 0.25*min + 0.75*max) { // default initializations
        this.id = id;
        this.definition = definition;
        this.max = max;
        this.min = min;
        this.step = step;
        this.value = value;
        this.error = error;
        this.limit = limit;
        this.omittedValues = 0;
    }
    change(value, error){
        if (String(value) != '' && String(value) != ' ' && String(value) != '\n') {  // value is not empty
            this.value = value;
            this.omittedValues = 0;
            if(value > this.max || value < this.min) this.error = String(value)
            else this.error = error;
        }
        else {  // empty value
            this.omittedValues += 1;
            if (this.omittedValues > maxOmittedValues) { this.value = ''; this.omittedValues = 0; this.error = 'Lost Value'} // if you have lost 15 data continuously, show Lost value
        }
        
    }
}

datalist = [                        // CAUTION!  The data.id should match the fieldname from fieldnames list
    new Data("charge", "State of Charge (%)", 100) , 
    new Data("battery_temperature", "Battery Temperature (°C)", 50) , 
    new Data("speed", "Speed (kn)", 20) , 
    new Data("motor_tempMosfet", "Mosfet Temperature (°C)", 90) , 
    new Data("motor_current", "Motor Current (A)", 250) , 
    new Data("motor_tempMotor", "Motor Temperature (°C)", 75) 
    //, new Data("input_voltage", "Input Voltage (V)")
]

numericData = [                     // CAUTION!  The data.id should match the fieldname from fieldnames list
   new Data('autonomy', 'Autonomy', Infinity),
   new Data('miles', 'Miles (miles)', Infinity),
   new Data('miles_lap', 'Miles per Lap (miles)', Infinity),
   new Data('rpm', 'RPM (rpm)', Infinity)
   //, new Data('millis', 'Millis', Infinity)
]

