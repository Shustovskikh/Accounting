from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import datetime
# import table15 - Imp. Google tables (pip install table15)

if __name__ == '__main__':
    print(f'Current {datetime.today().strftime("%d.%m.%Y")}')
    calculate_salary()
    get_employees()