# DW_homework4
ดวงตะวัน สิ่งส่า 65114540215

*a. เขียนวิธีการติดตั้งและเปิดใช้งาน clickhouse*

ของผมใช้ clickhouse ผ่าน docker รันคำสั่งเรียก image สร้าง containner มาใช้

docker run -d --name clickhouse-server \
  -p 8123:8123 -p 9000:9000 \
  yandex/clickhouse-server

ถ้าอยากใช้ clickhouse ก็รันคำสั่ง



 docker exec -it clickhouse-server clickhouse-client

 
 
*b. เขียนวิธีนำเข้าข้อมูลจากการบ้านที่ 4. (HW04)*

*1.ใช้งานผ่าน ubantu

git clone https://github.com/vadimtk/ssb-dbgen.git

cd ssb-dbgen

make


*2. gen ข้อมูล ทำได้แค่ date เพราะ gen ไฟล์อื่นไม่ได้ เพราะอันอื่นขนาดใหญ่เกินไป

./dbgen -s 1000 -T c

./dbgen -s 1000 -T l

./dbgen -s 1000 -T p

./dbgen -s 1000 -T s

./dbgen -s 1000 -T d


*3. เข้า clickhouse - client แล้ว สร้าง table 

CREATE TABLE customer lineorder part  supplier date




*4.แปลงข้อมูล .tbl เป็น .csv

sed 's/|$//' customer.tbl | sed 's/|/,/g' > customer.csv


*5.แต่จะติดปัญหา ต้องแก้ ข้อมูลมี "" insert ไม่ได้ต้องแก้ และเดือนเขียนผิด จาก Augest เป็น August  จาก Octorber เป็น October  


*6.แก้เสร็จ insert ข้อมูล

clickhouse-client --host=127.0.0.1 --query "INSERT INTO date FORMAT CSV" < date.csv


*7.แก้ view แก้  url  สร้าง template  runserver เสร็จสิ้น




*c. เขียนวิธีการติดตั้งและเปิดใช้งาน superset*

เข้าไปที่เว็บไซต์ superset documentation ในหัวข้อ quickstart 

clone https://github.com/apache/superset ใน tag 5.0.0

หลังจากนั้น cd superset แล้วรันคำสั่ง เอา superset conatainer

docker compose -f docker-compose-image-tag.yml up

หลังจากนั้น เข้าไปที่ http://localhost:8088 กรอกข้อมูลเสร็จสิ้น

username: admin
password: admin




*d. เขียนวิธีการเชื่อม superset กับ clickhouse*

เราเข้าไปใน superset เพื่อเชื่อมกับ clickhouse  เช็คชื่อ container แล้วเข้าไปใน container superset

docker ps

docker exec -it superset_app bash

หลังจากนั้นให้ pip install clickhouse-connect เพื่อเชื่อม clickhouse

จากนั้น exit แล้ว restart superset รันคำสั่ง

docker restart superset_app

จากนั้นเข้าไปใน superset dashboard แล้วกดปุ่ม + ขวาบน กด data แล้วก็กด create dataset  มันจะมีให้เลือก drop down ข้างล่าง เลือก click house

จากนั้นให้ใส่ข้อมูล client  ของเรา แล้วเชื่อม กับ database แล้วก็จะเสร็จสิ้น





*e. เขียนวิธีการนำเสนอข้อมูลจากข้อมูล b. บน dashboard ของ superset พร้อมผลลัพธ์*

กดเข้าไปที่ dataset ที่เราโหลดมาจาก clickhouse  สร้าง chart ที่ต้องการ ผลลัพธ์ก็จะออกมา เช่น bar area แล้วก็ save




*f. เขียนบทสรุปการใช้งาน*

เป็นการทำใช้ clickhouse มาเก็บข้อมูลผ่าน docker เราต้องเชื่อม clickhouse กับ docker เพื่ออย่างน้อยให้ table ใน clickhouse แล้วมีการใช้ superset  เพื่อนำข้อมูลจาก clickhouse มานำมาทำ dashborad ที่เราต้องการ ส่วนมากจะเป็นการเชื่อมข้อมูล  

สรุปคือ สร้าง clickhouse ผ่าน docker -> โหลดข้อมูลที่เราได้ -> นำไปสร้างใน ckickhouse -> แล้วนำไปเชื่อมกับ superset -> นำข้อมูลที่ได้ไปสร้าง dashboard






