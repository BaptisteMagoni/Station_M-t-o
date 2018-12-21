#include <SoftwareSerial.h>

bool receive;

void setup() {
  Serial.begin(19200);

}

void loop() {
  Serial.write("4c4f4f1401ff7f0275d40224b90104ff3b014a003c0010005101ff7fff7f2100ff41ff2b002800ff000000ffff7f0c0092240c000000000000000c00020000ffff027502750275ff00050e120a06151e030101ff7fff7fff7fff7fff7fff7f0a0d40c0");
  delay(1000);
}
