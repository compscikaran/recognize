from .models import Scan
import numpy as np
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

def get_avg_age():
    avg = 0
    count = 0
    for scan in Scan.objects.all():
        end_idx = scan.text.find('Years')
        if end_idx == -1:
            continue
        try:    
            avg += int(scan.text[end_idx-3:end_idx])
        except:
            continue
        count += 1
    avg /= count
    return avg

def life_expectency_vs_city():
    rasipuram_avg = 0
    chennai_avg = 0
    count_rasi = 0
    count_chenn = 0
    for scan in Scan.objects.all():
        end_idx = scan.text.find('Years')
        if end_idx == -1:
            continue
        if "RASIPURAM" in scan.text:
            try:
                rasipuram_avg += int(scan.text[end_idx-3:end_idx])
            except:
                continue
            count_rasi += 1
        else:
            print(scan.text)
            print(scan.text[end_idx - 10: end_idx + 5])
            try:
                chennai_avg += int(scan.text[end_idx-3:end_idx])
            except:
                continue
            count_chenn += 1
    rasipuram_avg /= count_rasi
    chennai_avg /= count_chenn
    x = np.arange(2)
    avg_expectency = [rasipuram_avg, chennai_avg]
    fig, ax = plt.subplots()
    pr, pc = plt.bar(x, avg_expectency)
    pr.set_facecolor('g')
    pc.set_facecolor('b')
    plt.xticks(x, ('Rasipuram', 'Chennai'))
    plt.ylim([0, 100])
    ax.set_xlabel('Municipality')
    ax.set_ylabel('Avg. Life Expectency')
    plt.axhline(y = get_avg_age(), color = 'lawngreen', linestyle = '--')
    plt.show()

def life_expectency_vs_gender():
    male_avg = 0
    female_avg = 0
    count_male = 0
    count_female = 0
    for scan in Scan.objects.all():
        end_idx = scan.text.find('Years')
        if end_idx == -1:
            continue
        if "FEMALE" in scan.text:
            try:
                female_avg += int(scan.text[end_idx-3:end_idx])
            except:
                continue
            count_female += 1
        else:
            try:
                male_avg += int(scan.text[end_idx-3:end_idx])
            except:
                continue
            count_male += 1
    female_avg /= count_female
    male_avg /= count_male
    print(count_female,count_male)
    x = np.arange(2)
    avg_expectency = [male_avg, female_avg]
    fig, ax = plt.subplots()
    pm, pf = plt.bar(x, avg_expectency)
    pm.set_facecolor('b')
    pf.set_facecolor('r')
    plt.xticks(x, ('Male', 'Female'))
    plt.ylim([0, 100])
    ax.set_xlabel('Gender')
    ax.set_ylabel('Avg. Life Expectency')
    plt.axhline(y = get_avg_age(), color = 'lawngreen', linestyle = '--')
    plt.show()

    

        
