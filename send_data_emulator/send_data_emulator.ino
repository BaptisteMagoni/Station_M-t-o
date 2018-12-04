#include <SoftwareSerial.h>

bool receive;

void setup() {
  Serial.begin(9600);

}

void loop() {
  Serial.write("4c4f4f1401ff7f0375d40225c20105ff57013c00580010005101ff7fff7f2000ff3dff2c002900ff000000ffff7f0c0092240c000000000000000c00020000ffff037503750375ff06050e120a02151a030101ff7fff7fff7fff7fff7fff7f0a0d5ea0");
  delay(1000);
}
