set -e
num=$1
if test -z $num 
then
 echo require a num 任务号
 exit 
fi
source activate lattice-lstm-pytorch-0.3
# 可以设置gpu号
# export CUDA_DEVICE_ORDER="PCI_BUS_ID" 
# export CUDA_VISIBLE_DEVICES="1"
outputdir=ccks-output/dataset_$num
mkdir $outputdir
outputdir=$outputdir/$(date +'%m%d-%H%M')
mkdir $outputdir
logfile=$outputdir/run.log
inputdir=../CCKS-Data-Use/ner_data/dataset_$num
echo "" > $logfile # rewriting a new log file
echo " inputdir : $inputdir " >> $logfile
echo " outputdir :$outputdir " >> $logfile
echo " logfile : $logfile " >> $logfile
echo "xshunder: starting at" >> $logfile
date >> $logfile
python main.py --status train \
  --train $inputdir/train.char \
  --dev $inputdir/dev.char \
  --test $inputdir/test.char \
  --savemodel $outputdir/model \
  --savedset $outputdir/model.dset \
  1>> $logfile\
  2>> $logfile
echo "xshunder: ended at" >> $logfile
date >> $logfile
