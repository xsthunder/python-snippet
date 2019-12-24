# 输出decode test/dev 的结果 以及 ground-truth 结果，调用seqeval.sh
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

# TODO when with multipy dirs
outputdir=$outputdir/$(ls $outputdir)

# take neweset model, remove trailing '*' with akw, but no * in subshell
# https://unix.stackexchange.com/questions/305190/remove-last-character-from-string-captured-with-awk
loadmodel=$(ls -l $outputdir --sort=time | awk '{print $9}' | grep -E 'model\.[0-9]+\.model' | head -n 1)

logfile=$outputdir/test.log
inputdir=../CCKS-Data-Use/ner_data/dataset_$num
echo starting $num at $(date)
echo $(date) > $logfile
echo " inputdir : $inputdir " >> $logfile
echo " outputdir :$outputdir " >> $logfile
echo " loadmodel : $loadmodel " >> $logfile
echo " logfile : $logfile" >> $logfile
python main.py --status test \
  --dev $inputdir/dev.char \
  --test $inputdir/test.char \
  --loadmodel $outputdir/$loadmodel \
  --savedset $outputdir/model.dset \
  >> $logfile 2>> $logfile
echo ended $num at $(date)
