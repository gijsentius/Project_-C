/*
 * Ultrasenoorsensor
 *
 * Onderstaande code zorgt ervoor dat de HC-SR04 sensor uitgelezen kan worden.
 *
 * De sensor zendt een geluid uit op 40 000 Hz. 
 * Dit reist door de lucht. Als er een object is stuit dit signaal weer terug naar de sensor. 
 * Door te kijken hoe lang de reis duurt en de snelheid van geluid kun je de afstand in centimeters berekenen.
 * Formule = afstand = tijd * 0.034 (snelheid geluid in ms) / 2
 * bron: http://howtomechatronics.com/tutorials/arduino/ultrasonic-sensor-hc-sr04/
 */ 

#include "pinIO.h"
#include <util/delay.h>

const int trigPin = 9; // const
const int echoPin = 10; // const


long duration;
int dis;


/* Ultrasenoorsensor 
*********************************************************************************************************************/

void setUpUltra(){
	digital_config(trigPin, OUT); // trigger pin wordt output
	digital_config(echoPin, IN); // echo pin is input
}

void startPulse(){
	digital_write(trigPin, LOW); // zorg ervoor dat trigger leeg is!
	_delay_ms(2);
	
	digital_write(trigPin, HIGH);
	_delay_us(10);
	digital_write(trigPin, LOW);
	
}

long readPulse(){
	duration = digital_read(echoPin); // pulse in maakt gebruik van timer, zelf een timer gebruiken om dit te regelen.
	return duration; // eeprom gebruiken for ID bijhouden Settings op je Arduino bijhouden
	// ardiuno moet zonder centrale door kunnen werken. Ardiuno 1 is voor zonnescherm 2. Ardiuno 2 is voor zonnescherm 2. 
	//Informatie weergeven in python, instellingen erin zetten, handmatig scherm omhoog of omlaag doen(vanuit centrale).
	// elke ardiuno is een klasse in centrale python.
}

int distance(int duration_){
	dis = (duration_ * 0.034) / 2;
	return dis;
}


/* dit is een soort van de main functie. Hierdoor krijg je de juiste afstand terug. Dit in scheduler gooien */
int getDistance(){
	int actDis;
	startPulse();
	actDis = readPulse();
	dis = distance(actDis);
	
	return dis;
	
}

/* Temperatuursensor
* verander het 10 bits getal in het voltage 
***************************************************************************************************************/


float voltage(uint16_t analog){
	float volt = analog * 5.0 / 1024;
	// keer 5.0 omdat het om 5 volt gaat en gedeelt door 1024 omdat het een 10 bits getal is
	// voorbeeld: 2.5 volt = 512 * 5.0 / 1024. Je krijgt 512(0x200) binnen
	return volt;
	
}


/* Deze functie zorgt ervoor dat de gemeten voltage omgezet wordt naar temperatuur */
float temperatureInC(float voltage_){
	float temperatureC = (voltage_ - 0.5) * 100;
	// de formule die ervoor zorgt dat het omgezet wordt.
	// voorbeeld: (1.2 - 0.5) * 100 = 70 graden Celsius.
	return temperatureC;
	
}


float measure_Temp(){
	float tempInC = temperatureInC(voltage(analog_read(0))); // lees ADC uit (A0) en maak er volt van en dan Celsius
	return tempInC;
}


uint8_t getTemp() {
	uint8_t temperature;
	temperature = measure_Temp(); // roep de functie aan die temperatuur uitleest
	return temperature;
}


/* Photocell sensor 
*********************************************************************************************************************/


uint8_t getLight(){
	uint8_t light = (analog_read(0)>>2); // lees A1 uit, met een shift /4 
	//
	
	return light;
}


