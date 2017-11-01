/*
 * project_arduino.c
 * 19200 baudrate 
 *
 */ 

#include <avr/io.h>
#include "sensorIO.h"
#include "serialConnection.h"
#include "AVR_TTC_scheduler.h"
#include "pinIO.h"

int max_rollout;
int min_rollout;


void Light(){
	transmitSerial(getLight()); 
}

void Temperature(){
	transmitSerial(getTemp());
}

void Distance(){
	transmitSerial(getDistance());
}



int main(void)
{
	
	analog_config();
	setUpUltra();
	initSerial();
	
	SCH_Init_T1(); // stel de scheduler in

	//SCH_Add_Task(Light, 0, 100); // Voeg taken toe aan de scheduler Light zit op A1.
	SCH_Add_Task(Temperature, 0, 100); // temp zit op A0.
	//SCH_Add_Task(Distance, 0, 100); 


	SCH_Start();// start de scheduler
   
    while (1) 
    {
		SCH_Dispatch_Tasks(); // verzend de taken
	}
} 





