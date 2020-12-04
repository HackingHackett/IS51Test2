def main():
    f = open("Final.txt", "r")
    f = f.read()
    f = f.split('\n')
    intNums = []
    for i in f:
        intNums.append(int(i))
    count  = len(intNums)
    finalSum = 0
    for i in intNums:
        finalSum += i
    avg = finalSum / count
    print("Number of Grades: ", count)
    print('Average Grade : ', avg)
    calculate_percent_above_average(avg,intNums)
    

def calculate_percent_above_average(x,lst):
    tmp = 0
    for i in lst:
        if i > x:
            tmp+=1
    print('Percentage above average is : ' , round((tmp/len(lst))*100,2), '%')

    
    

main()
