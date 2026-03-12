"""Gemini Function Calling용 도구 정의"""
from google.genai import types

GEMINI_TOOLS = [
    types.Tool(
        function_declarations=[
            types.FunctionDeclaration(
                name="get_employee_by_name",
                description="직원 이름으로 인사정보를 조회합니다",
                parameters=types.Schema(
                    type="OBJECT",
                    properties={
                        "name": types.Schema(type="STRING", description="조회할 직원의 이름 (성+이름)"),
                    },
                    required=["name"],
                ),
            ),
            types.FunctionDeclaration(
                name="get_employees_by_department",
                description="부서명으로 해당 부서 소속 직원 목록을 조회합니다",
                parameters=types.Schema(
                    type="OBJECT",
                    properties={
                        "department": types.Schema(type="STRING", description="부서명"),
                    },
                    required=["department"],
                ),
            ),
            types.FunctionDeclaration(
                name="get_employees_by_position",
                description="직급으로 해당 직급의 직원 목록을 조회합니다",
                parameters=types.Schema(
                    type="OBJECT",
                    properties={
                        "position": types.Schema(type="STRING", description="직급명 (사원, 대리, 과장, 차장, 부장, 이사 등)"),
                    },
                    required=["position"],
                ),
            ),
            types.FunctionDeclaration(
                name="get_recent_hires",
                description="특정 기간 내 입사한 직원 목록을 조회합니다",
                parameters=types.Schema(
                    type="OBJECT",
                    properties={
                        "start_date": types.Schema(type="STRING", description="조회 시작일 (YYYY-MM-DD)"),
                        "end_date": types.Schema(type="STRING", description="조회 종료일 (YYYY-MM-DD)"),
                    },
                    required=["start_date", "end_date"],
                ),
            ),
            types.FunctionDeclaration(
                name="get_employee_salary",
                description="직원 이름으로 연봉 정보를 조회합니다. 기밀 등급 정보이므로 경영진/HR 담당자만 사용할 수 있습니다.",
                parameters=types.Schema(
                    type="OBJECT",
                    properties={
                        "name": types.Schema(type="STRING", description="조회할 직원의 이름 (성+이름)"),
                    },
                    required=["name"],
                ),
            ),
            types.FunctionDeclaration(
                name="get_department_salary_stats",
                description="부서명으로 해당 부서의 연봉 통계(평균, 최고, 최저)를 조회합니다. 기밀 등급 정보이므로 경영진/HR 담당자만 사용할 수 있습니다.",
                parameters=types.Schema(
                    type="OBJECT",
                    properties={
                        "department": types.Schema(type="STRING", description="부서명"),
                    },
                    required=["department"],
                ),
            ),
        ]
    )
]

# 기밀 등급 도구 목록
CONFIDENTIAL_TOOLS = {"get_employee_salary", "get_department_salary_stats"}
