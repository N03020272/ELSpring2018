MCU_out(LOW);
delayMs(2);
Pinmode(MCU_out, input);
while(MCU_out == HIGH);

sensor_ready = 1;

if(sensor_ready)
{
	//Wait at least 70us for bus to be low
	while(useconds < 70)
	{
		wait_us(1);
		useconds++;
		preamble_1 = 1;
	}
	
	useconds = 0;

	//wait until the bus goes high to sense next
	//cycle of preamble
	while(MCU_out == LOW);	

	//wait at least 70us for bus to be high
	while(useconds < 70)
	{
		wait_us(1);
		useconds++;
		preamble_2 = 1;
	}

	useconds = 0;
	
	//wait until the bus goes low to indicate
	//the start of the data transmission
	while(MCU_out == HIGH);	

	if(preamble_1 & preamble_2)
		preamble_finished = 1;

	if(preamble_finished)
	{
		for(int i = 0; i < 40; i++)
		{
		//bus is low for at least 40us
		while(useconds < 40)
		{
			wait_us(1);
			useconds++;
		}
	
		useconds = 0;

		//wait until the bus goes high to sense 		 	  next
		//cycle of preamble
		while(MCU_out == LOW);
		}
		
	}	
}	