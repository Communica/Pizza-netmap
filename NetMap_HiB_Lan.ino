/*
	Pizza-netmap

	A pizza box converted to a netmap. Using an arduino for serial communica	to a controller pc; who updates the state of the network according to i		its real world state. A switch down / uplink down --> red light. 


	@Authors:	technocake, Joaquin, Isamun
	@Date:		17.11.2012
*/
 



int  led_B1 = 2;
int  led_C1 = 3;
int  led_D1 = 4;
int  led_D2 = 5;
int  led_Crew = 6;
int led_Distro = 7;

int led_min = 2;
int led_max = 7;

char led, * ledp;
int led_int;

// the setup routine runs once when you press reset:
void setup() {                
Serial.begin(9600);


  // initialize the digital pin as an output.

pinMode(led_B1, OUTPUT);
pinMode(led_C1, OUTPUT);
pinMode(led_D1, OUTPUT);
pinMode(led_D2, OUTPUT);
pinMode(led_Crew, OUTPUT);
pinMode(led_Distro, OUTPUT);

}

boolean range_check(int led) {
   return (led >= led_min && led <= led_max); 
}

void toggle_led(int led) {
   if ( range_check(led) ) {
      //  Turns on a led.
      int status;
      
      status = digitalRead(led);
      digitalWrite(led, !status);
   }
}




// the loop routine runs over and over again forever: 
void loop() {
  
  if (Serial.available() > 0) {
    led = Serial.read();
    *ledp = led; 
    led_int = atoi(ledp);
    
    
      // We have a valid led command
      toggle_led(led_int); //Converts from ascii 1 (55,56 etc) to integer 1, 2 etc,
      Serial.flush();
      Serial.println("Led: ");
      Serial.write(led);
      
  }  
}


