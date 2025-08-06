from models import SessionLocal, QueryLog

session = SessionLocal()
logs = session.query(QueryLog).all()

for log in logs:
    print(log.case_type, log.case_number, log.year, log.response)

session.close()
