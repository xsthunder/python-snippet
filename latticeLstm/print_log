base_inputdir='../dataset_'
line_n=$1

if test -z $line_n 
then
	echo require line number
	exit 1
fi

while true
do
clear

for i in {1..6}
do
inputdir=$base_inputdir$i

# TODO what if more than one dir

log_file=$(ls $inputdir/$(ls $inputdir)/test.log)
echo "------------------------------------------------------------------------------------->            $inputdir              <----"
cat $log_file | tail -n $line_n

done


sleep 3
done
