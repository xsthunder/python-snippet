source activate seqeval
for file in $(find .. | grep -E "(dev|test).json" | sort)
do
	python seqeval_file.py $file
done
