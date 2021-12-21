import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime as dt

ukhsa_national_case_csv = "data/ukhsa_national_covid_case_rolling_rates_and_admissions.csv"

adm_case_df = pd.read_csv(ukhsa_national_case_csv)
adm_case_df.date = pd.to_datetime(adm_case_df.date)

# No admissions figures in this dataset until 18 March 2020
march_18_2020 = dt(2020, 3, 18)

case_y_original = "newCasesBySpecimenDateRollingRate"
case_y_lab = "newCasesBySpecimenDateRollingRatePercentageDec2021Peak"
adm_y_original = "newAdmissions"
adm_y_lab = "newAdmissionsPercentageJan2021Peak"
adm_case_df = adm_case_df[adm_case_df.date > march_18_2020]
adm_case_df.set_index("date", inplace=True)

peak_adm_jan_2021 = adm_case_df[adm_y_original].max()
adm_case_df[adm_y_lab] = 100 * adm_case_df[adm_y_original] / peak_adm_jan_2021

peak_case_dec_2021 = adm_case_df[case_y_original].max()
adm_case_df[case_y_lab] = 100 * adm_case_df[case_y_original] / peak_case_dec_2021

def main():
    plt.figure(figsize=(16, 8), dpi=250)
    adm_case_df[case_y_lab].plot()
    adm_case_df[adm_y_lab].plot()
    plt.tight_layout(pad=2)
    from_date = str(adm_case_df.index.min()).split(" ")[0]
    to_date = str(adm_case_df.index.max()).split(" ")[0]
    plt.xlabel(f"Date (from {from_date} to {to_date})")
    plt.ylabel("% of historic peak")
    plt.legend()
    #plt.show()
    plt.savefig("plots/rolling_cases_percentage_and_admissions.png")

main()
