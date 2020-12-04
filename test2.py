function main():
	f -> open(final.txt,read)
	f -> split('\n')
	intNums -> []
	for i -> f:
		intNums -> append(i)
	count -> len(intNums)
	finalSum -> 0
	for i -> f:
		finalSum -> +1
	avg -> finalSum/count
	print 'Number of Grades', count
	print 'Average Grade', avg
	calculate_percent_above_average(avg,intNums)

function calculate_percent_above_average(x,lst):
	tmp -> 0
	for i -> lst:
		if i greater than x :
			tmp -> +1
	print 'Percentage above average is,' , round up tmp/lenth of lst * 100