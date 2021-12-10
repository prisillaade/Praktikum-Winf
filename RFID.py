import rdm6300
import serial
import time
import sys

#read the rfid chips
#reader = rdm6300.Reader(rdm6300.BaseReader)
#print("Please insert an RFID card")
#while True:
 #   card = reader.read()
  #  if card:
   #     print(f"[{card.value}] read card {card}")

class Reader(rdm6300.BaseReader):
    def card_inserted(self, card):
        print(f"card inserted {card}")

    def card_removed(self, card):
        print(f"card removed {card}")

    def invalid_card(self, card):
        print(f"invalid card {card}")

r = Reader('/dev/ttyS0') #python -m serial.tools.list_ports
r.start()