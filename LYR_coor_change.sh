sed -n '/1729\ \ N/, +28p' $1 |cut -b33-54 > $2.txt
python3 convert.py $3 $2.txt
