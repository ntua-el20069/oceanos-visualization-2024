const noError = 'No error';
const regular_color = "#54BBE0";
const above_limit_color = "#EEAA00";
let color = regular_color;
const maxOmittedValues = 15;

class Data {
    constructor(id, definition, slider = true, max = 100, min = 0, step = 0.1, value = (min + max) / 2, error = noError, limit = 0.25*min + 0.75*max) { // default initializations
        this.id = id;
        this.definition = definition;
        this.slider = slider;    // true if you want round slider for this data, false if it is just numeric
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
allData = [                       // CAUTION!  The data.id should match the fieldname from fieldnames list
    new Data('autonomy', 'Autonomy', slider = false, max = Infinity),
    new Data('miles', 'Miles', slider = false, max = Infinity),
    new Data('miles_lap', 'Miles per Lap', slider = false, max = Infinity),
    new Data('rpm', 'RPM (rpm)', slider = false, max = Infinity),
    //new Data('millis', 'Millis', slider = false, max = Infinity) ,   

    new Data("charge", "Charge (%)", slider = true, max = 100) , 
    new Data("battery_temperature", "Battery Temp (°C)", slider = true, max = 50) , 
    new Data("speed", "Speed (kn)", slider = true, max = 20) , 



    new Data("motor_tempMosfet", "Mosfet Temp (°C)", slider = true, max = 90) , 
    new Data("motor_current", "Motor Current (A)", slider = true, max = 250) , 
    new Data("motor_tempMotor", "Motor Temp (°C)", slider = true, max = 75) ,
    //new Data("input_voltage", "Input Voltage (V)", slider = true, max = 100)  ,              
   


]

// CHANGE : if you want, you can add a data and change the sequence, be careful to read the Data Class Declaration (for the constructor)