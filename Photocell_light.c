/*
 * Photocell
 *
 * Onderstaande code zorgt ervoor dat de LDR04 (light dependent resistor) sensor uitgelezen kan worden.
 *
 * Een photo-resistor of cel, is een weerstand die lichtgestuurd is. 
 * Als de lichtintensiteit toeneemt, neemt de weerstand van een photoresistor af.
 * bron : http://www.instructables.com/id/How-to-use-a-photoresistor-or-photocell-Arduino-Tu/
 *
 */ 

// # include temperature voor voltage functie

#include <util/delay.h>
#include "pinIO.h"

const int light;


int getLight(){
	light = analog_read(1); // lees A1 uit // deze functie nog uit Gijs zijn library halen
	return light;
}


/* bovenstaande code is alles wat je nodig hebt om de photoresistor uit te lezen.
* Vervolgens moeten we kijken of we in de centrale iets met de gelezen waarden te doen, of op de Arduino
*/