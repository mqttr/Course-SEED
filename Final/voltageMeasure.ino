int analogPin = A0;
int digitalPin = 2;

void setup() {
  pinMode(digitalPin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  int analogValue = analogRead(analogPin);
  int digitalValue = map(analogValue, 0, 1023, 0, 255); // convert analog value to digital (0-255)

  digitalWrite(digitalPin, HIGH); // send a signal to the Raspberry Pi to indicate that data is being sent
  Serial.print(digitalValue);
  Serial.write('\n'); // send a newline character to indicate the end of the data
  digitalWrite(digitalPin, LOW); // signal that the data transmission is complete

  delay(1000); // wait for one second before reading the voltage again
}