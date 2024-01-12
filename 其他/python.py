def dan():
    #单选或多选

    j = browser.find_element_by_xpath('//*[@id="app"]/section/div[2]/div[4]/div/p[1]').text

    if j=='当前题型已学完':
        print('已完')
        return 1
    else:
        pass

    x = browser.find_elements_by_css_selector('a')

    for i in x:

        if 'A' == i.text:
            try:
                i.click()
            except:
                pass
        else:
            pass

   
    time.sleep(0.5)
    x = browser.find_elements_by_css_selector('a')
    for i in x:

        if '查看解析' == i.text:
            i.click()
            time.sleep(0.5)
        else:
            pass
    
    xuan = browser.find_element_by_xpath('//*[@id="app"]/section/div[2]/div[4]/div/div[2]/ul')
    xuan = xuan.get_attribute('innerHTML')
    xuan = bs(xuan,'lxml')
    xuan = xuan.findAll('li')

    mu = browser.find_element_by_xpath('//*[@id="app"]/section/div[2]/div[4]/div/h1').text
    
    try:
        daan[mu]
        print('已经有答案')
    except:
        an =[]
        a = browser.find_element_by_xpath('//*[@id="app"]/section/div[2]/div[4]/div/div[3]/p/span[1]').text

        a = re.sub('正确答案:','',a)
        a = re.sub(' ','',a)

        an.append(a)
        
        for i in xuan:
            if i.text[0] in a:
                an.append(i.text)
            else:
                pass
            
        daan[mu]= an

        print(mu)
        print(an)
        print(len(daan))

    browser.find_element_by_xpath('//*[@id="app"]/section/div[2]/div[4]/div/p/a[1]').click()


def pan():

    j = browser.find_element_by_xpath('//*[@id="app"]/section/div[2]/div[4]/div/p[1]').text

    if j=='当前题型已学完':
        print('已完')
        return 1
    else:
        pass

    mu = browser.find_element_by_xpath('//*[@id="app"]/section/div[2]/div[4]/div/h1').text

    mu = re.sub('\n请输入答案:   ','',mu)

    try:
        browser.find_element_by_xpath('//*[@id="app"]/section/div[2]/div[4]/div/div[2]/ul/li[1]/a/span').click()
    except:
        pass

    x = browser.find_elements_by_css_selector('a')
    for i in x:

        if '查看解析' == i.text:
            i.click()
            time.sleep(0.5)
        else:
            pass
        
    time.sleep(0.3)

    try:
        daan[mu]
        print('已经有答案')
    except:
        an =[]
        try:
            a = browser.find_element_by_xpath('//*[@id="app"]/section/div[2]/div[4]/div/div[3]/p/span[1]').text
        except:
            a = browser.find_element_by_xpath('//*[@id="app"]/section/div[2]/div[4]/div/div[2]/p/span[1]').text

        a = re.sub('正确答案:','',a)
        a = re.sub(' ','',a)
        an.append(a)
        daan[mu]= an
        print(mu)
        print(an)
        print(len(daan))


    browser.find_element_by_xpath('//*[@id="app"]/section/div[2]/div[4]/div/p/a[1]').click()
    
