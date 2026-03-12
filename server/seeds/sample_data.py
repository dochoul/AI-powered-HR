"""테스트용 샘플 데이터 시딩 스크립트

Usage: python -m server.seeds.sample_data
"""
import asyncio
from datetime import date, datetime

from sqlalchemy import select

from server.models.database import async_session, engine, Base
from server.models.department import Department
from server.models.position import Position
from server.models.employee import Employee
from server.models.user_slack_mapping import UserSlackMapping
from server.models.employee_role import EmployeeRole


async def seed():
    # 테이블 생성
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    async with async_session() as session:
        # 이미 데이터가 있으면 스킵
        existing = await session.execute(select(Department).limit(1))
        if existing.scalar_one_or_none():
            print("Data already seeded. Skipping.")
            return

        # 부서
        departments = [
            Department(id=1, name="경영지원팀"),
            Department(id=2, name="개발팀"),
            Department(id=3, name="마케팅팀"),
            Department(id=4, name="영업팀"),
            Department(id=5, name="디자인팀"),
            Department(id=6, name="인사팀"),
        ]
        session.add_all(departments)

        # 직급
        positions = [
            Position(id=1, name="사원", level=1),
            Position(id=2, name="대리", level=2),
            Position(id=3, name="과장", level=3),
            Position(id=4, name="차장", level=4),
            Position(id=5, name="부장", level=5),
            Position(id=6, name="이사", level=6),
            Position(id=7, name="상무", level=7),
            Position(id=8, name="전무", level=8),
            Position(id=9, name="부사장", level=9),
            Position(id=10, name="사장", level=10),
        ]
        session.add_all(positions)
        await session.flush()

        # 직원 (30명)
        employees = [
            # 경영진
            Employee(id=1, name="이대표", email="ceo@a-company.com", phone="010-0000-0001",
                     birth_date=date(1965, 3, 15), hire_date=date(2000, 1, 1),
                     department_id=1, position_id=10, title="대표이사",
                     annual_salary=200_000_000, salary_updated_at=datetime(2026, 1, 1)),
            Employee(id=2, name="박상무", email="park.sm@a-company.com", phone="010-0000-0002",
                     birth_date=date(1970, 7, 20), hire_date=date(2005, 3, 1),
                     department_id=1, position_id=7, title="경영총괄",
                     annual_salary=150_000_000, salary_updated_at=datetime(2026, 1, 1)),

            # 경영지원팀
            Employee(id=3, name="최지원", email="jiwon.choi@a-company.com", phone="010-1111-0001",
                     birth_date=date(1985, 5, 10), hire_date=date(2015, 4, 1),
                     department_id=1, position_id=5, title="팀장",
                     annual_salary=85_000_000, salary_updated_at=datetime(2026, 1, 1)),
            Employee(id=4, name="정하늘", email="haneul.jung@a-company.com", phone="010-1111-0002",
                     birth_date=date(1992, 11, 25), hire_date=date(2020, 3, 2),
                     department_id=1, position_id=2,
                     annual_salary=48_000_000, salary_updated_at=datetime(2026, 1, 1)),

            # 개발팀
            Employee(id=5, name="한승우", email="seungwoo.han@a-company.com", phone="010-2222-0001",
                     birth_date=date(1980, 1, 5), hire_date=date(2012, 7, 1),
                     department_id=2, position_id=5, title="팀장",
                     annual_salary=92_000_000, salary_updated_at=datetime(2026, 1, 1)),
            Employee(id=6, name="김민수", email="minsu.kim@a-company.com", phone="010-2222-0002",
                     birth_date=date(1988, 8, 12), hire_date=date(2020, 3, 15),
                     department_id=2, position_id=3, title="백엔드파트장",
                     annual_salary=65_000_000, salary_updated_at=datetime(2026, 1, 1)),
            Employee(id=7, name="이지현", email="jihyun.lee@a-company.com", phone="010-2222-0003",
                     birth_date=date(1990, 4, 3), hire_date=date(2019, 6, 1),
                     department_id=2, position_id=3, title="프론트파트장",
                     annual_salary=63_000_000, salary_updated_at=datetime(2026, 1, 1)),
            Employee(id=8, name="정도현", email="dohyun.jung@a-company.com", phone="010-2222-0004",
                     birth_date=date(1993, 12, 1), hire_date=date(2021, 1, 4),
                     department_id=2, position_id=2,
                     annual_salary=52_000_000, salary_updated_at=datetime(2026, 1, 1)),
            Employee(id=9, name="오유나", email="yuna.oh@a-company.com", phone="010-2222-0005",
                     birth_date=date(1994, 6, 18), hire_date=date(2022, 3, 7),
                     department_id=2, position_id=2,
                     annual_salary=48_000_000, salary_updated_at=datetime(2026, 1, 1)),
            Employee(id=10, name="송태민", email="taemin.song@a-company.com", phone="010-2222-0006",
                     birth_date=date(1997, 9, 30), hire_date=date(2024, 1, 2),
                     department_id=2, position_id=1,
                     annual_salary=42_000_000, salary_updated_at=datetime(2026, 1, 1)),
            Employee(id=11, name="강서윤", email="seoyun.kang@a-company.com", phone="010-2222-0007",
                     birth_date=date(1998, 2, 14), hire_date=date(2024, 7, 1),
                     department_id=2, position_id=1,
                     annual_salary=40_000_000, salary_updated_at=datetime(2026, 1, 1)),
            Employee(id=12, name="임재혁", email="jaehyuk.lim@a-company.com", phone="010-2222-0008",
                     birth_date=date(1999, 5, 22), hire_date=date(2025, 1, 6),
                     department_id=2, position_id=1,
                     annual_salary=38_000_000, salary_updated_at=datetime(2026, 1, 1)),

            # 마케팅팀
            Employee(id=13, name="이서연", email="seoyeon.lee@a-company.com", phone="010-3333-0001",
                     birth_date=date(1982, 10, 8), hire_date=date(2014, 2, 1),
                     department_id=3, position_id=5, title="팀장",
                     annual_salary=78_000_000, salary_updated_at=datetime(2026, 1, 1)),
            Employee(id=14, name="박준혁", email="junhyuk.park@a-company.com", phone="010-3333-0002",
                     birth_date=date(1991, 3, 17), hire_date=date(2018, 9, 1),
                     department_id=3, position_id=3,
                     annual_salary=58_000_000, salary_updated_at=datetime(2026, 1, 1)),
            Employee(id=15, name="최수빈", email="subin.choi@a-company.com", phone="010-3333-0003",
                     birth_date=date(1995, 7, 29), hire_date=date(2021, 4, 5),
                     department_id=3, position_id=2,
                     annual_salary=47_000_000, salary_updated_at=datetime(2026, 1, 1)),
            Employee(id=16, name="정우진", email="woojin.jung@a-company.com", phone="010-3333-0004",
                     birth_date=date(1996, 1, 11), hire_date=date(2023, 2, 1),
                     department_id=3, position_id=2,
                     annual_salary=44_000_000, salary_updated_at=datetime(2026, 1, 1)),
            Employee(id=17, name="김하은", email="haeun.kim@a-company.com", phone="010-3333-0005",
                     birth_date=date(2000, 4, 5), hire_date=date(2025, 3, 3),
                     department_id=3, position_id=1,
                     annual_salary=35_000_000, salary_updated_at=datetime(2026, 1, 1)),

            # 영업팀
            Employee(id=18, name="윤성호", email="sungho.yoon@a-company.com", phone="010-4444-0001",
                     birth_date=date(1983, 8, 25), hire_date=date(2013, 5, 1),
                     department_id=4, position_id=5, title="팀장",
                     annual_salary=82_000_000, salary_updated_at=datetime(2026, 1, 1)),
            Employee(id=19, name="김민수", email="minsu2.kim@a-company.com", phone="010-4444-0002",
                     birth_date=date(1995, 11, 3), hire_date=date(2022, 8, 1),
                     department_id=4, position_id=2,
                     annual_salary=45_000_000, salary_updated_at=datetime(2026, 1, 1)),
            Employee(id=20, name="배하린", email="harin.bae@a-company.com", phone="010-4444-0003",
                     birth_date=date(1997, 2, 28), hire_date=date(2024, 6, 1),
                     department_id=4, position_id=1,
                     annual_salary=38_000_000, salary_updated_at=datetime(2026, 1, 1)),

            # 디자인팀
            Employee(id=21, name="조예린", email="yerin.jo@a-company.com", phone="010-5555-0001",
                     birth_date=date(1987, 6, 12), hire_date=date(2016, 3, 1),
                     department_id=5, position_id=4, title="팀장",
                     annual_salary=72_000_000, salary_updated_at=datetime(2026, 1, 1)),
            Employee(id=22, name="신동현", email="donghyun.shin@a-company.com", phone="010-5555-0002",
                     birth_date=date(1993, 9, 7), hire_date=date(2020, 1, 6),
                     department_id=5, position_id=2,
                     annual_salary=50_000_000, salary_updated_at=datetime(2026, 1, 1)),
            Employee(id=23, name="윤서준", email="seojun.yoon@a-company.com", phone="010-5555-0003",
                     birth_date=date(1998, 12, 20), hire_date=date(2026, 3, 2),
                     department_id=5, position_id=1,
                     annual_salary=36_000_000, salary_updated_at=datetime(2026, 1, 1)),

            # 인사팀
            Employee(id=24, name="강미래", email="mirae.kang@a-company.com", phone="010-6666-0001",
                     birth_date=date(1984, 4, 16), hire_date=date(2013, 9, 1),
                     department_id=6, position_id=5, title="팀장",
                     annual_salary=80_000_000, salary_updated_at=datetime(2026, 1, 1)),
            Employee(id=25, name="홍길동", email="gildong.hong@a-company.com", phone="010-6666-0002",
                     birth_date=date(1991, 7, 7), hire_date=date(2019, 5, 1),
                     department_id=6, position_id=3,
                     annual_salary=55_000_000, salary_updated_at=datetime(2026, 1, 1)),
            Employee(id=26, name="서지민", email="jimin.seo@a-company.com", phone="010-6666-0003",
                     birth_date=date(1996, 10, 30), hire_date=date(2023, 1, 2),
                     department_id=6, position_id=1,
                     annual_salary=37_000_000, salary_updated_at=datetime(2026, 1, 1)),

            # 퇴직자
            Employee(id=27, name="한소희", email="sohee.han@a-company.com", phone="010-7777-0001",
                     birth_date=date(1992, 3, 8), hire_date=date(2018, 4, 1),
                     resign_date=date(2025, 6, 30), status="resigned",
                     department_id=3, position_id=3,
                     annual_salary=56_000_000, salary_updated_at=datetime(2025, 1, 1)),

            # 최근 입사자
            Employee(id=28, name="배다은", email="daeun.bae@a-company.com", phone="010-5555-0004",
                     birth_date=date(1999, 8, 15), hire_date=date(2026, 3, 10),
                     department_id=5, position_id=2,
                     annual_salary=46_000_000, salary_updated_at=datetime(2026, 3, 1)),
        ]
        session.add_all(employees)
        await session.flush()

        # 슬랙 매핑 (경영진 + 테스트용)
        slack_mappings = [
            UserSlackMapping(employee_id=1, slack_user_id="U_CEO_001"),       # 이대표 (사장)
            UserSlackMapping(employee_id=2, slack_user_id="U_EXEC_002"),      # 박상무 (상무)
            UserSlackMapping(employee_id=5, slack_user_id="U_MGR_005"),       # 한승우 (개발팀장)
            UserSlackMapping(employee_id=6, slack_user_id="U_EMP_006"),       # 김민수 (개발팀 과장)
            UserSlackMapping(employee_id=24, slack_user_id="U_HR_024"),       # 강미래 (인사팀장)
        ]
        session.add_all(slack_mappings)

        # 역할
        roles = [
            EmployeeRole(employee_id=1, role="executive"),   # 이대표
            EmployeeRole(employee_id=2, role="executive"),   # 박상무
            EmployeeRole(employee_id=5, role="manager"),     # 한승우 (팀장)
            EmployeeRole(employee_id=6, role="employee"),    # 김민수 (일반)
            EmployeeRole(employee_id=24, role="hr_admin"),   # 강미래 (HR)
        ]
        session.add_all(roles)

        await session.commit()
        print(f"Seeded: 6 departments, 10 positions, {len(employees)} employees, "
              f"{len(slack_mappings)} slack mappings, {len(roles)} roles")


if __name__ == "__main__":
    asyncio.run(seed())
