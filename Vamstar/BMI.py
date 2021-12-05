import json
import io
import os

current = os.curdir

js_file = open('data.json', 'r')
json_obj = json.load(js_file)
js_file.close()

BMI_cat = ['Underweight', 'Normal weight Overweight', 'Moderately obese', 'Severel obese', 'Very severely obese']
hlth_risk = ['Malnutrition risk', 'Low risk', 'Enhanced risk', 'Medium risk', 'High', 'Very high risk']
BMI_range = [0, 18.5, 25, 30, 35, 40]
n = len(json_obj)
for i in range(n):
    bmi = json_obj[i]['WeightKg'] / ((json_obj[i]['HeightCm']/100)**2)
    j = 5
    while (j>0):
        if(bmi - BMI_range[j] >=0):
            break
        j = j - 1

    newGroup = { "BMI" : bmi,
                 "BmiCategory" : BMI_cat[j],
                 "HealthRisk" : hlth_risk[j]
    }

    json_obj[i].update(newGroup)

with io.open(os.path.join(current, 'new_data.json'), 'w') as js_new_file:
            json.dump(json_obj, js_new_file)