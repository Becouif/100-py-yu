

def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False
  


user_entered_year = int(input("Enter a year: "))

def days_in_months(year, months):
  if is_leap(user_entered_year) == True:
    months[1] = 29
    
  

