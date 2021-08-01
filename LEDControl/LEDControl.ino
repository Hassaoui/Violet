#include <FastLED.h>
#include "ESP_MICRO.h"
using namespace std;
#include <sstream>

//led_pin 0 = d0
#define LED_PIN 0
#define numLEDS 300

  CRGB leds[numLEDS];
  //wifi Peloquin
  //start("domo","smart1707"); // Wifi details connec to
  //wifi Suzanne

  
void setup(){
  Serial.begin(9600);
  
  start("N.St.Amour","Nancy2020"); 
  
  FastLED.addLeds<WS2812, LED_PIN, GRB>(leds, numLEDS);
  
}
void loop(){
    /*
    for(int i = 0; i < numLEDS; i++){
    leds[i] = CRGB(120, 65 , 77);
    FastLED.show();
    }
    
    for(int i = 0; i < numLEDS; i++){
    leds[i] = CRGB(255, 13 , 64);
    delay(50);
    FastLED.show();
    }
  }*/
  waitUntilNewReq();  //Waits until a new request from python come
    //first entry lighton/off, whichStrip, effect, startRGB, endRGB
    //making the command
  String command[10];
  String fullPath = getPath();
  String word = "";
    for (auto x : fullPath) 
    {
        if (x == ',')
        {
          for(int i=0; i < 10; i++)
              if(command[i] == 0) {
                command[i] = word;
                break;
              }
            word = "";
        }
        else {
            word = word + x;
        }
    }
     for(int i=0; i < 10; i++)
              if(command[i] == 0) {
                command[i] = word;
                break;
              }
  //command is now made
  
  if (command[0]=="/OPEN_LED"){
    if(command[2] == "SolidColor"){
      solidColor(command[3].toInt(), command[4].toInt(), command[5].toInt());
    } else if(command[2] == "Rainbow"){
      rainBow(command[3].toInt(), command[4].toInt(), command[5].toInt());
    }
}

  if (getPath()=="/CLOSE_LED"){
    for(int dot = 0; dot < numLEDS; dot++) { 
      leds[dot] = CRGB::Black;
    }
    FastLED.show();
  }

  returnThisStr(getPath());
  }

  void solidColor(int r, int g, int b){
     for(int i = 0; i < numLEDS; i++){
    leds[i] = CRGB(r, g , b);
  }
    FastLED.show();
  }

  
  void rainBow(int r, int g, int b){
  while(true){
    for(int i = 0; i < numLEDS; i++){
    leds[i] = CRGB(r, g , b);
    delay(50);
    FastLED.show();
    }
    
    for(int i = 0; i < numLEDS; i++){
    leds[i] = CRGB(b, g , r);
    delay(50);
    FastLED.show();
    }
  }
  }
