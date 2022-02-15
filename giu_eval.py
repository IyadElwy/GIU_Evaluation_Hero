from selenium import webdriver
from selenium.webdriver.support.ui import Select

# Install and Import dol ya ged3an


user_name = input("Enter username: ")
password = input("Enter password: ")

browser = webdriver.Chrome("Path to chrome driver ex")
//OR
browser = webdriver.Edge("Path to edge driver ex")



browser.get(
    f"https://" + user_name + ":" + password + "@" + "portal.giu-uni.de/GIUb/EXTStudent/EvaluateStaff_m.aspx")

try:
    transcript_btn = browser.find_element_by_id("ContentPlaceHolder1_lnk_transcript")
    transcript_btn.click()

    evaluate_btn = browser.find_element_by_link_text("click here")
    evaluate_btn.click()

    # Change depending on how many staff members
    for i in range(1, 15):
        staff_option_list = Select(browser.find_element_by_id("ContentPlaceHolder1_stfIdLst"))
        staff_option_list.select_by_index(i)
        for j in range(0, 14):
            select_box_id_strongly_agree = f"ContentPlaceHolder1_objRptr_grade_{j}_0_{j}"
            current_radio_btn = browser.find_element_by_id(select_box_id_strongly_agree)
            current_radio_btn.click()
        browser.find_element_by_css_selector("#ContentPlaceHolder1_pstEvalBtn").click()

    id_btn = browser.find_element_by_id("lbl_Account")
    id_btn.click()
    id_lnk_home_btn = browser.find_element_by_id("lnk_home")
    id_lnk_home_btn.click()
    transcript_btn = browser.find_element_by_id("ContentPlaceHolder1_lnk_transcript")
    transcript_btn.click()
    evaluate_btn = browser.find_element_by_link_text("click here")
    evaluate_btn.click()

    for i in range(1, 6):
        course_option_list = Select(browser.find_element_by_id("ContentPlaceHolder1_crsIdLst"))
        course_option_list.select_by_index(i)
        for j in range(19):
            select_box_id_strongly_agree = f"ContentPlaceHolder1_objRptr_grade_{j}_0_{j}"
            current_radio_btn = browser.find_element_by_id(select_box_id_strongly_agree)
            current_radio_btn.click()
        for k in range(1, 4):
            browser.find_element_by_id(f"ContentPlaceHolder1_RadioButtonList{k}_0").click()
        browser.find_element_by_css_selector("#ContentPlaceHolder1_pstEvalBtn").click()


except:
    print("Not found")
