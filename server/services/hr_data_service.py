import logging
from datetime import date

from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from server.models.department import Department
from server.models.employee import Employee
from server.models.position import Position

logger = logging.getLogger(__name__)


async def get_employee_by_name(session: AsyncSession, name: str) -> list[dict]:
    """이름으로 직원 검색 (정확 일치)"""
    result = await session.execute(
        select(Employee)
        .options(joinedload(Employee.department), joinedload(Employee.position))
        .where(Employee.name == name)
    )
    employees = result.unique().scalars().all()
    return [_employee_to_dict(e) for e in employees]


async def search_similar_names(session: AsyncSession, name: str, limit: int = 5) -> list[dict]:
    """유사 이름 검색 (LIKE)"""
    result = await session.execute(
        select(Employee)
        .options(joinedload(Employee.department), joinedload(Employee.position))
        .where(Employee.name.like(f"%{name[0]}%{name[-1]}%"))
        .where(Employee.status == "active")
        .limit(limit)
    )
    employees = result.unique().scalars().all()
    return [{"name": e.name, "department": e.department.name, "position": e.position.name} for e in employees]


async def get_employees_by_department(session: AsyncSession, department: str) -> list[dict]:
    """부서별 직원 목록 조회"""
    result = await session.execute(
        select(Employee)
        .options(joinedload(Employee.department), joinedload(Employee.position))
        .join(Department)
        .join(Position)
        .where(Department.name == department, Employee.status == "active")
        .order_by(Position.level.desc())
    )
    employees = result.unique().scalars().all()
    return [_employee_to_dict(e) for e in employees]


async def get_employees_by_position(session: AsyncSession, position: str) -> list[dict]:
    """직급별 직원 목록 조회"""
    result = await session.execute(
        select(Employee)
        .options(joinedload(Employee.department), joinedload(Employee.position))
        .join(Position)
        .where(Position.name == position, Employee.status == "active")
        .order_by(Employee.name)
    )
    employees = result.unique().scalars().all()
    return [_employee_to_dict(e) for e in employees]


async def get_recent_hires(
    session: AsyncSession, start_date: str, end_date: str
) -> list[dict]:
    """기간별 입사자 조회"""
    result = await session.execute(
        select(Employee)
        .options(joinedload(Employee.department), joinedload(Employee.position))
        .where(
            Employee.hire_date >= date.fromisoformat(start_date),
            Employee.hire_date <= date.fromisoformat(end_date),
        )
        .order_by(Employee.hire_date.desc())
    )
    employees = result.unique().scalars().all()
    return [_employee_to_dict(e) for e in employees]


async def get_employee_salary(session: AsyncSession, name: str) -> list[dict]:
    """직원 연봉 조회 (기밀)"""
    result = await session.execute(
        select(Employee)
        .options(joinedload(Employee.department), joinedload(Employee.position))
        .where(Employee.name == name)
    )
    employees = result.unique().scalars().all()
    return [
        {
            "id": e.id,
            "name": e.name,
            "department": e.department.name,
            "position": e.position.name,
            "annual_salary": e.annual_salary,
            "salary_updated_at": e.salary_updated_at.isoformat() if e.salary_updated_at else None,
        }
        for e in employees
    ]


async def get_department_salary_stats(session: AsyncSession, department: str) -> dict | None:
    """부서별 연봉 통계 (기밀)"""
    result = await session.execute(
        select(
            func.count(Employee.id).label("count"),
            func.avg(Employee.annual_salary).label("avg_salary"),
            func.max(Employee.annual_salary).label("max_salary"),
            func.min(Employee.annual_salary).label("min_salary"),
        )
        .join(Department)
        .where(Department.name == department, Employee.status == "active", Employee.annual_salary.is_not(None))
    )
    row = result.one_or_none()
    if not row or row.count == 0:
        return None

    return {
        "department": department,
        "count": row.count,
        "avg_salary": int(row.avg_salary) if row.avg_salary else 0,
        "max_salary": row.max_salary,
        "min_salary": row.min_salary,
    }


def _employee_to_dict(e: Employee) -> dict:
    """Employee 모델을 딕셔너리로 변환 (극비 필드 제외)"""
    return {
        "id": e.id,
        "name": e.name,
        "department": e.department.name,
        "position": e.position.name,
        "title": e.title,
        "hire_date": e.hire_date.isoformat(),
        "status": e.status,
        "email": e.email,
        "phone": e.phone,
        "birth_date": e.birth_date.isoformat() if e.birth_date else None,
    }
