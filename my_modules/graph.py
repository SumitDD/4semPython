import matplotlib.pyplot as plt
plt.figure()
student_attendance = {'day1':33, 'day2':34,'day3':29,'day4':31,'day5':28,'day6':26,'day7':30}

x_values = list(student_attendance.keys())
y_values = list(student_attendance.values())

plt.bar(x_values, y_values,width=0.5, align='center')
plt.xticks(rotation=45, horizontalalignment='right',fontweight='light')
plt.scatter(x_values, y_values, s=100)