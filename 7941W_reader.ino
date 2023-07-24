void CommandList()
{
    Serial.println("0) This Command List");
    Serial.println("1) Command 0x10: Read UID from 13.56MHz RFID");
    Serial.println("2) Command 0x11: Write UID to 13.56MHz RFID");
    Serial.println("3) Command 0x12: Read Specified Sector from 13.56MHz RFID");
    Serial.println("4) Command 0x13: Write Specified Sector to 13.56MHz RFID");
    Serial.println("5) Command 0x14: Modify Group Password on 13.56MHz RFID");
    Serial.println("6) Command 0x15: Read ID number from 125KHz RFID");
    Serial.println("7) Command 0x16: Write ID number to 125KHz RFID");
    Serial.println("8) Command 0x17: Read Sector Data from 13.56MHz RFID");
}

void sendCommand0x10()
{
    //                                addrs, cmd, len,  XOR
    byte command[] = {0xAB, 0xBA, 0x00, 0x10, 0x00, 0x10};

    int commandSize = sizeof(command);

    // Send the command to the module
    Serial.write(command, commandSize);

    // Wait for the response from the module
    delay(100); // Add a short delay to allow the module to respond

    // Check if there's data available to read
    while (Serial.available() > 0)
    {
        // Read the incoming data byte-by-byte
        byte incomingByte = Serial.read();
        // Process the data here (e.g., check for success/failure, parse UID data)
        // ...

        // Print the received byte to the Serial monitor (for testing purposes)
        Serial.print("Received: 0x");
        Serial.print(incomingByte, HEX);
        Serial.print(" ");
    }
}

void sendCommand0x11()
{
    //                                addrs, cmd, len,  The actuall UID         XOR
    byte command[] = {0xAB, 0xBA, 0x00, 0x11, 0x04, 0xAA, 0xAA, 0xAA, 0xAA, 0xDa};

    int commandSize = sizeof(command);

    // Send the command to the module
    Serial.write(command, commandSize);

    // Wait for the response from the module
    delay(100); // Add a short delay to allow the module to respond

    // Check if there's data available to read
    while (Serial.available() > 0)
    {
        // Read the incoming data byte-by-byte
        byte incomingByte = Serial.read();
        // Process the data here (e.g., check for success/failure, parse UID data)
        // ...

        // Print the received byte to the Serial monitor (for testing purposes)
        Serial.print("Received: 0x");
        Serial.print(incomingByte, HEX);
        Serial.print(" ");
    }
}

void sendCommand0x12()
{

    //                                addrs, cmd, len,  sector, block, A or B group, next 6 bytes are the password, ussualy FF, XOR
    byte command[] = {0xAB, 0xBA, 0x00, 0x12, 0x09, 0x00, 0x01, 0X0A, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0x10};

    int commandSize = sizeof(command);

    // Send the command to the module
    Serial.write(command, commandSize);

    // Wait for the response from the module
    delay(100); // Add a short delay to allow the module to respond

    // Check if there's data available to read
    while (Serial.available() > 0)
    {
        // Read the incoming data byte-by-byte
        byte incomingByte = Serial.read();
        // Process the data here (e.g., check for success/failure, parse UID data)
        // ...

        // Print the received byte to the Serial monitor (for testing purposes)
        Serial.print("Received: 0x");
        Serial.print(incomingByte, HEX);
        Serial.print(" ");
    }
}

void sendCommand0x13()
{

    //                                addrs, cmd, len,  sector, block, A or B group, next 6 bytes are the password, ussualy FF, sector IG :D,                                                                                        XOR
    byte command[] = {0xAB, 0xBA, 0x00, 0x13, 0x19, 0x00, 0x01, 0x0A, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x10};

    int commandSize = sizeof(command);

    // Send the command to the module
    Serial.write(command, commandSize);

    // Wait for the response from the module
    delay(100); // Add a short delay to allow the module to respond

    // Check if there's data available to read
    while (Serial.available() > 0)
    {
        // Read the incoming data byte-by-byte
        byte incomingByte = Serial.read();
        // Process the data here (e.g., check for success/failure, parse UID data)
        // ...

        // Print the received byte to the Serial monitor (for testing purposes)
        Serial.print("Received: 0x");
        Serial.print(incomingByte, HEX);
        Serial.print(" ");
    }
}

void sendCommand0x14()
{

    //                                  addrs, cmd, len,  sector, A or B group, next 6 bytes are the OLD password         next 6 bytes are the NEW password
    byte command[] = {0xAB, 0xBA, 0x00, 0x14, 0x0E, 0x00, 0x0A, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x17};

    int commandSize = sizeof(command);

    // Send the command to the module
    Serial.write(command, commandSize);

    // Wait for the response from the module
    delay(100); // Add a short delay to allow the module to respond

    // Check if there's data available to read
    while (Serial.available() > 0)
    {
        // Read the incoming data byte-by-byte
        byte incomingByte = Serial.read();
        // Process the data here (e.g., check for success/failure, parse UID data)
        // ...

        // Print the received byte to the Serial monitor (for testing purposes)
        Serial.print("Received: 0x");
        Serial.print(incomingByte, HEX);
        Serial.print(" ");
    }
}

void sendCommand0x15()
{

    //                                  addrs, cmd, len,  XOR
    byte command[] = {0xAB, 0xBA, 0x00, 0x15, 0x00, 0x15};
    int commandSize = sizeof(command);

    // Send the command to the module
    Serial.write(command, commandSize);

    // Wait for the response from the module
    delay(100); // Add a short delay to allow the module to respond

    // Check if there's data available to read
    while (Serial.available() > 0)
    {
        // Read the incoming data byte-by-byte
        byte incomingByte = Serial.read();
        // Process the data here (e.g., check for success/failure, parse UID data)
        // ...

        // Print the received byte to the Serial monitor (for testing purposes)
        Serial.print("Received: 0x");
        Serial.print(incomingByte, HEX);
        Serial.print(" ");
    }
}

void sendCommand0x16()
{

    //                                  addrs, cmd, len,  XOR
    byte command[] = {0xAB, 0xBA, 0x00, 0x15, 0x00, 0x15};
    int commandSize = sizeof(command);

    // Send the command to the module
    Serial.write(command, commandSize);

    // Wait for the response from the module
    delay(100); // Add a short delay to allow the module to respond

    // Check if there's data available to read
    while (Serial.available() > 0)
    {
        // Read the incoming data byte-by-byte
        byte incomingByte = Serial.read();
        // Process the data here (e.g., check for success/failure, parse UID data)
        // ...

        // Print the received byte to the Serial monitor (for testing purposes)
        Serial.print("Received: 0x");
        Serial.print(incomingByte, HEX);
        Serial.print(" ");
    }
}

void sendCommand0x17()
{

    //                             addrs, cmd, len,  A or B group, next 6 bytes are the password, ussualy FF, XOR
    byte command[] = {0xAB, 0xBA, 0x00, 0x17, 0x07, 0x0A, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0x1A};

    int commandSize = sizeof(command);

    // Send the command to the module
    Serial.write(command, commandSize);

    // Wait for the response from the module
    delay(100); // Add a short delay to allow the module to respond

    // Check if there's data available to read
    while (Serial.available() > 0)
    {
        // Read the incoming data byte-by-byte
        byte incomingByte = Serial.read();
        // Process the data here (e.g., check for success/failure, parse UID data)
        // ...

        // Print the received byte to the Serial monitor (for testing purposes)
        Serial.print("Received: 0x");
        Serial.print(incomingByte, HEX);
        Serial.print(" ");
    }
}

void setup()
{
    Serial.begin(115200); // Set the baud rate to match the module's communication speed
}

void loop() {
  Serial.println("");
  Serial.println("Enter 0 for Command List");

  while(!Serial.available());
  char newchar = Serial.read();
  switch (newchar){
    case '0':
      CommandList();
      break;
    case '1':
      sendCommand0x10();
      break;
    case '2':
      sendCommand0x11();
      break;
    case '3':
      sendCommand0x12();
      break;
    case '4':
      sendCommand0x13();
      break;
    case '5':
      sendCommand0x14();
      break;
    case '6':
      sendCommand0x15();
      break;
    case '7':
      sendCommand0x16();
      break;
    case '8':
      sendCommand0x17();
      break;
  }
}
