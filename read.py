import time
import binascii

from pn532pi import Pn532, pn532
from pn532pi import Pn532I2c

I2C = True

if I2C:
    PN532_I2C = Pn532I2c(1)
    nfc = Pn532(PN532_I2C)


def read_setup():
    nfc.begin()

    versiondata = nfc.getFirmwareVersion()
   
    nfc.SAMConfig()




def read_loop():
    success, uid = nfc.readPassiveTargetID(pn532.PN532_MIFARE_ISO14443A_106KBPS)

    if (success):
    
        if (len(uid) == 4):
            
            print("Mifare Classic card (4 byte UID)")

            keya = bytearray([0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF])

            success = nfc.mifareclassic_AuthenticateBlock(uid, 4, 0, keya)

            if (success):
                
                success, data = nfc.mifareclassic_ReadDataBlock(4)

                if (success):
                    
                    result = "Mifare Classic card (4 byte UID)" + "|" + "Reading Block 4: " + binascii.hexlify(data).decode() + "|" + "ISO1444-3 (Type A)" + "|" + binascii.hexlify(uid).decode() 

                    result_list = result.split("|")
                    print(result_list)

                    return result_list


                else:
                    print("Ooops ... unable to read the requested block.  Try another key?")
                    return "Ooops ... unable to read the requested block.  Try another key?"
            else:
                print("Ooops ... authentication failed: Try another key?")
                return "Ooops ... authentication failed: Try another key?"

        elif (len(uid) == 7):
            print("Seems to be a Mifare Ultralight tag (7 byte UID)")

            print("Reading page 4")
            success, data = nfc.mifareultralight_ReadPage(4)
            if (success):
                binascii.hexlify(data)

                result = "Mifare Classic card (4 byte UID)" + "|" + "Reading Block 4: " + "|" + binascii.hexlify(data).decode() + "|" + "ISO1444-3 (Type A)" + "|" + binascii.hexlify(uid).decode() 

                result_list = result.split("|")
                print(result_list)

                return result_list

            else:
                print("Ooops ... unable to read the requested page!?")
                return "Ooops ... unable to read the requested page!?"

    return False
