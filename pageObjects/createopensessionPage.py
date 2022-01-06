import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


class CreateSessionPage:
    # Session Locators
    btn_createSessionHome = "(//div[contains(@class,'px-4 py-2 mx-auto text-center text-white rounded-md cursor-pointer lg:mx-0 text-md lg:min-w-32 lg:w-auto')][normalize-space()='Create Open Session'])[1]"

    btn_createSessionTutoring = "(//span[@class='hidden pl-2 font-bold md:block'])[1]"

    drp_subjectName = "(//select[@name='subjectId'])[1]"

    txt_sessionTitle = "(//input[@placeholder='Session Name'])[1]"
    rdb_liveTutoring = "(//input[@id='liveTutoring'])[1]"
    rdb_inPersonTutoring = "(//input[@id='inPersonTutoring'])[1]"

    # Enter Address details for inpersontutoring
    btn_address = "(//div[@class='flex flex-col items-center justify-center m-2 border rounded-lg cursor-pointer w-60 h-44'])[1]"
    btn_change = "(//span[@class='text-red-400 cursor-pointer hover:text-red-500'])[1]"
    txt_searchArea = "(//input[@placeholder='Search for area, street name...'])[1]"
    sel_selectAddress = "(//div[normalize-space()='Yellappa Chetty Layout, Sivanchetti Gardens, Halasuru, Karnataka, India'])[1]"
    confirmLocation = "check bala"
    txt_addressTitle = "(//input[@id='addressTitle'])[1]"
    txt_houseFlat = "(//input[@id='flatNo'])[1]"
    txt_landmark = "(//input[@id='landmarkArea'])[1]"
    btn_save = "(//button[normalize-space()='save'])[1]"

    drp_sessionTimeZone = "(//select[@class='w-full px-2 py-2 mt-2 mr-2 bg-gray-200 rounded-md lg:w-108 focus:outline-none'])[1]"
    sel_sessiondate = "(//input[@id='new_date_component'])[1]"
    drp_month = "(//select[@aria-label='Month'])[1]"
    drp_year = "(//input[@aria-label='Year'])[1]"
    sel_selectDate = "(//div[@class='dayContainer'])[1]"
    drp_sessionduration = "(//select[@id='dropdown'])[1]"
    sel_sessionRecurrence = "(//option[normalize-space()='Does not repeat'])[1]"

    # select_customRecurrence
    sel_repeatEvery = "(//input[@value='1'])[1]"
    sel_repeatEveryWeek = "(//option[normalize-space()='week(s)'])[1]"
    sel_repeatEveryday = "(//option[normalize-space()='day(s)'])[1]"

    sel_sessionRecurrence1 = "(//option[@value='custom'])[1]"

    sel_repeatonSunday = "(//div[@class='text-sm'][normalize-space()='S'])[1]"
    sel_repeatonMonday = "(//div[@class='text-sm'][normalize-space()='M'])[1]"
    sel_repeatonTuesday = "(//div[@class='text-sm'][normalize-space()='T'])[1]"
    sel_repeatonWednesday = "(//div[contains(text(),'W')])[1]"
    sel_repeatonThursday = "(//div[@class='text-sm'][normalize-space()='T'])[2]"
    sel_repeatonFriday = "(//div[contains(text(),'F')])[1]"
    sel_repeatonSaturaday = "(//div[@class='text-sm'][normalize-space()='S'])[2]"

    rdb_endOn = "(//input[@name='recur_mode'])[1]"
    sel_repeatMonth = "(//select[@aria-label='Month'])[3]"
    sel_repeatyear = "(//div[@class='numInputWrapper'])[9]"
    rdb_endafter = "(//input[@name='recur_mode'])[2]"
    sel_repeatEvery1 = "(//input[@value='2'])[1]"
    sel_Ok = "(//div[@class='text-base font-medium cursor-pointer text-logo_blue'])[1]"

    txt_addStudent = "(//input[@name='newStudent'])[1]"
    btn_addStudent = "(//button[@class='w-20 py-2 font-bold text-session_btn focus:outline-none'])[1]"

    def __init__(self, driver):
        self.driver = driver

    def clkcreateSessionHome(self):
        self.driver.find_element(By.XPATH, "btn_createSessionHome").click()

    def clkcreateSessionTutoring(self):
        self.driver.find_element(By.XPATH, "btn_createSessionTutoring").click()

    def drpsubjectName(self):
        self.driver.find_element(By.XPATH, "drp_subjectName").click()

    def txtsessionTitle(self):
        self.driver.find_element(By.XPATH, "txt_sessionTitle").click()

    def rdbliveTutoring(self):
        self.driver.find_element(By.XPATH, "rdb_liveTutoring").click()

    def rdbinPersonTutoring(self):
        self.driver.find_element(By.XPATH, "rdb_inPersonTutoring").click()

    # Address details for Tutoring

    def btnaddress(self):
        self.driver.find_element(By.XPATH, "btn_address").click()

    def btnchange(self):
        self.driver.find_element(By.XPATH, "btn_change").click()

    def txtsearchArea(self):
        return self.driver.find_element(By.XPATH, "txt_searchArea").click()

    def entertxtsearchArea(self, searchArea):
        self.txtsearcharea.send_keys(searchArea)

    def selselectAddress(self):
        self.driver.find_element(By.XPATH, "sel_selectAddress").click()

    def confirmlocation(self):
        self.driver.find_element(By.XPATH, "confirmLocation").click()

    def txtaddressTitle(self):
        self.driver.find_element(By.XPATH, "txt_addressTitle").click()

    def enteraddressTitle(self, addressTitle):
        self.txtaddressTitle.send_keys(addressTitle)

    def txthouseFlat(self):
        self.driver.find_element(By.XPATH, "txt_houseFlat").click()

    def enterhouseFlat(self, houseFlat):
        self.txthouseFlat.send_keys(houseFlat)

    def txtlandmark(self):
        self.driver.find_element(By.XPATH, "txt_landmark").click()

    def enterlandmark(self, landmark):
        self.txtlandmark.send_keys(landmark)

    def btnsave(self):
        self.driver.find_element(By.XPATH, "btn_save").click()

    def drpsessionTimeZone(self):
        self.driver.find_element(By.XPATH, "drp_sessionTimeZone").click()

    def selsessiondate(self):
        self.driver.find_element(By.XPATH, "sel_sessiondate").click()

    def drpmonth(self):
        self.driver.find_element(By.XPATH, "drp_month").click()

    def entermonth(self, month):
        self.drpmonth.send_keys(month)

    def drpyear(self):
        self.driver.find_element(By.XPATH, "drp_sessionTimeZone").click()

    def enteryear(self, year):
        self.drpyear.send_keys(year)

    def selselectDate(self, selectDate):
        self.driver.find_element(By.XPATH, "drp_sessionTimeZone").send_keys(selectDate)

    def drpsessionduration(self):
        self.driver.find_element(By.XPATH, "drp_sessionduration").click()

    def entersessionduration(self, sessionduration):
        self.drpsessionduration.send_keys(sessionduration)

    def selsessionRecurrence(self):
        self.driver.find_element(By.XPATH, "sel_sessionRecurrence").click()

    def selrepeatEvery(self):
        self.driver.find_element(By.XPATH, "sel_repeatEvery").click()

    def enterrepeatEvery(self,repeatEvery):
        self.selrepeatEvery.send_keys(repeatEvery)

    def selrepeatEveryWeek(self):
        self.driver.find_element(By.XPATH, "sel_repeatEveryWeek").click()

    def enterrepeatEveryWeek(self,repeatEveryWeek):
        self.selrepeatEveryWeek.send_keys(repeatEveryWeek)

    def selrepeatEveryday(self):
        self.driver.find_element(By.XPATH, "sel_repeatEveryday").click()

    def enterrepeatEveryday(self,repeatEveryday):
        self.selrepeatEveryday.send_keys(repeatEveryday)

    def selsessionRecurrence1(self):
        self.driver.find_element(By.XPATH, "sel_sessionRecurrence1").click()

    def selrepeatonSunday(self):
        self.driver.find_element(By.XPATH, "sel_repeatonSunday").click()

    def enterrepeatonSunday(self,Sunday):
        self.selrepeatonSunday.send_keys(Sunday)

    def selrepeatonMonday(self):
        self.driver.find_element(By.XPATH, "sel_repeatonMonday").click()

    def enterrepeatonMonday(self,Monday):
        self.selrepeatonMonday.send_keys(Monday)

    def selrepeatonTuesday(self):
        self.driver.find_element(By.XPATH, "sel_repeatonTuesday").click()

    def enterrepeatonTuesday(self,Tuesday):
        self.selrepeatonTuesday.send_keys(Tuesday)

    def selrepeatonWednesday(self):
        self.driver.find_element(By.XPATH, "sel_repeatonWednesday").click()

    def enterrepeatonWednesday(self, Wednesday):
        self.selrepeatonWednesday.send_keys(Wednesday)

    def selrepeatonThursday(self):
        self.driver.find_element(By.XPATH, "sel_repeatonThursday").click()

    def enterrepeatonThursday(self, Thursday):
        self.selrepeatonThursday.send_keys(Thursday)

    def selrepeatonFriday(self):
        self.driver.find_element(By.XPATH, "sel_repeatonFriday").click()

    def enterrepeatonFriday(self, Friday):
        self.selrepeatonFriday.send_keys(Friday)

    def selrepeatonSaturaday(self):
        self.driver.find_element(By.XPATH, "sel_repeatonSaturaday").click()

    def enterrepeatonSaturaday(self, Saturaday):
        self.selrepeatonSaturaday.send_keys(Saturaday)

    def rdbendOn(self):
        self.driver.find_element(By.XPATH, "rdb_endOn").click()

    def selrepeatMonth(self):
        self.driver.find_element(By.XPATH, "sel_repeatMonth").click()

    def enterrepeatMonth(self, month):
        self.selrepeatMonth.send_keys(month)

    def selrepeatyear(self):
        self.driver.find_element(By.XPATH, "sel_repeatyear").click()

    def enterrepeatyear(self, year):
        self.selrepeatyear.send_keys(year)

    def rdbendafter(self):
        self.driver.find_element(By.XPATH, "rdb_endafter").click()

    def selrepeatEvery1(self):
        self.driver.find_element(By.XPATH, "sel_repeatEvery1").click()

    def enterrepeatEvery1(self, occurrences):
        self.selrepeatEvery1.send_keys(occurrences)

    def selOk(self):
        self.driver.find_element(By.XPATH, "sel_Ok").click()

    def txtaddStudent(self):
        self.driver.find_element(By.XPATH, "txt_addStudent").click()

    def btnaddStudent(self):
        self.driver.find_element(By.XPATH, "btn_addStudent").click()



