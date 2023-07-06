#! /usr/bin/python3

import sys
from countryinfo import CountryInfo

def country():
    input = sys.argv[1]
    country = CountryInfo(input)
    print(country.name())
    print("--------")
    print("Capital: " + country.capital())
    print("Region: " + country.region())
    print("Language: " + ', '.join([p for p in country.languages()]))
    print("Area: " + str(country.area()) + " Km²")
    print("Population: " + str(country.population()) + " Peoples")
    print("Currency: " + ', '.join([p for p in country.currencies()]))
    if country.timezones() == None:
        print("Timezone: None")
    else:
        print("Timezone: " +  ', '.join([p for p in country.timezones()]))
    print("Calling Code: " +  ', '.join([p for p in country.calling_codes()]))
    print("TLD: " +  ', '.join([p for p in country.tld()]))

def error():
    try:
        input = sys.argv[1]
        country = CountryInfo(input)
    except:
        print("Select a country")
        print("--------")
        return False
    try:
        country.region()
    except KeyError:
        print("Invalid country")
        print("--------")
        return False

def help():
    print("Usage: countryfetch [COUNTRY]")
    print("The [COUNTRY] argument take the Alpha-2 code, a single word, or a multiple word between quotations marks.")
    print("Alpha-2 Code: countryfetch io")
    print("Single: countryfetch palau")
    print("Multiple: countryfetch \'french polynesia\'")

def main():
    if error() == False:
        help()
    else:
        country()

main()
