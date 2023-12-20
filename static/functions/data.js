const noError = 'No error';
const regular_color = "#54BBE0";
const above_limit_color = "#EEAA00";
let color = regular_color;

class Data {
    constructor(id, definition,  max = 100, min = 0, step = 0.1, value = (min + max) / 2, error = noError, limit = 0.25*min + 0.75*max) {
        this.id = id;
        this.definition = definition;
        this.max = max;
        this.min = min;
        this.step = step;
        this.value = value;
        this.error = error;
        this.limit = limit;
    }
    change(value, error){
        if (value != '' && value != ' ' && value != '\n') this.value = value;
        this.error = error;
    }
}

datalist = [                        // CAUTION!  The data.id should match the fieldname from fieldnames list
    new Data("charge", "State of Charge (%)", 100) , 
    new Data("battery_temperature", "Battery Temperature (°C)", 50) , 
    new Data("speed", "Speed (kn)", 20) , 
    new Data("motor_tempMosfet", "Mosfet Temperature (°C)", 90) , 
    new Data("motor_current", "Motor Current (A)", 250) , 
    new Data("motor_tempMotor", "Motor Temperature (°C)", 75) 
]

numericData = [                     // CAUTION!  The data.id should match the fieldname from fieldnames list
   new Data('autonomy', 'Autonomy'),
   new Data('miles', 'Miles (miles)'),
   new Data('miles_lap', 'Miles per Lap (miles)'),
   new Data('rpm', 'RPM (rpm)')
]
