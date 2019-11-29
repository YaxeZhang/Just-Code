class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        import datetime, calendar
        return calendar.day_name[datetime.date(year, month, day).weekday()]