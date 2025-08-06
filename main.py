from flask import Flask, render_template, request, redirect, url_for, flash
from models import SessionLocal, QueryLog
from backend.scraper import fetch_case_details  # Adjust path if needed

app = Flask(__name__)
app.secret_key = 'your-secret-key'  # Needed for flashing messages

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        case_type = request.form.get('case_type')
        case_number = request.form.get('case_number')
        year = request.form.get('year')

        if not (case_type and case_number and year):
            flash("All fields are required.")
            return redirect(url_for('index'))

        # Call scraper
        result = fetch_case_details(case_type, case_number, year)

        # Error check
        if not result or not result.get('order_pdf'):
            flash("No case data found or invalid case number.")
            return redirect(url_for('index'))

        # ✅ Save to database
        session = SessionLocal()
        log = QueryLog(
            case_type=case_type,
            case_number=case_number,
            year=year,
            response=str(result)
        )
        session.add(log)
        session.commit()
        session.close()

        return render_template('result.html', result=result)

    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
