#!/usr/bin/python3

age = input("What is your current age?")

#Calculates the remaining years, days, weeks and months based on the fact that we would live up to 90 years.

age_as_int = int(age)

years_remaining = 90 - age_as_int
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12 


print(f"You have {years_remaining} years left, {days_remaining} days remaining, {weeks_remaining} weeks remaining and {months_remaining} months remaining")
