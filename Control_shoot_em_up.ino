const int SWITCH = 2;
const int x = 1;
const int y = 0;
const int a = 7;

void setup(){
  pinMode(SWITCH,INPUT);
  digitalWrite(SWITCH,HIGH);

  pinMode(a,INPUT);
  digitalWrite(a,HIGH);
  
  Serial.begin(9600);
 
}
void loop() {
  Serial.println("{\"x\" :" + (String)analogRead(x) + ", \"y\":" + (String)analogRead(y)+ ", \"a\":" + (String)digitalRead(a) +"}");

}
