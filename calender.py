import calendar
from fpdf import FPDF


class PDF(FPDF):
    def basic_calendar(self, heading, data):
        days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
        self.set_font("helvetica", "B", 30)
        self.cell(0, 20, heading, 1, align='C')
        self.ln()
        cell_width = self.epw / 7
        self.set_font("helvetica", size=25)
        self.set_fill_color(216, 248, 255)
        for d in range(0, 7):
            self.cell(cell_width, 15, days[d], 1, fill=True)
        self.set_font("helvetica", "", 20, )
        self.ln()

        for row in data:
            for col in row:
                self.cell(cell_width, 27, str(col), 1, align='L')
            self.ln()


class Calendar:

    def calendar_data(year, month):
        months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
                  "November", "December"]

        month_table = []
        day_month = calendar.monthrange(year, month)
        first_day = day_month[0]
        date_day = 1
        for weeks in range(0, 5):
            week = []
            for day in range(0, 7):
                if weeks == 0 and day < first_day:
                    week.append("")
                elif weeks == 4 and date_day > day_month[1]:
                    week.append("")
                else:
                    week.append(date_day)
                    date_day += 1

            month_table.append(week)
            cal_data = (month_table, months[month - 1])
        return cal_data


if __name__ == '__main__':
    month = int(input("Insert month: "))
    year = int(input("Insert Year: "))
    cal_info = Calendar.calendar_data(year, month)
    header = [str(cal_info[1]), str(year)]
    month = header[0]
    year = header[1]
    pdf = PDF(orientation='L', format='A4')
    pdf.set_title(header[0] + "  " + header[1])
    pdf.set_font("helvetica", size=14)
    pdf.add_page()
    pdf.basic_calendar(month + "  " + year, cal_info[0])
    pdf.output("{} {}.pdf".format(month, year))
