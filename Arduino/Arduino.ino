#include <Adafruit_NeoPixel.h>

const uint8_t PIN  = 6;
const uint8_t NUMPIXELS = 162;

Adafruit_NeoPixel strip = Adafruit_NeoPixel(NUMPIXELS, PIN, NEO_RGB + NEO_KHZ800);

void setup() {
  Serial.begin(9600);
  strip.begin();
  strip.show();
}

void loop() {
  while (Serial.available() > 0) {
    int cmd = Serial.parseInt();
    int n = Serial.parseInt();
    int red = Serial.parseInt();
    int green = Serial.parseInt();
    int blue = Serial.parseInt();

    if (Serial.read() == '\n') {
      switch (cmd) {
        case 0:
          strip.setPixelColor(n, red, green, blue);
          break;
        case 1:
          strip.setPixelColor(n, red, green, blue);
          strip.show();
          break;
        case 2:
          // strip.begin();
          for (int n = 0; n < NUMPIXELS; n++)
          {
            strip.setPixelColor(n, 0, 0, 0);
          }
          strip.show();
          break;
        case 3:
          strip.show();
          break;
      }
    }
  }
}








