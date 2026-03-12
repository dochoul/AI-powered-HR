---
name: project_hr_chatbot_overview
description: AI HR 챗봇 프로젝트 개요 - 아키텍처, MVP 범위, 로드맵 확정 내용
type: project
---

## 프로젝트 개요
- 메신저(슬랙/메타모스트)에서 자연어로 직원 인사정보를 조회하는 AI 챗봇
- 대상 사용자: 경영진 (MVP), 추후 팀장/HR담당자/일반직원 확대

## 아키텍처 결정
- LLM은 DB에 직접 접근하지 않음 (의도 분석 + 응답 생성만 담당)
- Function Calling 패턴으로 LLM이 API 호출 결정 -> 시스템이 실행 -> 결과를 LLM이 자연어로 변환
- 권한 검증은 AI 이전 단계에서 수행

## MVP 범위 (Phase 2) - v1.1 업데이트
- 슬랙 DM 기반 질의만 (채널 노출 방지)
- 직원 기본정보 조회: 이름, 부서, 직급, 직책, 입사일, 이메일, 연락처
- 연봉 조회 포함 (v1.1 추가): 개인 연봉, 부서별/직급별 평균 연봉 - 기밀 등급, 경영진/HR 담당자 전용
- 경영진 역할만 조회 가능
- 감사 로그 기록 필수
- 급여 명세서/평가/수정 기능은 MVP 이후 (급여 명세서는 Phase 3)

## MVP 상세 기획 (2026-03-12 작성, v1.1)
- 상세 기획서: docs/mvp-plan.md
- 지원 질문 유형 15가지 (기본 12가지 + 연봉 관련 3가지)
- 6개 Claude Tool 정의: get_employee_by_name, get_employees_by_department, get_employees_by_position, get_recent_hires, get_employee_salary, get_department_salary_stats
- DB 6개 테이블 (employees에 annual_salary, salary_updated_at 컬럼 추가)
- 동명이인 처리: 직전 1턴 컨텍스트만 TTL 5분으로 유지
- 대규모 목록: 20명 초과 시 상위 20명 + "외 N명" 처리
- 개발 태스크 29개 (연봉 관련 6개 추가), Phase 1(기반) 2-3주 + Phase 2(핵심) 3-4주
- 기밀 등급 접근 제어: Tool 실행 전 서버에서 역할 기반 이중 검증

## 보안 등급 분류
- 일반(부서/직급/입사일/직책/이메일) -> 팀장 이상
- 제한(연락처/생년월일) -> HR + 임원
- 기밀(연봉) -> 경영진/HR 담당자만, MVP에서 조회 가능 (이중 검증 + 감사 로그 강화)
- 기밀(급여 명세서/평가) -> Phase 3 이후
- 극비(주민번호/계좌) -> 시스템 조회 원천 차단, DB에 저장하지 않음

## 기술 스택
- 서버: FastAPI (Python), SQLAlchemy 2.0, Alembic
- LLM: Anthropic Claude API (Tool Use)
- DB: PostgreSQL
- 메신저: Slack Bolt for Python
- 컨테이너: Docker + Docker Compose
- 프론트엔드: React + TypeScript + Vite + Hiworks 디자인 시스템

## 로드맵
- Phase 1 (2-3주): 기반 구축 (슬랙봇, 서버, 샘플데이터)
- Phase 2 (3-4주): MVP 핵심 기능
- Phase 3 (4-6주): 근태/급여 확장, 메타모스트, 관리자 대시보드
- Phase 4 (지속): 멀티턴, 통계, 고도화

## 프론트엔드 현황
- React + TypeScript + Vite + Hiworks 디자인 시스템 셋업 완료
- Phase 3에서 관리자 대시보드로 발전 예정
