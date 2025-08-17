# this file contains the utility functions used for calculations and UI
import plotly.graph_objects as go

# -------------------------------
# ui formatting utilities
# -------------------------------
def format_currency(value: float) -> str:
    return f"€{value:,.0f}"  

def parse_currency(text: str) -> float:
    try:
        val = float(text.replace("€", "").replace(",", "").strip() or 0)
        return max(val, 0)  # prevent negative
    except ValueError:
        return 0.0  # fallback if invalid
    
def currency_input(label: str, key: str, default: float = 0.0, st=None) -> float:
    if(st is None):
        raise ValueError("Streamlit object must be provided")
    else:
        if key not in st.session_state:
            st.session_state[key] = default
            st.session_state[f"{key}_text"] = format_currency(default)

    def _format_callback():
        val = parse_currency(st.session_state[f"{key}_text"])
        st.session_state[key] = val
        st.session_state[f"{key}_text"] = format_currency(val)

    # Use fixed `key` for the text input
    st.text_input(label, key=f"{key}_text", on_change=_format_callback)
    return st.session_state[key]

def format_currency_df(df, cols):
    df_formatted = df.copy()
    for col in cols:
        df_formatted[col] = df_formatted[col].apply(lambda x: f"€{x:,.2f}")
    return df_formatted

def format_month_column(df, labels):
    df_display = df.copy()
    df_display["Month"] = df_display["Month"].apply(
        lambda m: f"{labels['year_label']} {((m-1)//12)+1} – {labels['month_label']} {((m-1)%12)+1}"
    )
    return df_display

def translate_dataframe(df, labels):
    """Rename dataframe columns based on selected language."""
    col_map = {
        "Month": labels["col_month"],
        "Principal Part": labels["col_principal"],
        "Interest Part": labels["col_interest"],
        "Total Interest Paid": labels["col_total_interest"],
        "Remaining Debt": labels["col_remaining"],
    }
    return df.rename(columns=col_map)
    
def month_to_year_month(m, labels):
    year = (m - 1) // 12 + 1
    month = (m - 1) % 12 + 1
    return f"{year} {labels["month"]}: {month}"

# -------------------------------
# interactive plotting functions
# -------------------------------
def plot_line_chart(
    df, 
    x_col, 
    y_cols, 
    names, 
    colors, 
    title, 
    labels, 
    hover_labels, 
    month_to_year_month_func
):
    fig = go.Figure()
    for y_col, name, color, hover_label in zip(y_cols, names, colors, hover_labels):
        fig.add_trace(go.Scatter(
            x=df[x_col], y=df[y_col], mode="lines",
            name=name, line=dict(color=color, width=3),
            text=[month_to_year_month_func(m, labels=labels) for m in df[x_col]],
            hovertemplate=f"{labels['year_label']}: %{{text}}<br>{hover_label}: €%{{y:,.0f}}<extra></extra>"
        ))

    xticks = list(range(0, int(df[x_col].max()) + 1, 12))
    fig.update_xaxes(
        tickmode="array",
        tickvals=xticks,
        ticktext=[str(x // 12) for x in xticks],
        title=labels["year_label"]
    )
    fig.update_yaxes(title=labels["graph_y_axis"])
    fig.update_layout(
        title=title,
        paper_bgcolor="#0E1117",
        plot_bgcolor="#0E1117",
        font=dict(color="white"),
        legend=dict(bgcolor="#0E1117")
    )
    return fig
