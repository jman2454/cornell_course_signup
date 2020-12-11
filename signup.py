import sys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

timeout = 30

user = sys.argv[1]
pwd = sys.argv[2]


def wait_get_element(driver, timeout, locator):
    return WebDriverWait(driver, timeout).until(EC.presence_of_element_located(locator))


driver = webdriver.Chrome()
done = False

while not done:
    try:
        driver.get("http://studentcenter.cornell.edu")

        if driver.title == "Cornell University Web Login":
            main = driver.find_element_by_xpath("html/body/main")
            netid_field = main.find_element_by_name("netid")
            pass_field = main.find_element_by_name("password")
            login_btn = main.find_element_by_name("Submit")
            netid_field.send_keys(user)
            pass_field.send_keys(pwd)
            login_btn.click()

            wrap = wait_get_element(driver, timeout, (By.ID, "wrap"))

            driver.switch_to.frame(0)

            signin_methods = driver.find_element_by_id("login-form").find_element_by_id(
                "auth_methods"
            )

            push_btn = signin_methods.find_element_by_xpath("fieldset/div/button")
            push_btn.click()

        load_page = wait_get_element(driver, 100, (By.NAME, "TargetContent"))

        driver.switch_to.frame(0)

        shopping_cart_btn = driver.find_element_by_id("ACE_width").find_element_by_id(
            "DERIVED_SSS_SCL_SSS_ENRL_CART$276$"
        )

        shopping_cart_btn.click()

        table = wait_get_element(driver, timeout, (By.ID, "SSR_DUMMY_RECV1$scroll$0"))

        radio_btns = table.find_element_by_xpath(
            "tbody/tr[2]/td/table/tbody"
        ).find_elements_by_tag_name("tr")

        latest_sem_btn = radio_btns[len(radio_btns) - 1].find_element_by_tag_name(
            "input"
        )
        latest_sem_btn.click()

        cont = driver.find_element_by_name("DERIVED_SSS_SCT_SSR_PB_GO")
        cont.click()

        table = wait_get_element(driver, timeout, (By.ID, "win0divSSR_REGFORM_VW$0"))
        classes = table.find_elements_by_xpath('//input[@type="checkbox"]')

        while len(classes) > 0:
            for inpt in classes:
                inpt.click()

            enrll = driver.find_element_by_xpath('//input[@title="Enroll in Course"]')
            enrll.click()

            finish_btn = wait_get_element(
                driver, timeout, (By.ID, "DERIVED_REGFRM1_SSR_PB_SUBMIT")
            )

            finish_btn.click()

            restart_btn = wait_get_element(
                driver, timeout, (By.ID, "DERIVED_REGFRM1_SSR_LINK_STARTOVER")
            )

            restart_btn.click()

            table = wait_get_element(
                driver, timeout, (By.ID, "win0divSSR_REGFORM_VW$0")
            )
            classes = table.find_elements_by_xpath('//input[@type="checkbox"]')

        done = True
        print("All courses in your shopping cart have been added!")

    except TimeoutException:
        pass
