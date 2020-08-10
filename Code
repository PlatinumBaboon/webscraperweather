import requests
import pandas as pd
from bs4 import BeautifulSoup

class RteWeather:

    Temp1 = []
    day1 = []
    time1 = []
    hour_temp1 = []
    rain1 = []
    icon = []
    wind1 = []

    def page_Url(Url):
        headers = {"User-Agent": "Mozilla/5.0"}
        page = requests.get(Url, headers=headers)
        soup: BeautifulSoup = BeautifulSoup(page.content, 'html.parser')
        return soup

    Url1 = page_Url("https://www.rte.ie/weather/22259-dublin/")

    time = Url1.find_all(class_='hour-title')
    hour_temp = Url1.find_all(class_='temperature')
    rain = Url1.find_all(class_='rain-label visible')
    wind = Url1.find_all(class_='wind-label visible')
    weather = Url1.find_all(class_='forecast-icon')
    day = Url1.find_all(class_='day-name')
    Temp = Url1.find_all(class_='day-temperature')

    for e in Temp:
        Temp1.append(e.text)
    for e in day:
        day1.append(e.text)
    for e in time[0:13]:
        time1.append(e.text)
    for e in hour_temp[2:15]:
        hour_temp1.append(e.text)
    for e in rain[0:13]:
        rain1.append(e.text)
    for e in wind[0:13]:
        wind1.append(e.text)
    for i in weather[7:20]:
        num = str(i).split('"')
        for e in num:
            if e == ' title=':
                firstnum = num.index(e) + 1
                icon.append(num[firstnum].title())

    Weather3 = {'Time': time1,
                'Temp': hour_temp1,
                'Rain': rain1,
                'Wind': wind1,
                'Weather': icon,
               }
    Weather2 = {'Day': day1[0:7],
                'Temp': Temp1[0:7]
               }

    hourlyweather = pd.DataFrame(Weather3, columns=['Time', 'Temp', 'Weather', 'Rain', 'Wind'])
    dailytemp = pd.DataFrame(Weather2, columns=['Day', 'Temp'])

class ACCUWeather:

    HTemp = []
    day1 = []
    Ltemp = []
    weather1 = []
    rain1 = []
    time1 = []
    temp1 = []
    Weather1 = []
    rain3 = []
    wind3 = []
    time1B = []
    temp1B = []
    Weather1B = []
    rain3B = []
    wind3B = []

    def page_Url(Url):
        headers = {"User-Agent": "Mozilla/5.0"}
        page = requests.get(Url, headers=headers)
        soup: BeautifulSoup = BeautifulSoup(page.content, 'html.parser')
        return soup

    Url1 = page_Url("https://www.accuweather.com/en/ie/dublin/207931/daily-weather-forecast/207931")
    Url2 = page_Url("https://www.accuweather.com/en/ie/dublin/207931/hourly-weather-forecast/207931")
    Url3 = page_Url("https://www.accuweather.com/en/ie/dublin/207931/hourly-weather-forecast/207931?day=2")

    Day = Url1.find_all(class_='module-header dow date')
    high_temp = Url1.find_all(class_='high')
    low_temp = Url1.find_all(class_='low')
    weather = Url1.find_all(class_='phrase')
    rain = Url1.find_all(class_='precip')

    time = Url2.find_all(class_='date')
    Temp = Url2.find_all(class_='temp metric')
    Weather = Url2.find_all(class_='phrase')
    rain2 = Url2.find_all(class_='precip')
    wind2 = Url2.find_all(class_='value')

    timeB = Url3.find_all(class_='date')
    TempB = Url3.find_all(class_='temp metric')
    WeatherB = Url3.find_all(class_='phrase')
    rain2B = Url3.find_all(class_='precip')
    wind2B = Url3.find_all(class_='value')

    for e in Day:
        day1.append(e.text)
    for e in high_temp:
        HTemp.append(e.text)
    for e in low_temp:
        x = e.text
        du2 = x.replace('/', '')
        Ltemp.append(du2)
    for i in rain:
        num = str(i).split('>')
        num2 = num[-2].replace("\n\t", "")
        num3 = num2.replace("</div", "")
        num4 = num3.replace("\t", "")
        rain1.append(num4)
    for e in weather:
        p = e.text
        pu = p.replace('\n\t\t\t\t', '')
        tu = pu.replace('\n\t\t\t', '')
        weather1.append(tu)
    for e in time:
        u = e.text
        yu = u.replace('\n', '')
        ku = yu.replace('\t', '')
        ou = ku.split('M')
        ku1 = ou[0] + 'M'
        time1.append(ku1)
    for e in Temp:
        u = e.text
        yu = u.replace('\n', '')
        ku = yu.replace('\t', '')
        temp1.append(ku)
    for e in Weather:
        p = e.text
        pu = p.replace('\n\t\t\t', '')
        tu = pu.replace('\n\t\t', '')
        Weather1.append(tu)
    for e in rain2:
        p = e.text
        pu = p.replace('\n\n\t\t', '')
        tu = pu.replace('\n\t', '')
        rain3.append(tu)
    for e in wind2:
        f = e.text.split()
        if f[-1] == 'km/h':
            if len(f) == 3:
                wind3.append(' '.join(f))
    for e in timeB:
        u = e.text
        yu = u.replace('\n', '')
        ku = yu.replace('\t', '')
        ou = ku.split('M')
        ku1 = ou[0] + 'M'
        time1B.append(ku1)
    for e in TempB:
        u = e.text
        yu = u.replace('\n', '')
        ku = yu.replace('\t', '')
        temp1B.append(ku)
    for e in WeatherB:
        p = e.text
        pu = p.replace('\n\t\t\t', '')
        tu = pu.replace('\n\t\t', '')
        Weather1B.append(tu)
    for e in rain2B:
        p = e.text
        pu = p.replace('\n\n\t\t', '')
        tu = pu.replace('\n\t', '')
        rain3B.append(tu)
    for e in wind2B:
        f = e.text.split()
        if f[-1] == 'km/h':
            if len(f) == 3:
                wind3B.append(' '.join(f))

    if len(time1) < 13:
        for i in time1B[0:(13-len(time1))]:
            time1.append(i)
    if len(temp1) < 13:
        for i in temp1B[0:(13 - len(temp1))]:
            temp1.append(i)
    if len(Weather1) < 13:
        for i in Weather1B[0:(13 - len(Weather1))]:
            Weather1.append(i)
    if len(rain3) < 13:
        for i in rain3B[0:(13 - len(rain3))]:
            rain3.append(i)
    if len(wind3) < 13:
        for i in wind3B[0:(13 - len(wind3))]:
            wind3.append(i)

    Weather2 = {'Day': day1[0:7],
                'Temp-High': HTemp[0:7],
                'Temp-Low': Ltemp[0:7],
                'Weather': weather1[0:7],
                'Rain': rain1[0:7],
                }
    Weather3 = {'Time': time1[0:13],
                'Temp': temp1[0:13],
                'Weather': Weather1[0:13],
                'Rain': rain3[0:13],
                'Wind': wind3[0:13],
                }
    hourlyweather = pd.DataFrame(Weather3, columns=['Time', 'Temp', 'Weather', 'Rain', 'Wind'])
    dailytemp = pd.DataFrame(Weather2, columns=['Day', 'Temp-High', 'Temp-Low', 'Weather', 'Rain'])

class Weathercom:
    htemp = []
    day1 = []
    Ltemp = []
    wind3 = []
    rain1 = []
    Weather1= []
    time1 = []
    temp1B = []
    Weather1B = []
    rain3B = []
    wind3B = []
    rain3 = []

    def page_Url(Url):
        headers = {"User-Agent": "Mozilla/5.0"}
        page = requests.get(Url, headers=headers)
        soup: BeautifulSoup = BeautifulSoup(page.content, 'html.parser')
        return soup

    Url1 = page_Url('https://weather.com/en-IE/weather/tenday/l/15128cb9dec08a69b64d22f987d80c90694877543bfc1e7083db3b20c0526b82')
    Url2 = page_Url('https://weather.com/en-IE/weather/hourbyhour/l/15128cb9dec08a69b64d22f987d80c90694877543bfc1e7083db3b20c0526b82')

    Day = Url1.find_all(class_='_-_-components-src-molecule-DaypartDetails-DetailsSummary-DetailsSummary--daypartName--kbngc')
    HTemp = Url1.find_all(class_='_-_-components-src-molecule-DaypartDetails-DetailsSummary-DetailsSummary--highTempValue--3PjlX')
    LTemp = Url1.find_all(class_='_-_-components-src-molecule-DaypartDetails-DetailsSummary-DetailsSummary--lowTempValue--2tesQ')
    Weather = Url1.find_all(class_='_-_-components-src-molecule-DaypartDetails-DetailsSummary-DetailsSummary--extendedData--307Ax')
    Rain = Url1.find_all(class_='_-_-components-src-molecule-DaypartDetails-DetailsSummary-DetailsSummary--precip--1a98O')
    Wind = Url1.find_all(class_='_-_-components-src-atom-WeatherData-Wind-Wind--windWrapper--3Ly7c undefined')

    time = Url2.find_all(class_='_-_-components-src-molecule-DaypartDetails-DetailsSummary-DetailsSummary--daypartName--kbngc')
    temp = Url2.find_all(class_='_-_-components-src-molecule-DaypartDetails-DetailsSummary-DetailsSummary--tempValue--jEiXE')
    weather = Url2.find_all(class_='_-_-components-src-molecule-DaypartDetails-DetailsSummary-DetailsSummary--extendedData--307Ax')
    Rain1 = Url2.find_all(class_='_-_-components-src-molecule-DaypartDetails-DetailsSummary-DetailsSummary--precip--1a98O')
    Wind1 = Url2.find_all(class_='_-_-components-src-atom-WeatherData-Wind-Wind--windWrapper--3Ly7c undefined')

    for e in Day:
        day1.append(e.text)
    for e in HTemp:
        htemp.append(e.text)
    for e in LTemp:
        Ltemp.append(e.text)
    for e in Weather:
        Weather1.append(e.text)
    for e in Rain:
        rain1.append(e.text)
    for e in Wind:
        wind3.append(e.text)
    for e in time:
        time1.append(e.text)
    for e in temp:
        temp1B.append(e.text)
    for e in weather:
        Weather1B.append(e.text)
    for e in Rain1:
        rain3.append(e.text)
    for e in Wind1:
        wind3B.append(e.text)

    Weather2 = {'Day': day1[0:7],
                'Temp-High': htemp[0:7],
                'Temp-Low': Ltemp[0:7],
                'Weather': Weather1[0:7],
                'Rain': rain1[0:7],
                'Wind': wind3[0:7],
                }
    Weather3 = {'Time': time1[0:13],
                'Temp': temp1B[0:13],
                'Weather': Weather1B[0:13],
                'Rain': rain3[0:13],
                'Wind': wind3B[0:13],
                }
    
    hourlyweather = pd.DataFrame(Weather3, columns=['Time', 'Temp', 'Weather', 'Rain', 'Wind'])
    dailytemp = pd.DataFrame(Weather2, columns=['Day', 'Temp-High', 'Temp-Low', 'Weather', 'Rain', 'Wind'])

class DarkSky:
    HTemp = []
    day1 = []
    Ltemp = []
    weather1 = [] 
    rain3 = []

    def page_Url(Url):
        headers = {"User-Agent": "Mozilla/5.0"}
        page = requests.get(Url, headers=headers)
        soup: BeautifulSoup = BeautifulSoup(page.content, 'html.parser')
        return soup

    Url1 = page_Url('https://darksky.net/forecast/53.3805,-6.2711/ca12/en')

    Day = Url1.find_all(class_='name')
    mintemp = Url1.find_all(class_='minTemp')
    maxtemp = Url1.find_all(class_='maxTemp')
    weather = Url1.find_all(class_='summary')
    rain = Url1.find_all(class_='num swip')

    for e in Day:
        u = e.text
        pu = u.replace(' ', '')
        tu = pu.replace('\n\n', '')
        day1.append(tu)
    for e in mintemp:
        u = e.text[0:2]
        Ltemp.append(u)
    for e in maxtemp:
        u = e.text[0:2]
        HTemp.append(u)
    for e in weather[2:]:
        u = e.text
        pu = u.replace('\n', '')
        weather1.append(pu)
    for e in rain:
        u = e.text
        rain3.append(u+'mm')

    Weather2 = {'Day': day1[0:7],
                'Temp-High': HTemp[0:7],
                'Temp-Low': Ltemp[0:7],
                'Weather': weather1[0:7],
                'Rain': rain3[0:7],
                }
    
    dailytemp = pd.DataFrame(Weather2, columns=['Day', 'Temp-High', 'Temp-Low', 'Weather', 'Rain'])

class AnalyseWeather:
    HTemp = []
    Ltemp = []
    temp1 = []
    rain3 = []
    wind3 = []
    rain3B = []
    
    for i in range(0, 7):
        Big = max([ACCUWeather.Weather2['Temp-High'][i][0:2], RteWeather.Weather2['Temp'][i][0:2],DarkSky.Weather2['Temp-High'][i], Weathercom.Weather2['Temp-High'][i][0:2]])
        HTemp.append(Big+RteWeather.Weather2['Temp'][0][2:4])
    for i in range(0, 7):
        Big = min([ACCUWeather.Weather2['Temp-Low'][i][0:2], RteWeather.Weather2['Temp'][i][0:2],DarkSky.Weather2['Temp-Low'][i], Weathercom.Weather2['Temp-Low'][i][0:2]])
        Ltemp.append(Big+RteWeather.Weather2['Temp'][0][2:4])
    for i in range(0, 7):
        perc = ((int(ACCUWeather.Weather2['Rain'][i].replace('%', '')) + int(Weathercom.Weather2['Rain'][i].replace('%', '')))/2)
        rain3.append(str(perc) + '%' + ' ' + DarkSky.Weather2['Rain'][i])
    for i in range(0, 13):
        a1 = ACCUWeather.Weather3['Temp'][i]
        b1 = RteWeather.Weather3['Temp'][i].replace('C', '')
        c1 = Weathercom.Weather3['Temp'][i]
        d = []
        e1 = []
        f = []
        for e in a1:
            d.append(e)
        d.pop(-1)
        a = ''.join(d)
        for e in b1:
            e1.append(e)
        e1.pop(-1)
        b = ''.join(e1)
        for e in c1:
            f.append(e)
        f.pop(-1)
        c = ''.join(d)
        Big = (int(a) + int(b) + int(c))/3
        B = str(Big).split('.')
        temp1.append(B[0] + RteWeather.Weather3['Temp'][0][-2] + RteWeather.Weather3['Temp'][0][-1])
    for i in range(0, 13):
        a1 = ACCUWeather.Weather3['Rain'][i]
        b1 = Weathercom.Weather3['Rain'][i]
        d = []
        e1 = []
        for e in a1:
            d.append(e)
        y = d.pop(-1)
        a = ''.join(d)
        for e in b1:
            e1.append(e)
        e1.pop(-1)
        b = ''.join(e1)
        Big = str((int(a) + int(b))/2) + y
        rain3B.append(Big)
    for i in range(0, 13):
        a1 = ACCUWeather.Weather3['Wind'][i]
        b1 = RteWeather.Weather3['Wind'][i]
        c1 = Weathercom.Weather3['Wind'][i]
        a = a1.split()
        j = a.pop(0)
        g = a.pop(-1)
        a2 = ''.join(a)
        b = b1.split()
        b.pop(-1)
        b2 = ''.join(b)
        c = c1.split()
        c.pop(0)
        c.pop(-1)
        c2 = ''.join(a)
        q = str((int(a2) + int(b2) + int(c2))/3).split('.')
        if int(q[-1][0]) > 4:
            wind3.append(j + ' ' + str(int(q[0]) + 1) + ' ' + g)
        else:
            wind3.append(j + ' ' + q[0] + ' ' + g)

    Weather2 = {'Day': RteWeather.Weather2['Day'],
                'Temp-High': HTemp,
                'Temp-Low': Ltemp,
                'Weather': ACCUWeather.weather1[0:7],
                'Rain': rain3,
                'Wind': Weathercom.wind3B[0:7]
                }
    Weather3 = {'Time': RteWeather.time1[0:13],
                'Temp': temp1[0:13],
                'Weather': ACCUWeather.Weather1[0:13],
                'Rain': rain3B[0:13],
                'Wind': wind3[0:13],
                }
    
    hourlyweather = pd.DataFrame(Weather3, columns=['Time', 'Temp', 'Weather', 'Rain', 'Wind'])
    dailytemp = pd.DataFrame(Weather2, columns=['Day', 'Temp-High', 'Temp-Low', 'Weather', 'Rain', 'Wind'])

print(AnalyseWeather.hourlyweather)
print(AnalyseWeather.dailytemp)
