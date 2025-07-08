# DW_homework4
ดวงตะวัน สิ่งส่า 65114540215

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



 




