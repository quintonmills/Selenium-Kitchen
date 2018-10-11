from selenium import webdriver
import csv, sys
#vairable for printing test summary
test_executed = 0
test_passed = 0
test_failed = 0
test_status = True

try:
    #create an instance of WebDriver for Firefox
    driver = webdriver.Firefox(executable_path='/Users/QuintonMills/Desktop')
    driver = webdriver.Firefox()
    driver.get("http://dl.dropbox.com/u/55228056/bmicalculator.html")
    #open csv file
    datafile = open('c:/data.csv', "rb")
    reader = csv.reader(datafile)
    test_executed = 0
    for row in reader:
        test_executed += 1
        print("test "+str(test_executed))
        highlightField = driver.find_element_by_name("heightCMS")
        highlightField.clear()
        highlightField.send_keys(row[0])
        weightField = driver.find_element_by_name("weightKg")
        weightField.clear()
        weightField.send_keys(row[1])
        calculateButton = driver.find_element_by_id("Calculate")
        calculateButton.click()
        bmiLabel = driver.find_element_by_name("bmi")
        bmiCategoryLabel = driver.find_element_by_id("bmi_category")
        if bmiCategoryLabel.get_attribute("value") == row[2]:
            print("Pass, expected value for BMI <" + row[2] + ", actual <" + bmiLabel.get_attribute("value") + ">")
        else:
            print("fail, expected value for BMI Category <" + row[3] + ", actual <" + bmiLabel.get_attribute("value") + ">")
            test_status=False
        if bmiCategoryLabel.get_attribute("value") == row[3]:
            print("pass, expected value for BMI Category <" + row[3] + ">, actual <" + bmiCategoryLabel.get_attribute("value") + ">")
        else:
            print("fail, expected value for BMI Catergory <" + row[3] + ">, actual <" + bmiCategoryLabel.get_attribute("value") + ">")
            test_status = False
        if test_status == True:
            test_passed = test_passed + 1
        else :
            test_failed = test_failed +1
        datafile.close()
    #except:
    #    print("Unexpected error:", sys.exc_info()[0])
    #    raise
finally:
        SystemExit()
