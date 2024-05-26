class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        day_values = ["Friday", "Saturday","Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"]
        months_values = {
            1:31,
            2:28,
            3:31,
            4:30,
            5:31,
            6:30,
            7:31,
            8:31,
            9:30,
            10:31,
            11:30,
            12:31,
        }
        """
        we have to account for leap year
        jan 1 1971 was a friday
        1972 was first leap year
        we discoutn this year as it will be accounted for in days
        """
        num_years_past = year - 1971
        leap_offset = (year - 1972)//4
        if year == 2100 or year%4==0:
            leap_offset-=1
        
        days_in_years = num_years_past * 365 + leap_offset
        
        """
        leap year and months
        """
        if (year - 1972)%4 == 0 and year != 2100:
            months_values[2] = 29
        days_in_months = 0
        for i in range(1, month):
            days_in_months+=months_values[i]
        
        total_days = day + days_in_months + days_in_years
        
        day_of_week = total_days%7
        
        return day_values[day_of_week]