import streamlit as st
from labels_lang import label_dict
from ui_utils import *
from calc_utils import *

# -------------------------------
# Language Selector
# -------------------------------
lang = st.sidebar.radio("Sprache / Language", ["de", "en"], on_change=lambda: st.session_state.clear())
labels = label_dict[lang]

# -------------------------------
# UI
# -------------------------------
st.title(labels["title"])

total_cost = currency_input(labels["total_cost"], "total_cost", 637000, st)
down_payment = currency_input(labels["down_payment"], "down_payment", 100000, st)
yearly_extra = currency_input(labels["yearly_extra"], "yearly_extra", 0, st)
interest_rate = st.number_input(labels["interest_rate"], value=3.5, step=0.1,min_value=0.0, max_value=20.0)
initial_tilgung = st.number_input(labels["initial_tilgung"], value=4.0, step=0.5, min_value=0.1, max_value=10.0)
years_fixed = st.slider(labels["years_fixed"], 5, 30, 10)


if st.button(labels["calculate"]):
    if st.session_state["total_cost_text"].strip() == "":
        st.error(labels["ERR_totalcost_empty"])
    if st.session_state["down_payment_text"].strip() == "":
        st.error(labels["ERR_downpayment_empty"])
    elif total_cost <= 0:
        st.error(labels["ERR_totalcost_oorlo"])
    elif down_payment < 0:
        st.error(labels["ERR_downpayment_oorlo"])
    elif down_payment >= total_cost:
        st.error(labels["ERR_downpayment_oorhi"])
    elif interest_rate <= 0:
        st.error(labels["ERR_interest_oorlo"])
    elif initial_tilgung <= 0:
        st.error(labels["ERR_tilgung_oorlo"])
    else:
        monthly, df, remaining_debt = mortgage_analysis(
            total_cost, interest_rate, down_payment, initial_tilgung, years_fixed, yearly_extra
        )
        st.subheader(f"{labels['monthly_payment']}: {format_currency(monthly)}")
        st.subheader(f"{labels['remaining_debt']}: {format_currency(remaining_debt)}")

        df_formatted = format_currency_df(df, ["Remaining Debt", "Interest Part", "Principal Part", "Total Interest Paid"])
        df_formatted = format_month_column(df_formatted, labels=labels)
        df_translated = translate_dataframe(df_formatted, labels=labels)

        # --- Plot Interest vs Principal (Interactive) ---
        paymentCompFig = plot_line_chart(
            df,
            x_col="Month",
            y_cols=["Interest Part", "Principal Part"],
            names=[labels["interest"], labels["principal"]],
            colors=["#e63946", "#2a9d8f"],
            title=labels["monthly_breakdown"],
            labels=labels,
            hover_labels=[labels["interest"], labels["principal"]],
            month_to_year_month_func=month_to_year_month
        )
        st.plotly_chart(paymentCompFig, use_container_width=True)

        # --- Plot Remaining Debt (Interactive) ---
        remDebtFig = plot_line_chart(
            df,
            x_col="Month",
            y_cols=["Remaining Debt"],
            names=[labels["remaining_debt"]],
            colors=["#e63946"],
            title=labels["remaining_debt_over_time"],
            labels=labels,
            hover_labels=[labels["remaining_debt"]],
            month_to_year_month_func=month_to_year_month
        )
        st.plotly_chart(remDebtFig, use_container_width=True)

        # csv table
        st.write(f"### {labels['repayment_schedule']}")
        st.dataframe(df_translated, hide_index=True)
