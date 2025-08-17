# this file contains the translation of all possible labels, 
# for now only German and English are supported


# -------------------------------
# Language dictionary
# -------------------------------
label_dict = {
    "en": {
        "title": "🏠 Mortgage Calculator",
        "total_cost": "Total Cost (€)",
        "down_payment": "Down Payment (€)",
        "yearly_extra": "Yearly Extra Payment (€)",
        "interest_rate": "Interest Rate (%)",
        "initial_tilgung": "Initial Tilgung (%)",
        "years_fixed": "Fixed Interest Period (Years)",
        "calculate": "Calculate",
        "monthly_payment": "Fixed Monthly Payment",
        "remaining_debt": "Remaining Debt",
        "repayment_schedule": "Repayment Schedule (downloadable as CSV)",
        "remaining_debt_over_time": "Remaining Debt Over Time",
        "monthly_breakdown": "Monthly Payment Breakdown",
        "principal": "Principal Payment",
        "interest": "Interest Payment",
        "month": "Month",
        "year_label": "Year",
        "month_label": "Month",
        # DataFrame column headers
        "col_principal": "Principal Part",
        "col_interest": "Interest Part",
        "col_total_interest": "Total Interest Paid",
        "col_remaining": "Remaining Debt",
        "col_month": "Year - Month",
        "graph_y_axis": "Amount (€)",
        # Error messages 
        "ERR_totalcost_empty": "❌ Total cost field cannot be empty",
        "ERR_downpayment_empty": "❌ Down payment field cannot be empty",
        "ERR_totalcost_oorlo": "❌ Total cost must be greater than 0.",
        "ERR_downpayment_oorlo": "❌ Down payment cannot be negative",
        "ERR_downpayment_oorhi": "❌ Down payment must be less than the total cost",
        "ERR_interest_oorlo": "❌ Interest rate must be greater than 0",
        "ERR_tilgung_oorlo": "❌ Initial Tilgung must be greater than 0",
    },
    "de": {
        "title": "🏠 Hypothekenrechner",
        "total_cost": "Gesamtkosten (€)",
        "down_payment": "Eigenkapital (€)",
        "yearly_extra": "Jährliche Sondertilgung (€)",
        "interest_rate": "Zinssatz (%)",
        "initial_tilgung": "Anfängliche Tilgung (%)",
        "years_fixed": "Zinsbindungsfrist (Jahre)",
        "calculate": "Berechnen",
        "monthly_payment": "Monatliche Rate",
        "remaining_debt": "Restschuld",
        "repayment_schedule": "Tilgungsplan (CSV-Datei herunterladbar)",
        "remaining_debt_over_time": "Restschuld im Zeitverlauf",
        "monthly_breakdown": "Aufschlüsselung der Monatsrate",
        "principal": "Tilgungsanteil",
        "interest": "Zinsanteil",
        "month": "Monat",
        "year_label": "Jahr",
        "month_label": "Monat",
        # DataFrame column headers
        "col_principal": "Tilgungsanteil",
        "col_interest": "Zinsanteil",
        "col_total_interest": "Gezahlte Zinsen",
        "col_remaining": "Restschuld",
        "col_month": "Jahr - Monat",
        "graph_y_axis": "Betrag (€)",
         # Error messages 
        "ERR_totalcost_empty": "❌ Gesamtkosten-Feld darf nicht leer sein",
        "ERR_downpayment_empty": "❌ Eigenkapital-Feld darf nicht leer sein",
        "ERR_totalcost_oorlo": "❌ Gesamtkosten müssen größer als 0 sein.",
        "ERR_downpayment_oorlo": "❌ Eigenkapital darf nicht negativ sein",
        "ERR_downpayment_oorhi": "❌ Eigenkapital muss kleiner als die Gesamtkosten sein",
        "ERR_interest_oorlo": "❌ Zinssatz muss größer als 0 sein",
        "ERR_tilgung_oorlo": "❌ Tilgung muss größer als 0 sein",
    }
}