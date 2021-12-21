import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime as dt

ukhsa_national_case_csv = "data/ukhsa_national_covid_case_rolling_rates_and_admissions.csv"

adm_case_df = pd.read_csv(ukhsa_national_case_csv)
adm_case_df.date = pd.to_datetime(adm_case_df.date)

# No admissions figures in this dataset until 18 March 2020
march_18_2020 = dt(2020, 3, 18)

case_y_original = "newCasesBySpecimenDateRollingRate"
adm_y_original = "newAdmissions"
adm_case_df = adm_case_df[adm_case_df.date > march_18_2020]
adm_case_df.set_index("date", inplace=True)

def main():
    plt.figure(figsize=(16, 8), dpi=250)
    adm_case_df[case_y_original].plot()
    adm_case_df[adm_y_original].plot()
    plt.tight_layout(pad=2)
    from_date = str(adm_case_df.index.min()).split(" ")[0]
    to_date = str(adm_case_df.index.max()).split(" ")[0]
    plt.xlabel(f"Date (from {from_date} to {to_date})")
    plt.ylabel("Count")
    plt.legend()
    #plt.show()
    plt.savefig("plots/rolling_cases_abs_and_admissions.png")

main()
