#include<RSCG12864B.h>
byte chnr[101]={0};
void setup() {
  // put your setup code here, to run once:
  RSCG12864B.begin();
  RSCG12864B.brightness(200);
  RSCG12864B.clear();
  Serial.begin(9600);
  
}

void loop() {
  
  // put your main code here, to run repeatedly:
  if(Serial.available()){
    RSCG12864B.clear();
    Serial.println("ok");
    int i=0;
    while(Serial.available() && i<=100){
      chnr[i]=Serial.read();
      delay(2);
      i++;
    }
    chnr[i]=0;
    RSCG12864B.cursor(0,0);
    RSCG12864B.print_string_12_xy(0,0,chnr);
  }
//  for(int i=0;i<10;i++){
//    Serial.print(chnr[i],HEX);
//  }
//  Serial.println();
  
}
