from selenium.webdriver.common.by import By

class Locators():
    # --- Landing Page Locators ---
    LOGIN_BUTTON = (By.XPATH, '//*[@id="root"]/div/div/header/div/div[2]/button')

    # --- Login Page object Locators ---
    LOGINBUTTON = (By.NAME,'submit')
    EMAILFIELD = (By.ID, '1-email')
    PASSWORDFIELD = (By.NAME,'password')

    # --- Certification page Object Locators ---
    ADDANOTHERRR = (By.XPATH, '//h3[contains(.,"Certifications")]/parent::div/following-sibling::div/child::button/child::div')
    CERTOIFICATIONFIELDNEW = (By.NAME, 'CertificationFieldNew')
    CERTOIFICATIONFIELDEDIT = (By.NAME, 'name')
    CERTYEARFIELD = (By.XPATH, '//label[contains(.,"Year")]/parent::div/child::div/child::div/child::button')
    SELECTYEAR2 = (By.XPATH, '//span[contains(.,"2016")]')
    YEARFIELD = (By.XPATH, '//*[@id="root"]/div/div/main/div/div/div/div[7]/div[2]/div[2]/form/div[2]/div/div/button/div/div[1]/div/input')
    SAVEBUTTONCERTI = (By.CLASS_NAME,'StyledButton-sc-323bzc-0.bDapPz')
    SELECTYEAR = (By.CSS_SELECTOR, 'input.StyledTextInput-sc-1x30a0s-0.cQnphq.Select__SelectTextInput-sc-17idtfo-0.dIrhTb')
    EDITTBUTTON = (By.XPATH, '//h3[contains(.,"Certification")]/parent::div[1]/parent::div[1]/child::div[2]/child::div[1]/child::div/child::div[3]/child::button')
    ALERTFIELD = (By.CLASS_NAME,'StyledText-sc-1sadyjn-0.dCCtef')
    GETINPUTTEXTANDVERIFY1 = '((//h3[contains(.,"Certifications")]/parent::div/following-sibling::div/child::div)[last()]/child::div/child::div/child::div/child::div/child::h4)'
    GETINPUTTEXTANDVERIFY2 = '((//h3[contains(.,"Certifications")]/parent::div/following-sibling::div/child::div/child::div/child::div/child::div/child::div/child::h4))[1]'

    # --- Education Page Object Locators ---
    ADDANOTHERRRRRR = (By.XPATH, '(//div[@class="StyledBox__StyledBoxGap-sc-13pk1d4-1 geTJbw"])[2]')
    UNIVERSITYFIELD = (By.NAME, 'UniversityFieldNew')
    GRADUATIONYEARFIELD = (By.ID, 'new-degree-endDate-year__input')
    YEARR = (By.XPATH,'//span[contains(.,"2015")]')
    DEGREEFIELD = (By.XPATH, '//label[contains(.,"Degree")]/following-sibling::div/child::div/child::div/child::input')
    ADDBUTTTON = (By.XPATH, '(//button[@class="StyledButton-sc-323bzc-0 bDapPz"])')
    TEXTTOBEVERIFIEDDD = (By.XPATH, '//H4[contains(.,"SRM University")]')
    EDITTTBUTTON = (By.XPATH, '//h3[contains(.,"Education")]/parent::div[1]/parent::div[1]/child::div[2]/child::div[1]/child::div/child::div[3]/child::button')
    EDITUNIVERSITYNAMEFIELD = (By.NAME, 'schoolName')
    SAVEBUTTONNNN = (By.XPATH, '//button[contains(.,"Save")]')
    ALERTTTT = (By.XPATH, '//span[contains(.,"required")]')
    GETINPUTTEXTANDVEIFY1 = '//h3[contains(.,"Education")]/parent::div/following-sibling::div/child::div[last()]/child::div/child::div/child::div/child::div/child::h4'
    GETEDITEDTEXTANDVERIFY1 = '//h3[contains(.,"Education")]/parent::div/following-sibling::div/child::div[1]/child::div/child::div/child::div/child::div/child::h4'

    # --- Profile Picture Section Page Object Locators ---
    PROFILEPICTURESECTIONEDITBUTTON = (By.XPATH, '//div[@class="StyledBox-sc-13pk1d4-0 bmwFVH"]/child::span/following-sibling::button')
    CROSSBUTTONPROFILEPICTURESECTION = (By.XPATH, '//*[@id="root"]/div/div/main/div/div/div/div[1]/div[2]/div/div[2]/div[2]/form/div[2]/button')
    ADDANOTHERPROFILEPICTURESECTIONN = (By.XPATH, '(//button[contains(.,"Upload New Profile Picture")]/parent::p/parent::div/parent::form/child::div[last()-1]/child::button/child::div)')
    INPUTFIELDPROFILEPICTURESECTION = (By.XPATH, '//button[contains(.,"Upload New Profile Picture")]/parent::p/parent::div/following-sibling::div/child::div/child::div/child::div/child::div/child::input')
    SAVEBUTTONPROFILEPICTURESECTON = (By.XPATH, '//button[text()="Save"]')
    NEWINPUTFIELDFROMADDANOTHER = (By.XPATH, '(//form/child::div)[last()-2]/child::div/child::div/child::div/child::div/child::input')
    GETINPUTTEXTANDVERIFYELEMENT = '//button[text()="Share"]/parent::div/preceding-sibling::span'
    GETINPUTTEXTFROMADDANOTHER = '//button[text()="Share"]/parent::div/preceding-sibling::span'
    GETNULLALERT = '//*[contains(.,"required'
    GETCHARLIMITALERT = '//*[contains(.,"Invalid Input'

    # --- Preferences Section Page Object Locators ---
    EDITBOTTTON = (By.XPATH, '//h3[contains(.,"Preferences")]/parent::div/child::button')
    UPTO100 = (By.XPATH, '//span[contains(.,"Up to 100%")]/parent::label/child::div/child::div')
    REMOTEOPTIONCHECKBOX = (By. XPATH, '//span[contains(.,"Would also like the option to work remotely")]/parent::label/child::div/child::div')
    MINMUMREVENUEFIELD = (By.XPATH, '//span[contains(.,"$0 - $250M")]/preceding-sibling::div/child::div/*')
    MINMUMREVENUEFIELDCHECK = (By.XPATH, '//span[contains(.,"$0 - $250M")]/preceding-sibling::div/child::div')
    MAXIMUMREVENUEFIELD = (By.XPATH, '//label[contains(.,"Maximum")]/parent::div/child::div/child::div/child::div/child::input')
    ENGINEERINGTAB = (By.XPATH, '//div[@data-rbd-drag-handle-draggable-id="5"]/child::div/child::button/child::div')
    CROSS = (By.XPATH, '//div[@data-rbd-drag-handle-draggable-id="5"]/child::div/child::button/child::div//*[@aria-label="FormClose"]')
    INDUSTRYTAB = (By.XPATH,'//h4[contains(.,"Add more industries")]/parent::div/child::div/child::div/child::div/child::input')
    SAVVVVEBUTTON = (By.XPATH,'//button[contains(.,"Save")]')
    ADDANOTHERLOCATIION = (By.XPATH, '(//div[contains(.,"Add another")])[15]')
    CITYFIELD = (By.XPATH, '(//div[@data-rbd-droppable-id="LocationsForm"]/child::div[last()]/child::div/child::div/child::div/child::div/child::div/child::div/child::input)[1]')
    STATEFELD = (By.XPATH, '(//div[@data-rbd-droppable-id="LocationsForm"]/child::div[last()]/child::div/child::div/child::div/child::div/child::div/child::div/child::input)[2]')
    SELECTENGINEERINGFROMDROPDOWN = (By.XPATH, '(//button[contains(.,"Engineering")])[1]')
    TEXTTOBEVERIFIED = (By.XPATH, '//strong[contains(.,"Engineering")]')
    CHECKENGINEERINGTAB = '//div[@data-rbd-drag-handle-draggable-id="5"]/child::div/child::button/child::div[contains(.,"Engineering")]'
    VERIFYTEXT = '(//span[contains(.,"Gurugram")])[last()]'
    CLICKOUTSIDELOCATION = '//h4[contains(.,"Locations")]'

    # --- Skill Section Page Object Locators ---
    EDITBUTTONSKILLS = (By.XPATH, '//h3[contains(.,"Skills & Expertise")]/parent::div/child::button')
    SKILLSINPUTFIELD = (By.XPATH, '//h4[contains(.,"Add more skills")]/parent::div/child::div/child::div/child::div/child::input')
    SELECTSKILL = (By.XPATH, '//button[contains(.,"LOADER (General")]')
    SAVEBUTTON = (By.XPATH, '//button[contains(.,"Save")]')
    VERIFYSKILLSAVED = '(//span[contains(.,"LOADER")])[last()]'
    VERIFYALERTTEXT = '//span[contains(.,"required")]'

    # --- Summary Section Page Object Locators ---
    SUMMARYEDITBUTTON =  (By.XPATH, '//h3[contains(.,"Summary")]/parent::div/child::button')
    SUMMARYINPUTFIELD = (By.XPATH, '//label[contains(.,"Summary")]/parent::div/child::div/child::div/child::textarea')
    AVAILABILITYCHECK = (By.XPATH,'//label[contains(.,"Availability")]/parent::div/child::div/child::div/child::div/child::label/child::div')
    RATEFIELD = (By.XPATH, '//label[contains(.,"Minimum expected rate")]/parent::div/child::div/child::div/child::div/child::input')
    SAVEBBUTTTON = (By.XPATH, '//button[contains(.,"Save")]')
    SUMMARYFIELDVERIFY = (By.XPATH, '//p[contains(.,"Updated text 432")]')
    VERIFYSUMMARYTEXT = '//h3[contains(.,"Summary")]/parent::div/following-sibling::div/child::p'
    VERIFYSUMMARYCHARLIMITALERT = '//*[contains(.,"Max 500 char allowed")]'
    VERIFYSUMMARYNULLALERT = '//*[contains(.,"required")]'

    # --- Work Experience Section page object ---
    ADDANOTHERRRR = (By.XPATH, '//h3[contains(.,"Experience")]/parent::div/following-sibling::div/child::button/child::div')
    COMPANYNAMEFIELD = (By.XPATH, '//label[contains(.,"Company Name")]/parent::div/child::div/child::div/child::div/child::input')
    JOBTITLEFIELD = (By.XPATH, '//label[contains(.,"Your Job Title")]/parent::div/child::div/child::div/child::div/child::input')
    STARTDATE = (By.XPATH, '//input[@id="new-experience-start-date-month__input"]')
    MARCH = (By.XPATH, '(//span[@class="StyledText-sc-1sadyjn-0 hLVcPf"])[3]')
    JOBDESCRIPTION = (By.XPATH, '//label[contains(.,"Description")]/parent::div[1]/child::div[1]/child::div[1]/child::textarea[1]')
    ADDBUTTONN = (By.XPATH, '//h3[contains(.,"Experiences")]/parent::div/following-sibling::div/child::div[last()]/child::div[last()]/child::button[2]')
    EDITBUTTTON = (By.XPATH, '(//h3[contains(.,"Experiences")]/parent::div/following-sibling::div/child::div/child::div/child::div[3]/child::button)[1]')
    DESCRIPTIONFIELD = (By.XPATH, '//label[contains(.,"Description")]/following-sibling::div/child::div/child::textarea')
    SAVVVEBUTTON = (By.XPATH, '//button[contains(.,"Save")]')
    INPUTTEXTVERIFY = '(//h3[contains(.,"Experiences")]/parent::div/following-sibling::div/child::div[1]/child::div/child::div/child::div/parent::div/parent::div/parent::div/parent::div/child::div)[1]/child::div/child::div/child::div/child::div/child::h4'
    EDITEDSAVEDTEXTVERIFY = '(//h3[contains(.,"Experiences")]/parent::div/following-sibling::div/child::div/child::div/child::div/child::div/child::div/child::p)[1]'
    ALERTTEXTVERIFY1 = '//span[contains(.,"required")]'
    ALERTTEXTVERIFY2 = '//span[contains(.,"Invalid Company Name")]'
