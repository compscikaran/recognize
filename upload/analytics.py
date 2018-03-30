from .models import Scan
import matplotlib.pyplot as plt

def malevsfemale():
    countMale = 0
    countFemale = 0
    for scan in Scan.objects.all():
        if "FEMALE" in scan.text:
            countFemale += 1
    
    countMale = Scan.objects.count() - countFemale
    labels = ['Male','Female']
    values = [countMale,countFemale]
    colors = ['r', 'g']
    trace = plt.pie(values, labels = labels, colors = colors)
    plt.show()

        
    